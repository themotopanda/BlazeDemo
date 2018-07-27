import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

class BlazeDemoTest(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.get("http://www.blazedemo.com")
		self.driver.implicitly_wait(3)
		# self.driver.maximize_window()

	def verifyWelcome(self):
		assert "Welcome" in self.driver.page_source

	def verify_url(self, actual_url, expected_url):
		unittest.TestCase.assertEquals(self, actual_url, expected_url, "Actual url:" + actual_url + "is not equal to expected url: " + expected_url)

	def findFlight(self):
		self.fromPort = self.driver.find_element_by_xpath("/html/body/div[3]/form/select[1]/option[6]").click()
		self.toPort = self.driver.find_element_by_xpath("/html/body/div[3]/form/select[2]/option[7]").click()
		self.portsClick = self.driver.find_element_by_xpath("/html/body/div[3]/form/div/input").click()
		sleep(3)
		actual_url = self.driver.current_url
		self.verify_url(actual_url, expected_url="http://www.blazedemo.com/reserve.php")

	def chooseFlight(self):
		self.flight = self.driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr[3]/td[1]/input").click()
		sleep(3)
		actual_url = self.driver.current_url
		self.verify_url(actual_url, expected_url="http://www.blazedemo.com/purchase.php")

	def purchaseFlight(self):
		self.driver.find_element_by_xpath("//*[@id=\"inputName\"]").send_keys("captain herp-a-derp")
		self.driver.find_element_by_xpath("//*[@id=\"address\"]").send_keys("123 tall ship st.")
		self.driver.find_element_by_xpath("//*[@id=\"city\"]").send_keys("pirate cove")
		self.driver.find_element_by_xpath("//*[@id=\"state\"]").send_keys("CA")
		self.driver.find_element_by_xpath("//*[@id=\"zipCode\"]").send_keys("95050")
		self.driver.find_element_by_xpath("//*[@id=\"creditCardNumber\"]").send_keys("1234123412341234")
		self.driver.find_element_by_xpath("//*[@id=\"creditCardYear\"]").send_keys("2020")
		self.driver.find_element_by_xpath("//*[@id=\"nameOnCard\"]").send_keys("captain herp-a-derp")
		self.driver.find_element_by_xpath("/html/body/div[2]/form/div[11]/div/input").click()
		sleep(3)
		actual_url = self.driver.current_url
		self.verify_url(actual_url, expected_url="http://www.blazedemo.com/confirmation.php")

	def confirmPurchase(self):
		assert "Thank you for your purchase today!" in self.driver.page_source

	def test_method(self):
		print "--- starting ---"
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

