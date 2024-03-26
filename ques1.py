import pandas as pd
"""It allows us to create, manipulate, and analyze data in tabular form."""
from selenium import webdriver
"""This line imports the webdriver module from the Selenium library.
Selenium is a tool used for automating web browsers"""

#from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
"""The By class provides various methods to locate elements on a web page using different strategies, 
such as by ID, by class name, by tag name, etc."""

driver = webdriver.Edge()
"""This line creates an instance of the Edge webdriver, which is used to automate the Microsoft Edge browser"""
driver.get("https://www.saucedemo.com/v1/")
driver.maximize_window()
element = driver.find_element(By.XPATH, '//*[@id="login_credentials"]')
text = element.text
#print("eferr",text)
usernames = text.split("\n")[1:]
 
#print("rererf",usernames)
 
pass_word = driver.find_element(By.XPATH,'//div[@class = "login_password"]')
text1 = pass_word.text
pass_words = text1.split("\n")[1:]
 
for p in pass_words:
    print(p)
data = {"User ID": range(1, len(usernames) + 1),
        "User Name": usernames,
        "Password": pass_words * len(usernames)}
 
df = pd.DataFrame(data)
 
df.to_excel("User credentials.xlsx", index=False)
#print(df)
 
driver.quit()
 