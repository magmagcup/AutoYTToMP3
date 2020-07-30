from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys


# Read file name
read = open("name/song_name.txt", "r", encoding='utf8')
song_name = read.read().splitlines()
read.close()

# Gathering yt link and write in to song_link
chromeDriverPath = "E:/MyPro/chrome_driver/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chromeDriverPath)
f_write = open("youtube_link/song_link.txt", "w")

singer = ""
FOLDER_NAME = ""

for song in song_name:
    if song[-1] == ";":
        FOLDER_NAME = song[:-1]
        continue
    if song[-1] == "}":
        singer = song[:-1]
        continue
    search_link = f"https://www.youtube.com/results?search_query={singer+' '+song}&sp=EgIYAQ%253D%253D"
    driver.get(search_link)
    element = driver.find_element_by_id("video-title")
    link = element.get_attribute('href')
    f_write.write(link + "\n")
    sleep(10)

driver.close()
f_write.close()

"""
Search from youtube (directly)

driver.get("https://www.youtube.com")
search_box = driver.find_element_by_name("search_query")
search_box.send_keys(song, Keys.ENTER)
"""