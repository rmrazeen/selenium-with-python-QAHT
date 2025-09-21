from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
# Launch Chrome (Selenium will auto-manage ChromeDriver if v4.6+)
driver = webdriver.Chrome()
driver.maximize_window()
print(driver.title)
driver.get("https://www.saucedemo.com/")
# Find by ID --------------------------------------------------
# user_name = driver.find_element(By.ID, "user-name")
# user_name.send_keys("standard_user")
# password = driver.find_element(By.ID, "password")
# password.send_keys("secret_sauce")
# login_button = driver.find_element(By.ID, "login-button")
# login_button.click()

# Find by XPATH --------------------------------------------------

# driver.find_element(By.XPATH, "//input[@data-test='username']").send_keys("standard_user") #attribute based xpath
driver.find_element(By.XPATH, "//input[starts-with(@id,'user')]").send_keys("standard_user") #starts-with() function xpath
driver.find_element(By.XPATH, "//input[contains(@placeholder,'Password')]").send_keys("secret_sauce") #contains() function xpath
driver.find_element(By.XPATH, "//input[@type='submit' and @value='Login']").click() #multiple attribute xpath
driver.find_element(By.XPATH, "//a[@id='item_4_title_link']/div[text()='Sauce Labs Backpack']").click() #text() function xpath
time.sleep(2)

# Find with Axes --------------------------------------------------


# driver.find_element(By.XPATH, "//div[@id='login_button_container']//input[@type='submit' and @id='login-button']") #double slash
# driver.find_element(By.XPATH, "//input[@id='login-button']/parent::div") #parent axis
# driver.find_element(By.XPATH, "//div[@class='login-box']/child::form/child::input[@id='login-button']") #child axis
# driver.find_element(By.XPATH, "//div[@class='login-box']/descendant::input[@id='login-button']") #`descendant axis`
# driver.find_element(By.XPATH, "//input[@id='login-button']/ancestor::div[@id='root']") # ancestor axis
# driver.find_element(By.XPATH, "//input[@id='login-button']/ancestor::div[@id='login_button_container']/descendant::div[@class='error-message-container']") # sibling axis


driver.quit()
