from time import sleep
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from product import Product
from user import User

PATH = r"C:\Program Files\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("http://127.0.0.1:80")
driver.maximize_window()
driver.implicitly_wait(10)

user = User(driver, "Pan", "Adam", "Adamski", "adam14@gmail.com", "adaamo12.", "2001-01-01")

products = []
products.append(Product(driver, "BUTY", "SNEAKERSY", "OZWEEGO Shoes"))
products.append(Product(driver, "BUTY", "SNEAKERSY", "ZX 22 BOOST Shoes"))
products.append(Product(driver, "BUTY", "SNEAKERSY", "Superstar Shoes"))
products.append(Product(driver, "BUTY", "SNEAKERSY", "Stan Smith Shoes"))
products.append(Product(driver, "BUTY", "SNEAKERSY", "Gazelle Indoor Shoes"))
products.append(Product(driver, "AKCESORIA", "TORBY I PLECAKI", "Adicolor Backpack"))
products.append(Product(driver, "AKCESORIA", "TORBY I PLECAKI", "Power VI Backpack"))
products.append(Product(driver, "AKCESORIA", "TORBY I PLECAKI", "4ATHLTS Camper Backpack"))
products.append(Product(driver, "AKCESORIA", "TORBY I PLECAKI", "4ATHLTS ID Gear Up Backpack"))
products.append(Product(driver, "AKCESORIA", "TORBY I PLECAKI", "Adicolor Classic Waist Bag"))

sec = 1
for product in products:
    product.add_to_cart(random.randint(1, 3), sec)
    sec = 0

sec = 1
driver.find_element(By.XPATH, '//*[@id="_desktop_cart"]/div/div/a/span[1]').click()
sleep(sec)
driver.find_element(By.XPATH, '//*[@id="main"]/div/div[1]/div/div[2]/ul/li/div/div[3]/div/div[3]/div/a/i').click()
sleep(sec)
driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[1]/div[2]/div/a').click()
sleep(sec)

user.fill_register_form(sec)
user.fill_address_form(sec, "Kosciuszki", "11-111", "Gdansk")
user.choose_delivery(sec)
user.choose_payment(sec)
user.check_order_status(sec)
sleep(5)
