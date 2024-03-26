import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SwagLabsLoginTester:
    def __init__(self):
        self.driver = webdriver.Firefox()
    
    def test_login(self):
        self.driver.get("https://www.saucedemo.com/v1/")
        self.driver.maximize_window()
        
        user_credentials = pd.read_excel("User credentials.xlsx")
        login_results = pd.DataFrame(columns=["User ID", "Login Message"])
        
        for index, row in user_credentials.iterrows():
            user_id = row["User ID"]
            user = row["User Name"]
            password = row["Password"]
            
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="user-name"]')))
            username_field = self.driver.find_element(By.XPATH, '//*[@id="user-name"]')
            password_field = self.driver.find_element(By.XPATH, '//*[@id="password"]')
            login_button = self.driver.find_element(By.XPATH, '//*[@id="login-button"]')
            
            username_field.clear()
            password_field.clear()
            username_field.send_keys(user)
            password_field.send_keys(password)
            login_button.click()
            
            time.sleep(5)
            self.driver.back()
            
            ERROR_MESSAGE = ""
            try:
                ERROR_MESSAGE = self.driver.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/h3').text
            except:
                pass
            
            new_data = {"User ID": [user_id], "Login Message": [ERROR_MESSAGE]}
            new_df = pd.DataFrame(new_data)
            login_results = pd.concat([login_results, new_df])
        
        self.driver.quit()
        
        df_login_results = pd.DataFrame(login_results)
        
        # Append the login results to the "Login" sheet in the existing Excel file
        with pd.ExcelWriter("User credentials.xlsx", mode="a", engine="openpyxl") as writer:
            df_login_results.to_excel(writer, sheet_name="Login", index=False)