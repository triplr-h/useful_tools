# useful_tools
============
> 写一点有意思的小工具<br><br>

## 健康日报自动填写
### 注意事项
> 'info.xlsx'文件里面存有个人信息，与py文件在同一路径下，支持多人次同时填写<br>
### 使用到的包
> 'selenium'爬取数据<br>
> 'pandas'读取Excel文件数据<br>
> 'datatime'自动填写每天的日期<br>
### 可能存在的bug
> 'webdriver'中'Chrome()'的调用需要将chromedriver的可执行文件放入python路径中的script文件夹下。<br>
> [chromedriver下载地址](https://code.google.com/p/chromedriver/downloads/list)<br><br>

## 个人成绩自动查询以及导出
### 注意事项
> 'info.xlsx'文件里面存有个人信息，与py文件在同一路径下，支持多人次同时查询导出<br>
> 内置链接有大二成绩查询链接和大三成绩查询链接<br>
### 使用到的包
> 'selenium'爬取数据<br>
> 'pandas'读取Excel文件数据<br>
> 'collections'合并字典<br>
> 'time'设置延时<br><br>

## 微博热搜榜单
### 注意事项
> 'data.xlsx'文件是输出文件，与py文件在同一路径下<br>
> 用于爬取热度与热搜信息，观察榜单热度变化<br>
### 使用到的包
> 'selenium'爬取数据<br>
> 'pandas'写入Excel文件数据<br>
> 'time'读取当前时间<br>
### 待优化的地方
> 数据输出格式问题，应当以每条热搜单独建立数据链，便于研究单个热搜热度变化<br>
