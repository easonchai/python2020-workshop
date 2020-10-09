import time
from datetime import date
from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

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
    # time.sleep(1)

    # Instead of using sleep(), we can use WebDriverWait to ensure that we click when the element exists
    WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id("agree_button")).click()
    

    # Selects the Sunway ID button
    WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath("//button[text()='Sunway ID']")).click()

    # Uses the previously loaded username & password and enters it into the fields
    WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id("userNameInput")).send_keys(username)
    WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id("passwordInput")).send_keys(password)

    # Click the Sign In button
    WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id("submitButton")).click()

def get_announcements():
    today = date.today().strftime("%B %d, %Y")

    try:
        # Gets the annoucement data
        todays_info = WebDriverWait(driver, 5).until(lambda x: x.find_element_by_class_name("js-todayStreamEntries"))
        announcement_feed = todays_info.find_element_by_tag_name("ul")
        useful_data = announcement_feed.find_elements_by_tag_name("li")
        
        # Open a file to store announcements
        announcement_file = open('announcements.txt', 'w', encoding='utf-8')
        announcement_file.write('🔔 Announcements for the day! 🔊\n')
        announcement_file.write(today + "\n\n")

        for announcement in useful_data:
            announcement_file.write('✉️ ' + announcement.find_element_by_tag_name("a").text + '\n') # From who
            announcement_file.write('👉 ' + announcement.find_element_by_class_name("name").text + '\n\n') # Main title of annoucement
    except:
        announcement_file = open('announcements.txt', 'w', encoding='utf-8')
        announcement_file.write('🔔 No announcements for the day! 🔊\n')
        announcement_file.write(today + "\n\n")

    announcement_file.close()


def open_subjects(subject_list):
    # The first step is to see how many subjects we have. Once we know that, we open 1 extra tab for each subject, leaving the first tab
    # for the announcements

    # Open tab per subject
    for subject in subject_list:
        actions = ActionChains(driver)
        courses_button = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath('//span[text()="Courses"]'))
        actions.key_down(Keys.CONTROL).click(courses_button).key_up(Keys.CONTROL).perform()
        driver.switch_to.window(driver.window_handles[-1])
        
    # Find the actual subject based on the subject codes and click into it
    for tab in range(len(subject_list)):
        # Remember! Tab 0 is the Activity Stream!
        driver.switch_to.window(driver.window_handles[tab+1])
        WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath('//span[contains(text(), "' + subject_list[tab] + '")]')).click()

def warning():
    print("You shouldn't be running this file directly! Please run main.py!")     
    
if __name__ == "__main__":
    warning()
        