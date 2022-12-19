from time import sleep

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class User:
    def __init__(self, driver, title, firstname, lastname, email, password, birthday):
        self.driver = driver
        self.title = title
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
        self.birthday = birthday

    def fill_register_form(self, sec):
        if self.title == "Pan":
            self.driver.find_element(By.ID, "field-id_gender-1").click()
        else:
            self.driver.find_element(By.ID, "field-id_gender-2").click()
        sleep(sec)
        self.driver.find_element(By.ID, "field-firstname").send_keys(self.firstname)
        sleep(sec)
        self.driver.find_element(By.ID, "field-lastname").send_keys(self.lastname)
        sleep(sec)
        self.driver.find_element(By.ID, "field-email").send_keys(self.email)
        sleep(sec)
        self.driver.find_element(By.ID, "field-password").send_keys(self.password)
        sleep(sec)
        self.driver.find_element(By.ID, "field-birthday").send_keys(self.birthday)
        sleep(sec)
        self.driver.find_element(By.XPATH, '//*[@id="customer-form"]/div/div[8]/div[1]/span/label/input').click()
        sleep(sec)
        self.driver.find_element(By.XPATH, '//*[@id="customer-form"]/div/div[10]/div[1]/span/label/input').click()
        sleep(sec)
        self.driver.find_element(By.XPATH, '// *[ @ id = "customer-form"] / footer / button').click()
        sleep(sec)

    def fill_address_form(self, sec, address, postcode, city):
        self.driver.find_element(By.ID, "field-address1").send_keys(address)
        sleep(sec)
        self.driver.find_element(By.ID, "field-city").send_keys(city)
        sleep(sec)
        field_id_country = Select(self.driver.find_element(By.ID, "field-id_country"))
        field_id_country.select_by_visible_text("Polska")
        sleep(sec)
        field_id_country = Select(self.driver.find_element(By.ID, "field-id_state"))
        field_id_country.select_by_index(1)
        sleep(sec)
        self.driver.find_element(By.ID, "field-postcode").send_keys(postcode)
        sleep(sec)
        try:
            self.driver.find_element(By.NAME, "confirm-addresses").click()
            sleep(sec)
        except NoSuchElementException:
            self.driver.find_element(By.XPATH, '//*[@id="checkout-addresses-step"]/div/div/form/footer/button').click()
            sleep(sec)

    def choose_delivery(self, sec):
        self.driver.find_element(By.ID, "delivery_option_2").click()
        sleep(sec)
        self.driver.find_element(By.XPATH, '//*[@id="js-delivery"]/button').click()
        sleep(sec)

    def choose_payment(self, sec):
        self.driver.find_element(By.ID, "payment-option-3").click()
        sleep(sec)
        self.driver.find_element(By.ID, "conditions_to_approve[terms-and-conditions]").click()
        sleep(sec)
        self.driver.find_element(By.XPATH, '//*[@id="payment-confirmation"]/div[1]/button').click()
        sleep(sec)

    def check_order_status(self, sec):
        self.driver.find_element(By.XPATH, '// *[ @ id = "_desktop_user_info"] / div / a[2]').click()
        sleep(sec)
        self.driver.find_element(By.ID, "history-link").click()
        sleep(sec)
        self.driver.find_element(By.XPATH, '//*[@id="content"]/table/tbody/tr/td[6]/a[1]').click()
        sleep(sec)



