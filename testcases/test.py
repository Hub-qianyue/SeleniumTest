from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
#创建浏览器对象
driver = webdriver.Chrome(options=options)
driver.get('https://www.baidu.com')