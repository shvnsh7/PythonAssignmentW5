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
user_credential = pd.read_excel("User credentials.xlsx")
login_results = pd.DataFrame(columns=["User ID", "Login Message"])
for index, row in user_credential.iterrows():
    user_id = row["User ID"]
    user = row["User Name"]
    password = row["Password"]
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="user-name"]')))
    username_field = driver.find_element(By.XPATH,'//*[@id="user-name"]')
    #username_field.send_keys("Some  text")
    password_field = driver.find_element(By.XPATH,'//*[@id="password"]')
    #password_field.send_keys("12344556")
    login_button = driver.find_element(By.XPATH,'//*[@id="login-button"]')
    #login_button.click()
    username_field.clear()
    password_field.clear()
    username_field.send_keys(user)
    password_field.send_keys(password)
    login_button.click()
    time.sleep(5)
    driver.back()
    #time.sleep(4)
    ERROR_MESSAGE = ""
    try:
        ERROR_MESSAGE = driver.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/h3').text
    except:
        pass
    new_data = {"User ID": [user_id], "Login Message": [ERROR_MESSAGE]}
    new_df = pd.DataFrame(new_data)
    login_results = pd.concat([login_results, new_df])
driver.quit()
df_product_details = pd.DataFrame(login_results)
# Append the product details to the "Product Details" sheet in the existing Excel file
with pd.ExcelWriter("User credentials.xlsx", mode="a", engine="openpyxl") as writer:
    df_product_details.to_excel(writer, sheet_name="Login", index=False)