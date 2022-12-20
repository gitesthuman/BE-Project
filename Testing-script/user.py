from time import sleep

from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
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
    # uzupelnienie formularza rejestracji
    def fill_register_form(self, sec):
        # wybranie opcji pan lub pani
        if self.title == "Pan":
            self.driver.find_element(By.ID, "field-id_gender-1").click()
        else:
            self.driver.find_element(By.ID, "field-id_gender-2").click()
        sleep(sec)
        # wpisanie imienia
        self.driver.find_element(By.ID, "field-firstname").send_keys(self.firstname)
        sleep(sec)
        # wpisanie nazwiska
        self.driver.find_element(By.ID, "field-lastname").send_keys(self.lastname)
        sleep(sec)
        # wpisanie emaila
        self.driver.find_element(By.ID, "field-email").send_keys(self.email)
        sleep(sec)
        # wpisanie hasla
        self.driver.find_element(By.ID, "field-password").send_keys(self.password)
        sleep(sec)
        # wypelnienie daty urodzenia
        self.driver.find_element(By.ID, "field-birthday").send_keys(self.birthday)
        sleep(sec)
        # zaakceptowanie regulaminow
        self.driver.find_element(By.XPATH, '//*[@id="customer-form"]/div/div[8]/div[1]/span/label/input').click()
        sleep(sec)
        self.driver.find_element(By.XPATH, '//*[@id="customer-form"]/div/div[10]/div[1]/span/label/input').click()
        sleep(sec)
        # przejscie dalej
        self.driver.find_element(By.XPATH, '// *[ @ id = "customer-form"] / footer / button').click()
        sleep(sec)
        while True:
            try:
                # jezeli podalismy zajety email to go edytujemy i powtarzamy proces
                self.driver.find_element(By.XPATH, '//*[@id="customer-form"]/div/div[4]/div[1]/div/ul/li')
                split = self.email.split('@')
                split[0] += '1'
                self.email = split[0] + '@' + split[1]
                print(self.email)
                field_email = self.driver.find_element(By.ID, "field-email")
                field_email.send_keys(Keys.SHIFT, Keys.END, Keys.BACK_SPACE)
                field_email.send_keys(self.email)
                sleep(sec)
                self.driver.find_element(By.ID, "field-password").send_keys(self.password)
                sleep(sec)
                self.driver.find_element(By.XPATH, '// *[ @ id = "customer-form"] / footer / button').click()
                sleep(sec)
            except NoSuchElementException:
                break

    # uzupelnienie formularza adresu
    def fill_address_form(self, sec, address, postcode, city):
        # wpisanie adresu
        self.driver.find_element(By.ID, "field-address1").send_keys(address)
        sleep(sec)
        # wpisanie miasta
        self.driver.find_element(By.ID, "field-city").send_keys(city)
        sleep(sec)
        # wybranie kraju
        field_id_country = Select(self.driver.find_element(By.ID, "field-id_country"))
        field_id_country.select_by_visible_text("Polska")
        sleep(sec)
        # wpisanie kodu pocztowego
        self.driver.find_element(By.ID, "field-postcode").send_keys(postcode)
        sleep(sec)
        # przejscie dalej
        try:
            self.driver.find_element(By.NAME, "confirm-addresses").click()
            sleep(sec)
        except NoSuchElementException:
            self.driver.find_element(By.XPATH, '//*[@id="checkout-addresses-step"]/div/div/form/footer/button').click()
            sleep(sec)

    # wybranie dostawy
    def choose_delivery(self, sec):
        self.driver.find_element(By.ID, "delivery_option_2").click()
        sleep(sec)
        # przejscie dalej
        self.driver.find_element(By.XPATH, '//*[@id="js-delivery"]/button').click()
        sleep(sec)

    # wybranie opcji platnosci
    def choose_payment(self, sec):
        # wybranie platnosci przy odbiorze
        self.driver.find_element(By.ID, "payment-option-3").click()
        sleep(sec)
        # zgoda regulaminu
        self.driver.find_element(By.ID, "conditions_to_approve[terms-and-conditions]").click()
        sleep(sec)
        # przejscie dalej
        self.driver.find_element(By.XPATH, '//*[@id="payment-confirmation"]/div[1]/button').click()
        sleep(sec)

    # sprawdzenie statusu zamowienia
    def check_order_status(self, sec):
        # klikniecie profilu
        self.driver.find_element(By.XPATH, '// *[ @ id = "_desktop_user_info"] / div / a[2]').click()
        sleep(sec)
        # klikniecie historii zamowien
        self.driver.find_element(By.ID, "history-link").click()
        sleep(sec)
        # klikniecie szczegolow
        self.driver.find_element(By.XPATH, '//*[@id="content"]/table/tbody/tr/td[6]/a[1]').click()
        sleep(sec)


