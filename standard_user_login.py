import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SwagLabsProductDetails:
    def __init__(self):
        self.driver = webdriver.Firefox()
    
    def login_and_retrieve_product_details(self):
        self.driver.get("https://www.saucedemo.com/v1/")
        self.driver.maximize_window()
        
        username = self.driver.find_element(By.XPATH, '//input[@id="user-name"]')
        username.send_keys("standard_user")
        
        password = self.driver.find_element(By.XPATH, '//input[@id="password"]')
        password.send_keys("secret_sauce")
        
        login_button = self.driver.find_element(By.XPATH, '//input[@id="login-button"]')
        login_button.click()
        
        time.sleep(3)
        
        product_elements = self.driver.find_elements(By.XPATH, '//div[@class="inventory_item"]')
        product_details = []
        
        for product_element in product_elements:
            product_id = product_element.find_element(By.XPATH, './/div[@class="inventory_item_label"]/a').get_attribute(
                "id")
            product_name = product_element.find_element(By.XPATH, './/div[@class="inventory_item_label"]/a/div').text
            description = product_element.find_element(By.XPATH, './/div[@class="inventory_item_label"]/div').text
            price = product_element.find_element(By.XPATH, './/div[@class="pricebar"]/div').text
        
            product_info = {"Product ID": product_id, "Product Name": product_name, "Description": description, "Price": price}
            product_details.append(product_info)
        
        self.driver.quit()
        
        with pd.ExcelWriter("User credentials.xlsx", mode="a", engine="openpyxl") as writer:
            df_product_details = pd.DataFrame(product_details)
            df_product_details.to_excel(writer, sheet_name="Product Details", index=False)