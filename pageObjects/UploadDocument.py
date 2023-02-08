import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

class UploadDocument():
    #Upload Document
    #lnkUploadDocument_menu_xpath="/html/body/div/nav/div[2]/ul/li/button"
    btnUploadDocument_xpath="/html/body/div/nav/div[2]/ul/li/button"
    txtProjectName_xpath="/html/body/div/div/div/div/div/div/form/div[2]/div[1]/div/input"
    txtProjectNo_xpath ="/html/body/div/div/div/div/div/div/form/div[2]/div[2]/div/input"
    txtSupplierName_xpath ="/html/body/div/div/div/div/div/div/form/div[3]/div[1]/div/input"
    txtDiscipline_xpath ="/html/body/div/div/div/div/div/div/form/div[3]/div[2]/div/input"
    txtActivityNumber_xpath ="/html/body/div/div/div/div/div/div/form/div[4]/div[1]/div/input"
    txtOperation_xpath ="/html/body/div/div/div/div/div/div/form/div[4]/div[2]/div/input"
    txtSubpart_xpath ="/html/body/div/div/div/div/div/div/form/div[5]/div[1]/div/input"
    txtDocumentRevised_xpath ="/html/body/div/div/div/div/div/div/form/div[5]/div[2]/div/input"
    txtFileTrackingNumber_xpath ="/html/body/div/div/div/div/div/div/form/div[6]/div/div/input"
    btnSubmit_xpath ="/html/body/div/div/div/div/div/div/form/div[7]/div/button"


    def __init__(self, driver):
        self.driver = driver

    def clickOnUploadDocument(self):
        self.driver.find_element(By.XPATH, self.btnUploadDocument_xpath).click()
        time.sleep(2)

    def setProjectName(self,ProjectName):
        self.driver.find_element(By.XPATH, self.txtProjectName_xpath).send_keys(ProjectName)
        time.sleep(2)

    def setProjectNo(self,ProjectNo):
        self.driver.find_element(By.XPATH, self.txtProjectNo_xpath).send_keys(ProjectNo)
        time.sleep(2)

    def setSupplierName(self,SupplierName):
        self.driver.find_element(By.XPATH, self.txtSupplierName_xpath).send_keys(SupplierName)
        time.sleep(2)

    def setDiscipline(self,Discipline):
        self.driver.find_element(By.XPATH, self.txtDiscipline_xpath).send_keys(Discipline)
        time.sleep(2)

    def setActivityNumber(self,ActivityNumber):
        self.driver.find_element(By.XPATH, self.txtActivityNumber_xpath).send_keys(ActivityNumber)
        time.sleep(2)

    def setOperation(self,Operation):
        self.driver.find_element(By.XPATH, self.txtOperation_xpath).send_keys(Operation)
        time.sleep(2)

    def setSubpart(self,Subpart):
        self.driver.find_element(By.XPATH, self.txtSubpart_xpath).send_keys(Subpart)
        time.sleep(2)

    def setDocumentRevised(self,DocumentRevised):
        self.driver.find_element(By.XPATH, self.txtDocumentRevised_xpath).send_keys(DocumentRevised)
        time.sleep(2)

    def setFileTrackingNumber(self,FileTrackingNumber):
        self.driver.find_element(By.XPATH, self.txtFileTrackingNumber_xpath).send_keys(FileTrackingNumber)
        time.sleep(2)

    def clickonSubmit(self):
        self.driver.find_element(By.XPATH, self.btnSubmit_xpath).click()


