from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import os
import time

fire_path=r"to\path\Chromedriver.exe"
driver=webdriver.Chrome(fire_path)
driver.get("<URL>") #url you want to  fill

for x in range (0,50):
	time.sleep(2)
	driver.find_element_by_xpath("""//*[@title="Select position"]""").click() #find the title below click
	driver.find_element_by_xpath("""//*[contains(text(),'ML Developer')]""").click() #select from dropdown  

	name=driver.find_element_by_xpath("""//*[@placeholder='First name']""")
	name.send_keys("some_Name")
	sname=driver.find_element_by_xpath("""//*[@placeholder='Last name']""")
	sname.send_keys("Some_Name")
	email=driver.find_element_by_xpath("""//*[@placeholder='Email address']""")
	email.send_keys("<SOME EMAIL>")
	phone=driver.find_element_by_xpath("""//*[@placeholder='Mobile no.']""")
	phone.send_keys("<PHONE NUMBER>")
	curr=driver.find_element_by_xpath("""//*[@placeholder='Current Company / Organisation']""")
	curr.send_keys("Company_Name")

	driver.find_element_by_xpath("""//*[@title="Your Experience"]""").click()
	driver.find_element_by_xpath("""//*[contains(text(),'choose option from drop box')]""").click()

	git=driver.find_element_by_xpath("""//*[@placeholder='Links to you online work/portfolio.']""")  
	git.send_keys("link to your profile mention ")

	git=driver.find_element_by_xpath("""//*[@placeholder='text written in textbox']""")  
	git.send_keys("name of college")

# driver.find_element_by_xpath("""//*[@id="decimal_opening"]/div/div[2]/div[2]/div/form/div/div[8]/div/div/input""").click()
# driver.find_element_by_css_selector('input[type="file"]').send_keys("to\path\find\resume.pdf")

	driver.find_element_by_xpath("""//*[@id="decimal_opening"]/div/div[2]/div[2]/div/form/div/div[8]/div/div/input""").send_keys("to\path\find\resume.pdf")
	
