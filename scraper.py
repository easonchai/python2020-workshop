import time
from datetime import date
from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

def run_scraper(username, password):
    global driver

    # Install Driver Automatically
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()

    # Stores the elearn URL
    search_url = "https://elearn.sunway.edu.my/" 

    # Opens up Chrome and connects to the search_url
    driver.get(search_url)

    # Wait a little while before clicking the "OK" button just incase if it haven't load
    time.sleep(1)
    driver.find_element_by_id("agree_button").click()

    # Selects the Sunway ID button
    time.sleep(1)
    driver.find_element_by_xpath("//button[text()='Sunway ID']").click()

    # Uses the previously loaded username & password and enters it into the fields
    time.sleep(1)
    driver.find_element_by_id("userNameInput").send_keys(username)
    
    time.sleep(1)
    driver.find_element_by_id("passwordInput").send_keys(password)

    # Click the Sign In button
    time.sleep(1)
    driver.find_element_by_id("submitButton").click()

def get_announcements():
    todays_info = driver.find_element_by_class_name("js-todayStreamEntries")
    announcement_feed = todays_info.find_element_by_tag_name("ul")
    print(announcement_feed)

    announcement_file = open('announcements.txt', 'w')
    announcement_file.write('🔔 Announcements for the day! 🔊\n')
    today = date.today().strftime("%B %d, %Y")
    announcement_file.write(today + "\n\n")
    announcement_file.close()


def open_subjects(subject_list):
    # The first step is to see how many subjects we have. Once we know that, we open 1 extra tab for each subject, leaving the first tab
    # for the announcements

    for subject in subject_list:
        time.sleep(3)
        actions = ActionChains(driver)
        courses_button = driver.find_element_by_xpath('//span[text()="Courses"]')
        actions.key_down(Keys.CONTROL).click(courses_button).key_up(Keys.CONTROL).perform()
        driver.switch_to.window(driver.window_handles[-1])
        
    for tab in range(len(subject_list)):
        # Remember! Tab 0 is the Activity Stream!
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[tab+1])
        driver.find_element_by_xpath('//span[contains(text(), "' + subject_list[tab] + '")]').click()
        