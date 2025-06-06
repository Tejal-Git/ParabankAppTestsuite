import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class Registerpage:
    textbox_firstname_id="customer.firstName"
    textbox_lastname_id="customer.lastName"
    textbox_address_id="customer.address.street"
    textbox_city_id="customer.address.city"
    textbox_state_id="customer.address.state"
    textbox_zipcode_id="customer.address.zipCode"
    textbox_phone_id="customer.phoneNumber"
    textbox_ssn_id="customer.ssn"
    textbox_username_id="customer.username"
    textbox_password_id="customer.password"
    textbox_confirm_password_id="repeatedPassword"
    btn_register_XPATH="//*[@id='customerForm']/table/tbody/tr[13]/td[2]/input"

    def __init__(self,driver):
        self.driver=driver

    def addfirstname(self,firstname):
        self.driver.find_element(By.ID, self.textbox_firstname_id).clear()
        self.driver.find_element(By.ID, self.textbox_firstname_id).send_keys(firstname)

    def addlastname(self,lastname):
        self.driver.find_element(By.ID, self.textbox_lastname_id).clear()
        self.driver.find_element(By.ID, self.textbox_lastname_id).send_keys(lastname)

    def addaddress(self,address):
        self.driver.find_element(By.ID, self.textbox_address_id).clear()
        self.driver.find_element(By.ID, self.textbox_address_id).send_keys(address)

    def addcity(self,city):
        self.driver.find_element(By.ID,self.textbox_city_id).clear()
        self.driver.find_element(By.ID, self.textbox_city_id).send_keys(city)

    def addstate(self,state):
        self.driver.find_element(By.ID, self.textbox_state_id).clear()
        self.driver.find_element(By.ID, self.textbox_state_id).send_keys(state)

    def addzipcode(self,zipcode):
        self.driver.find_element(By.ID, self.textbox_zipcode_id).clear()
        self.driver.find_element(By.ID, self.textbox_zipcode_id).send_keys(zipcode)

    def addphone(self,phone):
        self.driver.find_element(By.ID, self.textbox_phone_id).clear()
        self.driver.find_element(By.ID, self.textbox_phone_id).send_keys(phone)

    def addssn(self,ssn):
        self.driver.find_element(By.ID, self.textbox_ssn_id).clear()
        self.driver.find_element(By.ID, self.textbox_ssn_id).send_keys(ssn)

    def setUsername(self,username):
        self.driver.find_element(By.ID,self.textbox_username_id).clear()
        self.driver.find_element(By.ID,self.textbox_username_id).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element(By.ID,self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def setconfirmpassword(self,confirmpassword):
        self.driver.find_element(By.ID, self.textbox_confirm_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_confirm_password_id).send_keys(confirmpassword)

    def clickconfirm(self):
        self.driver.find_element(By.ID, self.btn_register_XPATH).click()
