from selenium import webdriver as w
import pyautogui as py

# path for chrome web driver
driver = w.Chrome('D:\Web Drivers\Chrome\chromedriver.exe')

driver.get("https://www.livechat.com/typing-speed-test/#/")
while True:
    text = driver.find_element_by_xpath(
        "/html/body/div[2]/div[1]/div/div[2]/div[1]/div/span/div[2]/span/div/div[2]/div[2]/span[1]").text + ' '
    text += driver.find_element_by_xpath(
        "/html/body/div[2]/div[1]/div/div[2]/div[1]/div/span/div[2]/span/div/div[2]/div[2]/span[2]").text + ' '
    text += driver.find_element_by_xpath(
        "/html/body/div[2]/div[1]/div/div[2]/div[1]/div/span/div[2]/span/div/div[2]/div[2]/span[3]").text + ' '
    text += driver.find_element_by_xpath(
        "/html/body/div[2]/div[1]/div/div[2]/div[1]/div/span/div[2]/span/div/div[2]/div[2]/span[4]").text + ' '
    text += driver.find_element_by_xpath(
        "/html/body/div[2]/div[1]/div/div[2]/div[1]/div/span/div[2]/span/div/div[2]/div[2]/span[5]").text + ' '
    text += driver.find_element_by_xpath(
        "/html/body/div[2]/div[1]/div/div[2]/div[1]/div/span/div[2]/span/div/div[2]/div[2]/span[6]").text + ' '
    text += driver.find_element_by_xpath(
        "/html/body/div[2]/div[1]/div/div[2]/div[1]/div/span/div[2]/span/div/div[2]/div[2]/span[7]").text + ' '
    text += driver.find_element_by_xpath(
        "/html/body/div[2]/div[1]/div/div[2]/div[1]/div/span/div[2]/span/div/div[2]/div[2]/span[8]").text + ' '
    py.typewrite(text)
