from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

for_you_url = "https://www.tiktok.com/foryou?lang=en"
opts = Options()
#This creates a user directory in the folder of your choice for chrome to store history and cookies
#The perk here is once you've logged in once, the website seems to remember you if you don't logout
opts.add_argument("user-data-dir=/Users/ademolabello/PycharmProjects/pythonProject/user_data")
# This seems to be the feature that stops TikTok from detecting you. Worked in R as well
opts.add_argument('--disable-blink-features=AutomationControlled')
#opts.add_argument("start-maximized")
#opts.add_experimental_option("excludeSwitches", ['enable_automation'])
#opts.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=opts,
                          executable_path="/Users/ademolabello/PycharmProjects/pythonProject/chromedriver")

# Login details
email = "dmcgirt565@gmail.com"
password = "DirtyBastard565."

# Xpaths
email_field = '/html/body/div[1]/div/div[1]/form/div[2]/div/input'
pw_field = '/html/body/div[1]/div/div[1]/form/div[3]/div/input'
login_button = '/html/body/div[1]/div/div[1]/form/button'

# Drive website
driver.get("https://www.tiktok.com/login/phone-or-email/email")
driver.find_element_by_xpath(email_field).send_keys(email)

pw_element = driver.find_element_by_xpath(pw_field)
pw_element.send_keys(password)

# For some reason TikTok loads a blank page when you login like this
# Current work around is to do it manually
#pw_element.send_keys(Keys.ENTER)
#driver.find_element_by_xpath(login_button).click()

# Move around
# Get access to the page
cntrl = driver.find_element_by_css_selector('body')
# Move to next video
cntrl.send_keys(Keys.ARROW_DOWN)
# Mute or unmute the video
cntrl.send_keys("m")
# Each video is contained in a 'span'. So you can increment the value in a loop
video1 = driver.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div/div[1]/span[1]')
print(video1.text)

# Example output from .text
# 'lukeleprevostofficial
# Luke Le Prevost
# Hi 👋🏼 #fyp #foryou #foryoupage #lukeleprevost
# Follow
# Seaside_demo by SEB - SEB
# 28.4K
# 27.6K
# 18'

# To do
# Increment the span xpath by 1 then linger on video for however long
# then collect data

# Close driver
# driver.close()