import time
from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager

def run_scraper(username, password):
    # Install Driver Automatically
    driver =webdriver.Chrome(ChromeDriverManager().install())

    # Stores the elearn URL
    search_url="https://elearn.sunway.edu.my/" 

    # Opens up Chrome and connects to the search_url
    driver.get(search_url)

    # Wait a little while before clicking the "OK" button just incase if it haven't load
    time.sleep(1)
    driver.find_element_by_id("agree_button").click()

    # Selects the Sunway ID button
    time.sleep(1)
    driver.find_element_by_xpath("//button[text()='Sunway ID']").click()

    # Uses the previously loaded username & password and enters it into the fields
    driver.find_element_by_id("userNameInput").send_keys(username)
    driver.find_element_by_id("passwordArea").send_keys(password)

    # Click the Sign In button
    driver.find_element_by_id("submitButton").click()
