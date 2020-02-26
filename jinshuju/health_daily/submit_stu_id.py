# coding:utf-8
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import pandas as pd
import datetime
import time

driver = webdriver.Chrome()
driver.get('https://jinshuju.net/f/enG1Hm')

df = pd.read_excel('stu_id.xlsx', sheetname= 'Sheet1') #出国的sheetname是'Sheet2'
origin_list = df.loc[0:].values #去掉表头
for info_list in origin_list:
    '''
    day = driver.find_element_by_id('entry_field_13')  # 找到日期
    date_str = datetime.date.today()
    day.send_keys(str(datetime.date.today()))  # 填写日期
    '''
    name = driver.find_element_by_id('entry_field_1') #姓名
    name.clear()
    name.send_keys(info_list[0])

    id_number = driver.find_element_by_id('entry_field_2') #学号
    id_number.clear()
    id_number.send_keys(str(info_list[1]))
    '''
    class_id = driver.find_element_by_id('entry_field_35')
    class_id.send_keys(info_list[2].replace('F', ''))

    teacher_name = driver.find_element_by_id('entry_field_27')
    teacher_name.send_keys(info_list[3])
    
    teacher_select = Select(driver.find_element_by_id('entry_field_11'))
    teacher_select.select_by_visible_text(info_list[4])

    ActionChains(driver).move_by_offset(200, 100).click().perform()  # 把日历的弹窗去掉
    '''
    driver.find_element_by_xpath(
        '//*[@id="new_entry"]/div[2]/div/div[4]/div[3]/div/div[2]/div/label[1]/div').click()
    time.sleep(2)#有课

    #driver.find_element_by_xpath('//*[@id="new_entry"]/div[2]/div/div[4]/div[3]/div/div[2]/div/label[2]/div').click() #出国的这个之后直接接提交，无课
    
    driver.find_element_by_xpath(
        '//*[@id="new_entry"]/div[2]/div/div[4]/div[4]/div/div[2]/div[2]/label[1]/div').click()#无困难

    #driver.find_element_by_xpath('//*[@id="new_entry"]/div[2]/div/div[5]/input[1]').click() #提交，默认注释掉
    time.sleep(1)
    driver.get('https://jinshuju.net/f/enG1Hm')

driver.quit()
