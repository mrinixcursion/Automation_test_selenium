import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def check_status_code(url):
    try:
        response = requests.get(url)
        status_code = response.status_code

        if status_code == 200:
            print("success")

        else:
            print("failed")

    except requests.RequestException as e:
        print(f"no result: {e}")

def check_elem(url):
    try:
        # wait for the elements to be present after succesful login 
        assign_job_elements = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "heading_mainContainer__o1Cu0"))
        )
        # Check the text content of the 'Assign Jobs' element
        if assign_job_elements.text == "Assign Jobs":
            print("Succesfully Logged in and Assign Job elements found")

        else:
         print("Logged in but no elements found")

    except Exception as e :
        print(f"no result: {e}")

driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\\chromedriver.exe")
driver.get("https://cvcdev.adcuratio.net/login") #provide your website url

driver.find_element(By.ID, "email").send_keys("*********") #provide email
driver.find_element(By.ID, "password").send_keys("*******") #provide password
driver.find_element(By.CSS_SELECTOR, "#root > section > main > div > div.ant-col.ant-col-xs-16.ant-col-xs-offset-0.ant-col-md-12.ant-col-lg-8.ant-col-lg-offset-0.ant-col-xl-6.ant-col-xxl-6.css-diro6f > form > div:nth-child(4) > div > div > div > div > div > button" ).click()

try:
        check_elem("https://cvcdev.adcuratio.net/supervisor/assign-jobs")
        # print("Found")

        driver.get("https://cvcdev.adcuratio.net/supervisor/assign-jobs")
        print("Navigated to Assign Jobs page")

        driver.get("https://cvcdev.adcuratio.net/supervisor/view-scheduling")
        print("Navigated to Scheduling page")

        driver.get("https://cvcdev.adcuratio.net/supervisor/timesheet-history")
        print("Navigated to the Timesheet History page")

        driver.get("https://cvcdev.adcuratio.net/supervisor/review-timesheet")
        print("Navigated to the Review Timesheet page")

        check_status_code("https://cvcdev.adcuratio.net/supervisor/assign-jobs")
        check_status_code("https://cvcdev.adcuratio.net/supervisor/view-scheduling")
        check_status_code("https://cvcdev.adcuratio.net/supervisor/timesheet-history")
        check_status_code("https://cvcdev.adcuratio.net/supervisor/review-timesheet")



except Exception as e:
    print("Logged in failed")

    
