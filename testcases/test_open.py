from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
#创建浏览器对象

class TestOpen:
    def test_open(self):
        driver = webdriver.Chrome(options=options)
        driver.get('https://www.baidu.com')
