
import shelve
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class TestDemo():
    def setup_method(self, method):
        options = Options()
        options.debugger_address = "127.0.0.1:9227"
        self.driver = webdriver.Chrome() #使用(options=options)复用技术获cookie信息
        # self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_demo(self):
        # print(self.driver.get_cookies())
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        db = shelve.open("cookies") #使用shelve打开一个文件
        # db['cookie'] = self.driver.get_cookies() #把cookie信息存储到shelve里面
        cookies = db['cookie']
        for cookie in cookies:
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        sleep(3)
        db.close()

