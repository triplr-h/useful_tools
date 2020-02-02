# useful_tools

  写一点有意思的小工具

## 健康日报自动填写

+ 注意事项

  'info.xlsx' 文件里面存有个人信息，与py文件在同一路径下，支持多人次同时填写

+ 使用到的包

  'selenium' 爬取数据
  'pandas' 读取Excel文件数据
  'datatime' 自动填写每天的日期

+ 可能存在的bug

  'webdriver' 中 'Chrome()' 的调用需要将chromedriver的可执行文件放入python路径中的script文件夹下。
  [chromedriver下载地址](https://code.google.com/p/chromedriver/downloads/list)

## 个人成绩自动查询以及导出

+ 注意事项

  'info.xlsx' 文件里面存有个人信息，与py文件在同一路径下，支持多人次同时查询导出
  内置链接有大二成绩查询链接和大三成绩查询链接

+ 使用到的包

  'selenium' 爬取数据
  'pandas' 读取Excel文件数据
  'collections' 合并字典
  'time' 设置延时

## 微博热搜榜单

+ 注意事项

  'data.xlsx' 文件是输出文件，与py文件在同一路径下
  用于爬取热度与热搜信息，观察榜单热度变化

+ 使用到的包

  'selenium' 爬取数据
  'pandas' 写入Excel文件数据
  'time' 读取当前时间

+ 待优化的地方

  ~~数据输出格式问题，应当以每条热搜单独建立数据链，便于研究单个热搜热度变化~~
  ~~看完主持人大赛回来更新~~
  ~~后台不用打开浏览器就能运行~~
  希望能够做到每10min保存一次，新出现的榜单自动加到后面，新保存的时间加到下面
  继续学习数据库，希望用数据库来解决数据的存储问题会更加方便
  