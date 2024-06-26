from selenium.webdriver.common.by import By



class ConfirmPage():

    def __init__(self,driver):
        self.driver = driver

    countrySelect = (By.ID, "country")

    selectDropdown = (By.LINK_TEXT, "India")

    checkBoxClick = (By.CSS_SELECTOR, ".checkbox.checkbox-primary")

    purchaseButton = (By.XPATH, "//input[@value='Purchase']")


    def selectCountry(self):
        return self.driver.find_element(*ConfirmPage.countrySelect)


    def selectDrop(self):
        return self.driver.find_element(*ConfirmPage.selectDropdown)


    def selectCheckBox(self):
        return self.driver.find_element(*ConfirmPage.checkBoxClick)


    def clickOnPurchaseButton(self):
        return self.driver.find_element(*ConfirmPage.purchaseButton)

