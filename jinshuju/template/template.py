# 为金数据问卷设置一个模板，里面有常用的函数
# coding:utf-8
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from collections import defaultdict
from selenium import webdriver
import pandas as pd
import datetime
import time

# 网页初始化
def init_webdriver(start_url):
    driver = webdriver.Chrome()
    driver.get(start_url)
    return driver

# 读取信息
def read_xlsx(filename):
    df = pd.read_excel(filename)
    read_list = df.loc[0:].values #去掉表头
    return read_list

# 信息框输入
def input_info(driver, info_list):
    # 日期
    try:
        day = driver.find_element_by_id('entry_field_13')
        day.send_keys(str(datetime.date.today()))
    except:
        pass

    # 姓名
    try:
        name = driver.find_element_by_id('q_0_field_3')
        name.clear()
        name.send_keys(info_list[0])
    except:
        pass

    # 学号
    try:
        stu_id = driver.find_element_by_id('entry_field_2')
        stu_id.clear()
        stu_id.send_keys(info_list[1])
    except:
        pass
        
    # 身份证号
    try:
        person_id = driver.find_element_by_id('q_0_field_14')
        person_id.clear()
        person_id.send_keys(info_list[2])
    except:
        pass

    # 老师姓名
    try:
        teacher_name = driver.find_element_by_id('entry_field_27')
        teacher_name.clear()
        teacher_name.send_keys(info_list[3])
    except:
        pass
        
    # 下拉框选择思政
    try:
        teacher_select = Select(driver.find_element_by_id('entry_field_11'))
        teacher_select.select_by_visible_text(info_list[4])
    except:
        pass

# 单选点击
def click_xpath(driver, xpath):
    driver.find_element_by_xpath(xpath).click()
    time.sleep(1)  # 有的题目会跳转

# 单击空白处
def click_blank(driver):
    ActionChains(driver).move_by_offset(200, 100).click().perform()

# 查询信息专属
def get_info(driver):
    temp_list = [[], []]  # 第一个储存表头信息，第二个储存内容，暂存的数据列表
    data_dict = {}  # 返回的数据字典
    data_list = []  # 返回的数据列表
    tr_list = driver.find_elements_by_tag_name('tr')
    for tr in tr_list:
        td_list = tr.find_elements_by_tag_name('td')
        temp_list[0].append(td_list[0].text)
        temp_list[1].append(td_list[1].text)
    data_dict = dict(zip(temp_list[0], temp_list[1]))
    return data_dict

# 查询数据处理
def process_data(data_list):
    final_dict = {}
    for stu in data_list:
        for keys, values in stu.items():
            final_dict.setdefault(keys, []).append(values)
    return final_dict

# 写入xlsx
def write_xlsx(final_dict):
    process = pd.DataFrame(final_dict)
    process.to_excel('data.xlsx', encoding='utf-8', startcol=0, index=False)

# 查询数据总函数
def fill_info(driver, start_url, filename):
    read_list = read_excel(filename)
    for info_list in read_list:
        input_info(driver, info_list)
        click_xpath(driver, '//*[@id="new_entry"]/div[2]/div/div[4]/div[7]/div/div[2]/div/label[2]/div')
        click_blank(driver)
        # click_xpath(driver, '//*[@id="new_entry"]/div[2]/div/div[5]/input[1]')  # 注释掉提交按钮
        driver.get(start_url)

def refer_data(driver, start_url, filename):
    read_list = read_xlsx(filename)
    data_list = []
    for info_list in read_list:
        input_info(driver, info_list)
        click_xpath(driver, '/html/body/div/div[2]/div/div/div[2]/form/div[2]/input')
        data_dict = get_info(driver)
        data_list.append(data_dict)
        driver.get(start_url)
    final_dict = process_data(data_list)
    write_xlsx(final_dict)



if __name__ == "__main__":
    start_url = 'https://jinshuju.net/f/MLanfB/s/IrVohq'
    filename = 'read_data.xlsx'
    driver = init_webdriver(start_url)
    # fill_info(driver, start_url, filename)
    refer_data(driver, start_url, filename)
    driver.quit()
