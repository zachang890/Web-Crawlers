from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--window-size=1920x1080")

driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="./chromedriver")

url = "https://news.ycombinator.com/"
driver.get(url)
time.sleep(2)

#unicode_article = driver.find_element_by_id('24196025')
elements = driver.find_elements_by_css_selector(".storylink")
storyTitles = [el.text for el in elements]
scores = driver.find_elements_by_css_selector(".score")
storyScores = [score.text for score in scores]
links = [el.get_attribute("href") for el in elements]
print(storyTitles)
print(links)
print(storyScores)