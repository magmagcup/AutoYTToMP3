from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import pafy
import os

from createfolder import *

# Read file name
read = open("name/song_name.txt", "r", encoding='utf8')
song_name = read.read().splitlines()
read.close()

# Gathering yt link and write in to song_link
chromeDriverPath = "chrome_driver/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chromeDriverPath)

file_index = 0
FOLDER_NAME = song_name[file_index][:-1]
file_index += 1
singer = song_name[file_index][:-1]
file_index += 1
f_write = open("youtube_link/song_link.txt", "w")

while True:
    search_link = f"https://www.youtube.com/results?search_query={singer+' '+song_name[file_index]}"
    driver.get(search_link)
    video_elements = driver.find_elements_by_id("video-title")

    for video_element in video_elements:
        vid_link = video_element.get_attribute('href')
        vid = pafy.new(vid_link)
        vid_title_list = vid.title.split()
        vid_duration = vid.duration
        hour = int(vid_duration[:2])
        minute = int(vid_duration[3:-3])

        if hour > 0:
            continue
        if 5 > minute > 1 and song_name in vid_title_list:
            f_write.write(vid_link + "\n")
            break

    file_index += 1
    sleep(10)

    if file_index >= len(song_name):
        break
    if song_name[file_index][-1] == '}':
        f_write.close()
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_settings.popups": 0,
                 "download.default_directory": return_path(FOLDER_NAME),
                 "directory_upgrade": True}
        chrome_options.add_experimental_option("prefs", prefs)
        chromeDriverPath = "E:/MyPro/chrome_driver/chromedriver.exe"
        driver_yt_to_mp3 = webdriver.Chrome(executable_path=chromeDriverPath, options=chrome_options)

        f_read = open("youtube_link/song_link.txt", "r", encoding='utf8')
        youtube_links = f_read.read().splitlines()
        driver_yt_to_mp3.implicitly_wait(20)

        driver_yt_to_mp3.get('https://ytmp3.cc/en13/')

        for link in youtube_links:
            element = driver_yt_to_mp3.find_element_by_id("input")
            element.send_keys(link, Keys.ENTER)
            link_with_tag = driver_yt_to_mp3.find_element(By.XPATH, '//a[text()="Download"]')
            link_with_tag.send_keys(Keys.ENTER)
            driver_yt_to_mp3.get('https://ytmp3.cc/en13/')
            sleep(10)

        driver_yt_to_mp3.close()

        FOLDER_NAME = song_name[file_index][:-1]
        file_index += 1
        singer = song_name[file_index][:-1]
        file_index += 1
        f_write = open("youtube_link/song_link.txt", "w")

f_write.close()
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_settings.popups": 0,
         "download.default_directory": return_path(FOLDER_NAME),
         "directory_upgrade": True}
chrome_options.add_experimental_option("prefs", prefs)
driver_yt_to_mp3 = webdriver.Chrome(executable_path=chromeDriverPath, options=chrome_options)

f_read = open("youtube_link/song_link.txt", "r", encoding='utf8')
youtube_links = f_read.read().splitlines()
driver_yt_to_mp3.implicitly_wait(20)

driver_yt_to_mp3.get('https://ytmp3.cc/en13/')

for link in youtube_links:
    element = driver_yt_to_mp3.find_element_by_id("input")
    element.send_keys(link, Keys.ENTER)
    link_with_tag = driver_yt_to_mp3.find_element(By.XPATH, '//a[text()="Download"]')
    link_with_tag.send_keys(Keys.ENTER)
    driver_yt_to_mp3.get('https://ytmp3.cc/en13/')
    sleep(10)

driver_yt_to_mp3.close()
driver.close()

# for song in song_name:
#     if song[-1] == ";":
#         FOLDER_NAME = song[:-1]
#         continue
#     if song[-1] == "}":
#         singer = song[:-1]
#         continue
#     search_link = f"https://www.youtube.com/results?search_query={singer+' '+song}&sp=EgIYAQ%253D%253D"
#     driver.get(search_link)
#     element = driver.find_element_by_id("video-title")
#     link = element.get_attribute('href')
#     f_write.write(link + "\n")
#     sleep(10)
#
# driver.close()
# f_write.close()

"""
Search from youtube (directly)

driver.get("https://www.youtube.com")
search_box = driver.find_element_by_name("search_query")
search_box.send_keys(song, Keys.ENTER)
"""