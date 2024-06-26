from selenium.webdriver.common.by import By

from PageObjects.CheckoutPage import CheckoutPage



class HomePage:

    #Step3 Create constructor
    def __init__(self,driver):  #This treat as class own constructor
        self.driver = driver



     #Step 1
    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    email = (By.XPATH, "//input[@name='email']")
    passwd = (By.ID, "exampleInputPassword1")
    checkBox = (By.ID, "exampleCheck1")
    firstname = (By.CSS_SELECTOR, "input[name='name']")
    selectGender = (By.ID, "exampleFormControlSelect1")

    #Step2
    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutpage = CheckoutPage(self.driver)
        return checkoutpage
        #Shop is a class variable so we called it <classname.shop>
        #driver.find_element(By.CSS_SELECTOR, "a[href*='shop']") This step mension as step 1 and step2
        #Instance veriable, Instance variable is a part of the Object constructor.
        #If we want to deserialize the tupple we use *, So system understand this variable as tupple

    #Basic setup of POM is end ^^^^^^^^^^^

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getPassword(self):
        return self.driver.find_element(*HomePage.passwd)


    def exampleCheck(self):
        return self.driver.find_element(*HomePage.checkBox)

    def getName(self):
        return self.driver.find_element(*HomePage.firstname)

    def getGender(self):
        return self.driver.find_element(*HomePage.selectGender)


