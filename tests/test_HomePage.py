import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from PageObjects.HomePage import HomePage
from TestData.HomePageData import HomePageData
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self,getData):
        log = self.getLogger()
        #print(driver.title)

        homePage = HomePage(self.driver)
        log.info("First Name is :"+getData["firstname"])
        homePage.getName().send_keys(getData["firstname"])
        log.info("Email is : "+getData["lastname"])
        homePage.getEmail().send_keys(getData["lastname"])
        homePage.getPassword().send_keys("12345")
        homePage.exampleCheck().click()

        # ID, xpath, CSS selector, classname, linktext this are some locators selenium provided.
        #self.driver.find_element(By.NAME, "email").send_keys("testmail@gmail.com")
        #self.driver.find_element(By.ID, "exampleInputPassword1").send_keys("12345")
        #self.driver.find_element(By.ID, "exampleCheck1").click()

        # xpath = //tagname[@attribute = 'Value'] > //input[@value = 'Submit']
        # cssselector = tagname[attibute = 'value']  , #id , .<calssname>
        # self.driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Siddhesh kedari")
        # not implement self.driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()

        # Static dropdown
        #self.driver.implicitly_wait(1000)

        self.selectOptionByText(HomePage.getGender(self), getData["gender"])

        self.driver.find_element(By.XPATH, "//input[@value = 'Submit']").click()

        messageVar = self.driver.find_element(By.CLASS_NAME, "alert-success").text
        print(messageVar)
        assert "Success" in messageVar

        #self.driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("Hello Again")
        #self.driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()
        # driver.close()

        self.driver.refresh()



    #@pytest.fixture(params=[('Siddhesh','skTest@gmail.com','Male'),('Siddhi','skTest@gmail.com','Female')])
    @pytest.fixture(params=HomePageData.getTestData("Testcase2"))
    def getData(self, request):
        return request.param
