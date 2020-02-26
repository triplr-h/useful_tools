# coding:utf-8
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import pandas as pd
import time

clock = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  # 记录当前日期时间

# 网页初始化
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_options)
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
    name = tr.find_element_by_tag_name('a').text
    name_list.append(name)
    number = tr.find_element_by_tag_name('span').text
    numb_list.append(number)

clock = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  # 记录当前日期时间
final_dict = {'时间': clock}
temp_dict = dict(zip(name_list, numb_list))
final_dict.update(temp_dict)

pd.DataFrame(final_dict, index=[0]).to_excel('data.xlsx', encoding='utf-8', startcol=0)
