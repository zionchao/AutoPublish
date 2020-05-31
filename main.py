# coding:utf-8
# @author zhangchao
# @date 2020/5/31 20:24
from toutiao import TouTiao
from csv_utils import *
import random
import time


username = "zhangchao@tcl.com" # 头条用户名称
password = "123415814"         # 头条用户密码
img_path = ''                  # 图片存放目录,默认为当前目录
number = 100                   # 最大截图评论数
page_count = 10                # 每次打开10个窗口
urls_path = "toutiao_url.csv"  # 待评论url文件
comment_path = "comments.csv"  # 评论汇总文件


def start(url_path, comment_path):
    driver=None
    try:
        toutiao = TouTiao(username,password,img_path)
        # toutiao1.login()

        driver = toutiao.get_driver()
        url_items = read_contents(url_path)              # 需要发布评论的url
        if len(url_items) > number:
            url_items = random.sample(url_items, number)

        comments = read_contents(comment_path,codec="gbk")                        # 评论内容 csv为中文时，需要指定编码格式

        for i, item in enumerate(url_items):
            if item[1] == '1':
                print("当前url={}已经发布评论".format(item[0]))
                continue
            toutiao.open_url(item[0], i)
            item[1] = '1'
            if i > 0 and (i % (page_count-1) == 0 or i >= len(url_items)-1):      # 一次打开10个窗口
                count = len(driver.window_handles)
                for index, handle in enumerate(driver.window_handles):
                    # print("current index={}".format(index))
                    if i > page_count and index == 0:
                        continue
                    driver.switch_to.window(handle)  # 切换窗口
                    random_index = random.randint(0, len(comments)-1)
                    toutiao.public_comments(comments[random_index])
                update_item(url_path,url_items)
                for index,handle in enumerate(driver.window_handles):              # 更新url标志，确认已经发布成功
                    driver.switch_to.window(handle)
                    if index != count-1:                                           # 保留一个窗口，防止浏览器退出
                        driver.close()
                        pass
        time.sleep(10)
    finally:
        if driver:
            driver.quit()  # 关闭driver（关闭窗口并结束chromedriver.exe进程）


if __name__ == '__main__':
    start(urls_path, comment_path)