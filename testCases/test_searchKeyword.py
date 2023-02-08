import time
import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.UploadDocument import UploadDocument
from pageObjects.SearchKeyword import SearchKeyword
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_SearchKeywordByKeyword_003:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_searchKeywordByKeyword(self, setup):
        self.logger.info("******* SearchKeyword By Keyword********")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        username = input("Enter username: ")
        password = input("Enter password: ")
        self.lp.setUsername(username)
        self.lp.setPassword(password)
        # self.lp.setUsername(self.username)
        # self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("******** Login Succesful ******")


        self.logger.info("***** Searching Keyword By KeywordID *******")
        searchkey = SearchKeyword(self.driver)
        time.sleep(2)
        keyword=input("Enter Keyword: ")
        searchkey.setKeyword(keyword)
        time.sleep(2)
        searchkey.clickSearch()
        time.sleep(3)
        # status=searchkey.setKeyword("Customer")
        #
        # assert True==status
        self.logger.info("***** TC_SearchKeyword_003 Finished *******")




