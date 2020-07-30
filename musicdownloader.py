from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from collectlink import FOLDER_NAME

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_settings.popups": 0,
        "download.default_directory": r"E:\MyPro\music\\",
         "directory_upgrade": True}
chrome_options.add_experimental_option("prefs", prefs)
chromeDriverPath = "E:/MyPro/chrome_driver/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chromeDriverPath, options=chrome_options)
action = ActionChains(driver)

f_read = open("youtube_link/song_link.txt", "r", encoding='utf8')
youtube_links = f_read.read().splitlines()
driver.implicitly_wait(20)

driver.get('https://ytmp3.cc/en13/')

for link in youtube_links:
    element = driver.find_element_by_id("input")
    element.send_keys(link, Keys.ENTER)
    link_with_tag = driver.find_element(By.XPATH, '//a[text()="Download"]')
    link_with_tag.send_keys(Keys.ENTER)
    driver.get('https://ytmp3.cc/en13/')
    sleep(10)

driver.close()

