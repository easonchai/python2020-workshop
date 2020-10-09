import time
from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager

# Install Driver Automatically
driver =webdriver.Chrome(ChromeDriverManager().install())

# Stores the elearn URL
search_url="https://elearn.sunway.edu.my/" 

# Opens up Chrome and connects to the search_url
driver.get(search_url)

# Wait a little while before clicking the "OK" button just incase if it haven't load
time.sleep(1)
driver.find_element_by_id("agree_button").click()

print("clicked ok")
time.sleep(3)
print('wait over')
driver.find_element_by_xpath("//button[text()='Sunway ID']").click()



print("clicked sunway")
