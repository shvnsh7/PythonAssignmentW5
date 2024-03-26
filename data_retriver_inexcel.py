import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

class SwagLabsDataGenerator:
    def __init__(self):
        self.driver = webdriver.Edge()
    
    def generate_user_credentials(self):
        self.driver.get("https://www.saucedemo.com/v1/")
        self.driver.maximize_window()
        
        usernames = self.get_usernames()
        passwords = self.get_passwords()
        
        data = {
            "User ID": range(1, len(usernames) + 1),
            "User Name": usernames,
            "Password": passwords * len(usernames)
        }
        
        df = pd.DataFrame(data)
        df.to_excel("User credentials.xlsx", index=False)
        
    def get_usernames(self):
        element = self.driver.find_element(By.XPATH, '//*[@id="login_credentials"]')
        text = element.text
        usernames = text.split("\n")[1:]
        return usernames
    
    def get_passwords(self):
        pass_word = self.driver.find_element(By.XPATH, '//div[@class="login_password"]')
        text1 = pass_word.text
        pass_words = text1.split("\n")[1:]
        return pass_words
    
    def quit_driver(self):
        self.driver.quit()


# Usage:
data_generator = SwagLabsDataGenerator()
data_generator.generate_user_credentials()
data_generator.quit_driver()