#-*- coding : utf-8-*-
# coding:unicode_escape
from selenium import webdriver
import time
import os
import pytesseract
from PIL import Image
import re

os.chdir(r'D:\\learnPython\\venv\\Lib\\site-packages\\pytesseract')

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get('http://gsjcag.add177.com/Login')
print("1")

driver.save_screenshot('d:/Python/aa.png')
element = driver.find_element_by_xpath("//form[@id = 'form1']/ul/li[3]/img")
location = element.location
size = element.size
# print(size)
# print(location)
# zuobiao = (1020,505,1072,525)
zuobiao = (int(location['x']), int(location['y']), int(location['x']+size['width']), int(location['y']+size['height']))

print(zuobiao)

i = Image.open('d:/Python/aa.png')
b = i.crop(zuobiao)
b.save('d:/Python/bb.jpg', 'png')
print('01')
c = Image.open('d:/Python/bb.jpg')
print('11')
text = pytesseract.image_to_string(c)
print('12')
print(text)
print('22')
# text1 = re.sub('\D','',text)
# print(text1)
driver.quit()
