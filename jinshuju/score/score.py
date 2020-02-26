# coding:utf-8

from selenium import webdriver
from collections import defaultdict
import pandas as pd
import time


# 提取数据，储存到字典person
df = pd.read_excel('info.xlsx')
name_list = df['姓名'].values
id_number_list = df['身份证号'].values
#id_number_dict = dict(zip('身份证号', id_number_list))
person = dict(zip(name_list, id_number_list))
# print(person)

# 网页初始化
#driver = webdriver.PhantomJS(    executable_path=r'G:\phantomjs-2.1.1-windows\bin\phantomjs.exe')
driver = webdriver.Chrome()
# driver.get('https://jinshuju.net/f/UtULIS/s/IbywKK') #大二下
driver.get('https://jinshuju.net/f/MLanfB/s/IrVohq')  # 大三上
# elem.send_keys(Keys.ENTER)  #相当于点击键盘上的Enter按钮

# 将不同数据填写到问卷里，并获取每个人的信息
#url_list = []
head_list = [] # 每个人成绩的表头，相当于表格的第一行
content_list = [] # 每个人的成绩内容，相当于表格的第二行，由这两个组成字典
person_list = []
for name in person:
    elem = driver.find_element_by_id('q_0_field_3') #姓名
    #time.sleep(0.2)
    elem2 = driver.find_element_by_id('q_0_field_14') #身份证号
    #time.sleep(0.2)
    elem.send_keys(name)
    #time.sleep(0.2)
    elem2.send_keys(person[name])
    #time.sleep(0.2)
    driver.find_element_by_xpath(
    '/html/body/div/div[2]/div/div/div[2]/form/div[2]/input').click()
    #time.sleep(0.2)
    #driver.refresh()
    #url_list.append(driver.current_url)
    tr_list = driver.find_elements_by_tag_name('tr')
    #time.sleep(0.2)
    for tr in tr_list:
        td_list = tr.find_elements_by_tag_name('td')
        #time.sleep(0.2)
        head_list.append(td_list[0].text)
        content_list.append(td_list[1].text)
    person_dict = dict(zip(head_list, content_list))
    person_list.append(person_dict)  
    
    # driver.get('https://jinshuju.net/f/UtULIS/s/IbywKK') #大二下
    driver.get('https://jinshuju.net/f/MLanfB/s/IrVohq') #大三上
    #time.sleep(0.2)
#print(person_list) #储存有所有人信息的list
#print(content_list)
#print(driver.current_url)  # 当前页面url
# print(driver.page_source) #网页内容

# 格式整理
final_dict = {}
for student in person_list:
    for keys, values in student.items():
        final_dict.setdefault(keys, []).append(values)
#print(final_dict)

process = pd.DataFrame(final_dict)
#id_num = pd.DataFrame(id_number_dict)
#print(process)
#id_num.to_excel('class_score.xlsx', encoding='utf-8', startcol=0, index=False)
process.to_excel('class_score_second.xlsx', encoding='utf-8', startcol=0, index=False)
driver.quit()
