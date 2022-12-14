from time import sleep

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By


class Product:
    def __init__(self, driver, category, sub, name):
        self.driver = driver
        self.category = category
        self.sub = sub
        self.name = name

    def add_to_cart(self, num, sec):
        # wybranie kategorii
        cat = self.driver.find_element(By.LINK_TEXT, self.category)
        chain = ActionChains(self.driver)
        chain.move_to_element(cat).perform()
        sleep(sec)
        # wybranie podkategorii
        self.driver.find_element(By.LINK_TEXT, self.sub).click()
        sleep(sec)
        # wybranie produktu
        self.driver.find_element(By.LINK_TEXT, self.name).click()
        sleep(sec)
        # uzupelnienie ilosci
        quantity = self.driver.find_element(By.ID, "quantity_wanted")
        quantity.send_keys(Keys.SHIFT, Keys.END, Keys.BACK_SPACE)
        quantity.send_keys(num)
        sleep(sec)

        # dodanie do koszyka
        self.driver.find_element(By.CLASS_NAME, "add-to-cart").click()
        sleep(sec*5)
        # klikniecie kontynuuowania zakupow
        self.driver.find_element(By.XPATH,
                                 '//*[@id="blockcart-modal"]/div/div/div[2]/div/div[2]/div/div/button').click()
        sleep(sec)
