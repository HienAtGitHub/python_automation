# -*- coding: utf-8 -*-
"""

@author: Hien Dang

Desc: This program is to get to external website and scrap the desired files on a monthly basis using SELENIUM

"""
from selenium import webdriver
import time

browser = webdriver.Chrome("C:\\Downloads\\chromedriver_win32\\chromedriver")

browser.get("https://external_website.com")
time.sleep(10)
Products_elem = browser.find_element_by_link_text("Products")
Products_elem.click()
time.sleep(2)
Reporting_elem = browser.find_element_by_link_text("Reporting")
Reporting_elem.click()
time.sleep(2)
report_elem = browser.find_element_by_link_text("Reports")
report_elem.click()
