from selenium import webdriver
from  time import sleep

class TestCase(object):

    def __init__(self):
        self.driver=webdriver.Chrome()
        self.driver.get('https://www.baidu.com')
        self.driver.maximize_window()

    def test_prop(self):
        print(self.driver.name) #浏览器名称
        print(self.driver.current_url)#url
        print(self.driver.title)
        print(self.driver.current_window_handle)
        print(self.driver.page_source)

        self.driver.quit()

    def test_method(self):
        self.driver.find_element_by_id('kw').send_keys('selenium')
        self.driver.find_element_by_id('su').click()
        sleep(2)
        self.driver.back() #后退
        sleep(2)
        self.driver.refresh()#刷新

        self.driver.forward()#前进

        self.driver.close() #只关闭当前tab

        self.driver.quit()



if __name__ == '__main__':
    case=TestCase()
    #case.test_prop()
    case.test_method()