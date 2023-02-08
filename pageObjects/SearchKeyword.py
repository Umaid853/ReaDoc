from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchKeyword():

    txtKeyword_xpath = '/html/body/div/div/div[2]/div/div/div[1]/div/form/div/div[1]/div[2]/div/input'
    btnSearch_xpath='//*[@id="search-btn"]'

    def __init__(self, driver):
        self.driver = driver

    def setKeyword(self,keyword):
        # element = WebDriverWait(self.driver, 10).until\
        #     (EC.presence_of_element_located((By.XPATH, self.txtKeyword_xpath)))
        self.driver.find_element(By.XPATH,self.txtKeyword_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtKeyword_xpath).send_keys(keyword)

    def clickSearch(self):
        self.driver.find_element(By.XPATH, self.btnSearch_xpath).click()