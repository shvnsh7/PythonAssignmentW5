"""Login using the "standard_user" and retrieve all the product related information for every listed product"""
"""importing"""
import time
import pandas as pd
from selenium import webdriver
#from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("https://www.saucedemo.com/v1/")
driver.maximize_window()

Username=driver.find_element(By.XPATH,'//input[@id="user-name"]')
Username.send_keys("standard_user")

Password=driver.find_element(By.XPATH,'//input[@id="password"]')
Password.send_keys("secret_sauce")

driver.implicitly_wait(3)

login_button=driver.find_element(By.XPATH,'//input[@id="login-button"]')
login_button.click()


# Get all the product elements
product_elements = driver.find_elements(By.XPATH, '//div[@class="inventory_item"]')

# Create a list to store the product details
product_details = []

# Iterate through each product element and retrieve the details
for product_element in product_elements:
    product_id = product_element.find_element(By.XPATH, './/div[@class="inventory_item_label"]/a').get_attribute(
        "id")
    product_name = product_element.find_element(By.XPATH, './/div[@class="inventory_item_label"]/a/div').text
    description = product_element.find_element(By.XPATH, './/div[@class="inventory_item_label"]/div').text
    price = product_element.find_element(By.XPATH, './/div[@class="pricebar"]/div').text

    product_info = {"Product ID": product_id, "Product Name": product_name, "Description": description, "Price": price}
    product_details.append(product_info)

# Close the browser
driver.quit()

# Open the existing Excel file and write the product details to a new sheet named "Product Details"
with pd.ExcelWriter("User credentials.xlsx", mode="a", engine="openpyxl") as writer:
    df_product_details = pd.DataFrame(product_details)
    df_product_details.to_excel(writer, sheet_name="Product Details", index=False)
