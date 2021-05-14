from selenium import webdriver
from  time import sleep

from selenium.webdriver.common.by import By


def test2():
    driver = webdriver.Chrome()
    driver.get('http://www.baidu.com')
    sleep(1)
    driver.find_element_by_id('kw').send_keys('selenium')
    sleep(1)
    driver.find_element_by_id('su').click()
    sleep(3)

    driver.quit()


class TestCase(object):
    def __init__(self):
        self.driver=webdriver.Chrome()

    def test(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.baidu.com')
        sleep(1)
        #self.driver.find_element_by_id('kw').send_keys('selenium')
        self.driver.find_element(By.ID,value='kw').send_keys('selenium')
        sleep(1)
        self.driver.find_element_by_id('su').click()
        sleep(3)

        self.driver.quit()

if __name__ == '__main__':
    #test2()
    case=TestCase()
    case.test()

