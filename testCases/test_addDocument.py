import pytest
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.UploadDocument import UploadDocument
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random


class Test_002_UploadDocument:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_uploadDocument(self,setup):
        self.logger.info("********* Test_002_UploadDocument **********")
        self.driver=setup
        self.driver.get(self.baseURL)
        time.sleep(2)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        username = input("Enter username: ")
        password = input("Enter password: ")
        self.lp.setUsername(username)
        self.lp.setPassword(password)
        self.lp.clickLogin()
        self.logger.info("******** Login Successful *******")

        self.logger.info("******* Start Upload Document Test ***********")

        self.uploadDocument = UploadDocument(self.driver)
        self.uploadDocument.clickOnUploadDocument()
        self.logger.info("******* Providing Document Information  ***********")
        ProjectName = input("Enter Project Name: ")
        self.uploadDocument.setProjectName(ProjectName)
        ProjectNo = input("Enter Project No: ")
        self.uploadDocument.setProjectNo(ProjectNo)
        SupplierName = input("Enter Supplier Name: ")
        self.uploadDocument.setSupplierName(SupplierName)
        Discipline = input("Enter Discipline: ")
        self.uploadDocument.setDiscipline(Discipline)
        ActivityNumber = input("Enter Activity Number: ")
        self.uploadDocument.setActivityNumber(ActivityNumber)
        Operation = input("Enter Operation: ")
        self.uploadDocument.setOperation(Operation)
        Subpart = input("Enter Subpart: ")
        self.uploadDocument.setSubpart(Subpart)
        DocumentRevised = input("Enter Document Revised: ")
        self.uploadDocument.setDocumentRevised(DocumentRevised)
        FileTrackingNumber = input("Enter File Tracking Number: ")
        self.uploadDocument.setFileTrackingNumber(FileTrackingNumber)
        self.uploadDocument.clickonSubmit()
        self.logger.info("******* Saving Document Information  ***********")


