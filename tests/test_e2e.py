import pytest
from selenium import webdriver


from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.CheckoutPage import CheckoutPage
from PageObjects.ConfirmPage import ConfirmPage
from PageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


#@pytest.mark.usefixtures("setup")
class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        #setup.find_element_by_css_selector("a[href*='shop']").click()
        checkoutPage = homePage.shopItems()
        log.info("Getting all the card titles.")
        #checkoutPage = CheckoutPage(self.driver)
        mobileList = checkoutPage.getCardDetails()
        #productName = checkoutPage.getProductName()

        for mlist in mobileList:

            productList = checkoutPage.getProductName().text

            productList = mlist
            log.info(productList)

            if productList == "Blackberry":
                selectedProdut = checkoutPage.getSelectProduct()
                mlist.selectedProdut.click()

        #self.driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
        checkoutPage.getCheckOut().click()

        #self.driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-success']").click()
        #checkoutPage.finalCheckOut().click()

        #self.driver.find_element(By.ID, "country").send_keys("India")

        sendName = checkoutPage.finalCheckOut()
        log.info("Entering country name : India")
        sendName.selectCountry().send_keys("India")

        #wait = WebDriverWait(self.driver, 10)
        #wait.until(EC.presence_of_element_located((By.LINK_TEXT, 'India')))  # (By.LINK_TEXT, "India"))

        self.verifyLinkPresence("India")
        sendName.selectDrop().click()

        #self.driver.find_element(By.XPATH, "//div[@class = 'checkbox checkbox-primary']").click()
        sendName.selectCheckBox().click()

        #self.driver.find_element(By.XPATH, "//input[@value='Purchase']").click()
        sendName.clickOnPurchaseButton().click()

        textContainer = self.driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
        log.info("Text received form application is : "+textContainer)
        assert "Success! Thank you!" in textContainer

