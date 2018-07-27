import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from helper_functions import finders

driver = webdriver.Chrome()
driver.get("http://www.blazedemo.com")
assert "Welcome" in driver.page_source
print ("welcome line is present")
driver.finders.xpath("/html/body/div[3]/form/select[1]/option[6]").click()
print ("selected Mexico City as fromPort")
# driver.find_element_by_xpath("/html/body/div[3]/form/select[2]/option[7]").click()
# print ("selected Cairo as toPort")
# driver.find_element_by_xpath("/html/body/div[3]/form/div/input").click()
# print ("clicked find flights")
# driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr[3]/td[1]/input").click()
# print ("clicked Flight 9696")
# driver.find_element_by_xpath("//*[@id=\"inputName\"]").send_keys("captain herp-a-derp")
# driver.find_element_by_xpath("//*[@id=\"address\"]").send_keys("123 tall ship st.")
# driver.find_element_by_xpath("//*[@id=\"city\"]").send_keys("pirate cove")
# driver.find_element_by_xpath("//*[@id=\"state\"]").send_keys("CA")
# driver.find_element_by_xpath("//*[@id=\"zipCode\"]").send_keys("95050")
# driver.find_element_by_xpath("//*[@id=\"creditCardNumber\"]").send_keys("1234123412341234")
# driver.find_element_by_xpath("//*[@id=\"creditCardYear\"]").send_keys("2020")
# driver.find_element_by_xpath("//*[@id=\"nameOnCard\"]").send_keys("captain herp-a-derp")
# print ("filled out form")
# driver.find_element_by_xpath("/html/body/div[2]/form/div[11]/div/input").click()
# assert "Thank you for your purchase today!" in driver.page_source
# print ("thank you line is present")
# print ("HACK THE MOTHERFUCKING PLANET!!!!!")
# driver.close()