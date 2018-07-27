import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import helper_functions

class BlazeDemoTest(unittest.TestCase):

	find = helper_functions.finder
	verify = helper_functions.verify_url

	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.get("http://www.blazedemo.com")
		self.driver.implicitly_wait(3)
		# self.driver.maximize_window()

	def verifyWelcome(self):
		assert "Welcome" in self.driver.page_source

	def findFlight(self):
		self.find("xpath","/html/body/div[3]/form/select[1]/option[6]").click()
		self.find("xpath","/html/body/div[3]/form/select[2]/option[7]").click()
		self.find("xpath","/html/body/div[3]/form/div/input").click()
		sleep(3)
		actual_url = self.driver.current_url
		self.verify(actual_url, expected_url="http://www.blazedemo.com/reserve.php")

	def chooseFlight(self):
		self.flight = self.find("xpath","/html/body/div[2]/table/tbody/tr[3]/td[1]/input").click()
		sleep(3)
		actual_url = self.driver.current_url
		self.verify(actual_url, expected_url="http://www.blazedemo.com/purchase.php")

	def purchaseFlight(self):
		self.find("xpath","//*[@id=\"inputName\"]").send_keys("captain herp-a-derp")
		self.find("xpath","//*[@id=\"address\"]").send_keys("123 tall ship st.")
		self.find("xpath","//*[@id=\"city\"]").send_keys("pirate cove")
		self.find("xpath","//*[@id=\"state\"]").send_keys("CA")
		self.find("xpath","//*[@id=\"zipCode\"]").send_keys("95050")
		self.find("xpath","//*[@id=\"creditCardNumber\"]").send_keys("1234123412341234")
		self.find("xpath","//*[@id=\"creditCardYear\"]").send_keys("2020")
		self.find("xpath","//*[@id=\"nameOnCard\"]").send_keys("captain herp-a-derp")
		self.find("xpath","/html/body/div[2]/form/div[11]/div/input").click()
		sleep(3)
		actual_url = self.driver.current_url
		self.verify(actual_url, expected_url="http://www.blazedemo.com/confirmation.php")

	def confirmPurchase(self):
		assert "Thank you for your purchase today!" in self.driver.page_source

	def test_method(self):
		print "\n\n--- starting ---"
		self.findFlight()
		print "flight found"
		self.chooseFlight()
		print "flight chosen"
		self.purchaseFlight()
		print "flight purchased"
		self.confirmPurchase()
		print "flight confirmed"

	def tearDown(self):
		self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)

