# coding:utf-8
from selenium import webdriver
import pandas as pd
import time

# time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) #记录当前日期时间

# 网页初始化
driver = webdriver.Chrome()
driver.get('https://s.weibo.com/top/summary?cate=realtimehot')

search_list = driver.find_element_by_xpath('//*[@id="pl_top_realtimehot"]/table/tbody')  # 找到热搜列表
rank_list = []  # 序号
name_list = []  # 热搜名称
numb_list = []  # 热度
time_list = []  # 储存时间
elements_list = search_list.find_elements_by_tag_name('tr')
tr_list = elements_list[1:]
for tr in tr_list:
    td_list = tr.find_elements_by_tag_name('td')
    rank_list.append(td_list[0].text)
    name = tr.find_element_by_tag_name('a').text
    name_list.append(name)
    number = tr.find_element_by_tag_name('span').text
    numb_list.append(number)

for clock in range(len(name_list)):
    clock_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    time_list.append(clock_time)

final_dict = {
    '时间': time_list,
    '序号': rank_list,
    '热搜名称': name_list,
    '热度': numb_list,
}
#print(name_list)

pd.DataFrame(final_dict).to_excel('data.xlsx', encoding='utf-8', startcol=0, index=False)

driver.quit()