# 自动化发布评论脚本
- [x] 今日头条
- [ ] 百度
- [ ] 微博

## 预置条件
### 安装python3.6.x 及以上版本
### 下载google chormedriver驱动 
1. 更新谷歌浏览器
2. 获取谷歌浏览器版本
1. 下载对应版本的Chromedriver，解压到python安装目录下Scripts文件夹（下载地址：http://chromedriver.storage.googleapis.com/index.html）

## 执行脚本
1. 下载脚本到本机目录
1. 进入脚本目录，执行pip install -r requirements.txt
1. 编辑toutiao_url.csv文件，输入需要发布评论的url,没有执行成功前，status状态为0，执行成功后状态自动设为1
1. 编辑comments.csv,这是一个所有评论汇总文件，每次发布评论时会从这些评论中随机挑选一个文件
1. 编辑main.py文件，输入头条的用户名和密码
``` python
username = "zhangchao@tcl.com" # 头条用户名称
password = "123415814"         # 头条用户密码
img_path = ''                  # 图片存放目录,默认为当前目录
number = 100                   # 最大截图评论数
page_count = 10                # 每次打开10个窗口
urls_path = "toutiao_url.csv"  # 待评论url文件
comment_path = "comments.csv"  # 评论汇总文件
```
6. 执行python main.py ,默认会打开头条登录页面，需要手动拖动验证码，之后程序会自动打开url并发布评论、截图
