# @author zhangchao
# @date 2020/5/30 11:05
from selenium import webdriver
import os
import time

'''
   头条PC端自动发布评论并保存截图
'''


class TouTiao:

    def __init__(self,username,password,img_path,):
        options = webdriver.ChromeOptions()

        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(chrome_options=options)
        if not img_path or not os.path.exists(img_path):
            save_dir = os.getcwd()
        else:
            save_dir = img_path
        img_dir_name = time.strftime("%Y%m", time.localtime())
        self.save_dir = os.path.join(save_dir,img_dir_name)

        pass

    def login(self):          # 需要手动操作
        self.driver.get('https://sso.toutiao.com/')
        self.driver.implicitly_wait(30)

        self.driver.find_element_by_id("login-type-account").click()
        self.driver.implicitly_wait(10)

        self.driver.find_element_by_id("user-name").send_keys(self.username)
        self.driver.find_element_by_id("password").send_keys(self.password)

        self.driver.find_element_by_id("bytedance-login-submit").click()

        time.sleep(50)  # 确保用户手动登录成功
        print(self.driver.title)

    def open_url(self, url, index=0):
        try:
            if index % 10 == 0:
                self.driver.get(url)
            else:
                s = "window.open(' {} ')".format(url)
                self.driver.execute_script(s)  # 打开多个窗口
            self.driver.implicitly_wait(20)
        except Exception as e:
            print(str(e))
            time.sleep(30)

    def public_comments(self,content):
        try:
            url = self.driver.current_url
            self.driver.find_element_by_css_selector("a.share-count").click()
            self.driver.implicitly_wait(3)
            self.driver.find_element_by_xpath("//textarea").send_keys(content)
            self.driver.implicitly_wait(10)
            self.driver.find_element_by_css_selector('div[class=c-submit]').click()
            self.driver.implicitly_wait(30)
            filename = ''
            if url.endswith('/'):
                filename = url.rsplit('/', 2)[1]
            else:
                filename = url.rsplit('/', 1)[1]
            if not os.path.exists(self.save_dir):
                os.mkdir(self.save_dir)
            self.driver.save_screenshot(os.path.join(self.save_dir,filename + ".png"))
        except Exception as e:
            print(str(e))
            pass

    def get_driver(self):
        return self.driver

    def close(self):
        self.driver.close()
