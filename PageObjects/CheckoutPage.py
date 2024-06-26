from selenium.webdriver.common.by import By

from PageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    #driver.find_elements(By.XPATH, "//div[@class='card h-100']")
    cardList = (By.XPATH, "//div[@class='card h-100']")
    productName = (By.XPATH, "//div/h4/a")
    selectProduct = (By.XPATH, "div/h4/a")
    checkoutButton = (By.XPATH, "//a[@class='nav-link btn btn-primary']")
    finalCheckOutButton = (By.CSS_SELECTOR, "button[class='btn btn-success']")

    def getCardDetails(self):
        return self.driver.find_elements(*CheckoutPage.cardList) #Too deserialise tupple we need to give *


    def getProductName(self):
        return self.driver.find_element(*CheckoutPage.productName)


    def getSelectProduct(self):
        return self.driver.find_element(*CheckoutPage.selectProduct)


    def getCheckOut(self):
        return self.driver.find_element(*CheckoutPage.checkoutButton)


    def finalCheckOut(self):
        self.driver.find_element(*CheckoutPage.finalCheckOutButton).click()
        confirmpage = ConfirmPage(self.driver)
        return confirmpage







