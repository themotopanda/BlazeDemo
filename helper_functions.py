import unittest
from selenium import webdriver

def finder(self, board = '', dart = ''):
	if board == "xpath":
		return self.driver.find_element_by_xpath(dart)
	elif board == "name":
		return self.driver.find_element_by_name(dart)
	elif board == "id":
		return self.driver.find_element_by_id(dart)
	elif board == "css":
		return self.driver.find_element_by_css_selector(dart)
	elif board == "tag":
		return self.driver.find_element_by_tag_name(dart)
	elif board == "link":
		return self.driver.find_element_by_link_text(dart)
	elif board == "class":
		return self.driver.find_element_by_class_name(dart)
	elif board == "partial":
		return self.driver.find_element_by_partial_link_text(dart)

def verify_url(self, actual_url, expected_url):
	return unittest.TestCase.assertEquals(self, actual_url, expected_url, "Actual url:" + actual_url + "is not equal to expected url: " + expected_url)