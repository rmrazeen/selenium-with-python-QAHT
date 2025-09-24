from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# title check
title = driver.title
print(title)
assert title in driver.title
print("Title Matched")

# radio button

elem = driver.find_element(By.XPATH, "//input[@value='male']")

if not elem.is_selected():
    elem.click()
    print("Radio button is selected")
else:
    print("Radio button is not selected")


# checkbox
checkbox = driver.find_element(By.XPATH, "//label[@for='sunday']")
# checkbox.click() enable and disable
if not checkbox.is_selected():
    checkbox.click()
    print("Checkbox is selected")
else:
    print("Checkbox is not selected")

#multiple checkbox using loop
day = ["sunday", "monday", "tuesday", "wednesday", "thursday"]  # Fixed spelling and capitalization

for d in day:
    checkbox = driver.find_element(By.XPATH, f"//input[@id='{d}']")
    if not checkbox.is_selected():  
        checkbox.click()
        print(f"{d} checkbox is selected")
    else:
        print(f"{d} checkbox is not selected")
#sunday checkbox is selected on previouse code so it will print not selected

#button

startButton = driver.find_element(By.XPATH, "//button[@name='start']")
startButton.click()
assert "STOP" in startButton.text, "assert error"
print("start is clicked")


#basic hover
hover_element = driver.find_element(By.XPATH, "//button[@class='dropbtn']")
ActionChains(driver).move_to_element(hover_element).perform()
dropbtn = driver.find_element(By.XPATH, "//a[contains(text(), 'Laptops')]")
dropbtn.click()
print("hover is done & clicked")
time.sleep(2)

#file upload
file_input = driver.find_element(By.XPATH, "//input[@id='singleFileInput']")
# Upload the file by sending the full path
file_input.send_keys(r"F:\selenium_guide.pdf")  # Use raw string to avoid escape issues \s or \n
# Click the upload button
upload_button = driver.find_element(By.XPATH, "//button[contains(text(),'Upload Single File')]")
upload_button.click()
upload_status = driver.find_element(By.ID, "singleFileStatus")
# Verify upload success
assert "Single file selected" in upload_status.text, "File upload verification failed"
print("File is uploaded")

# alert 
alert_button = driver.find_element(By.XPATH, "//button[@id='confirmBtn']")
alert_button.click()
# Switch to the alert
alert = driver.switch_to.alert
alert.text
print(alert.text)
alert.dismiss() # accept() to accept the alert, dismiss() to cancel it
print("alert is dismissed")

# prompt alert
alert_prompt = driver.find_element(By.XPATH, "//button[@id='promptBtn']")
alert_prompt.click()
alert = driver.switch_to.alert
print(alert.text)
alert.send_keys("Jhon")
alert.accept()
status = driver.find_element(By.XPATH, "//p[@id='demo']")
print(status.text)



try:
    
    # Wait for elements to be present
    wait = WebDriverWait(driver, 10)
    
    # Find the "Copy Text" button
    target = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Copy Text']")))
    
    # Create an ActionChains object
    actions = ActionChains(driver)
    
    # Perform double-click on the Copy Text button
    actions.double_click(target).perform()
    
    # Wait a moment for the copy operation to complete
    import time
    time.sleep(1)
    
    # Find the target field (field2) - removed the # symbol as it's not needed for ID selector
    copy_field = wait.until(EC.presence_of_element_located((By.ID, "field2")))
    
    # Get the text from both elements
    copied_text = copy_field.get_attribute("value")  # Use get_attribute for input field values
    button_text = target.text
    
    print(f"Copied text: '{copied_text}'")
    print(f"Button text: '{button_text}'")
    
    # The assertion should compare the copied text with the source text
    # The button text is "Copy Text", but what gets copied is likely from field1
    source_field = driver.find_element(By.ID, "field1")
    source_text = source_field.get_attribute("value")
    
    print(f"Source text: '{source_text}'")
    
    # Correct assertion - compare source text with copied text
    assert copied_text == source_text, f"Text not matched. Expected: '{source_text}', Got: '{copied_text}'"
    print("Text matched successfully!")
    
except Exception as e:
    print(f"Test failed with error: {e}")
    
finally:
    # Close the browser
    driver.quit()

