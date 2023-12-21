from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\\chromedriver.exe")
driver.get("***************") # provide your website to navigate

driver.find_element_by_id("email").send_keys("*******") #provide your email
driver.find_element_by_id("password").send_keys("******") #provide your password
driver.find_element_by_css_selector("#root > section > main > div > div.ant-col.ant-col-xs-16.ant-col-xs-offset-0.ant-col-md-12.ant-col-lg-8.ant-col-lg-offset-0.ant-col-xl-6.ant-col-xxl-6.css-diro6f > form > div:nth-child(4) > div > div > div > div > div > button").click()

try:
    # Wait for the 'Reports' element to be present after successful login
    reports_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "heading_mainContainer__o1Cu0"))
    )

    # Check the text content of the 'Reports' element
    if reports_element.text == "Reports":
        print("Logged in successfully. 'Reports' element found.")
        
        # Navigate to the Reports page
        driver.get("https://cvcdev.adcuratio.net/payroll/reports")
        print("Navigated to the Reports page.")

    else:
        print("Logged in but 'Reports' element text mismatch.")
except Exception as e:
    print(f"Failed to login or 'Reports' element not found: {e}")

