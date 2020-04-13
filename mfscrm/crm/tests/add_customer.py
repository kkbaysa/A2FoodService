import csv
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# def readNames(FILENAME):
#     nameListReturn = []
#     with open(FILENAME, "r") as file:
#         nameList = csv.reader(file)
#         for name in nameList:
#             nameListReturn.append(name)
#
#     return nameListReturn


class login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='/Users/kaitlynbaysa/Desktop/ISQA3900/Assignment3EC/chromedriver')


    def test_customer(self):
        FILENAME = "test.csv".replace("\t", "")

        # login
        userName = "kbaysa88"
        password = "test88test"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://kbaysa.pythonanywhere.com/")
        driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[2]/li/a").click()
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(userName)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(password)
        elem.send_keys(Keys.RETURN)

        with open(FILENAME, "r") as file:
            nameList = csv.reader(file)
            # click view details on customer
            driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div/div/div/div[1]/div/div/p[2]/a").click()
            for name in nameList:
                # add a customer
                driver.find_element_by_xpath("/html/body/div/div/div/di/div/a/span").click()
                elem = driver.find_element_by_id("id_cust_name")
                elem.send_keys(name[0])
                elem = driver.find_element_by_id("id_organization")
                elem.send_keys(name[1])
                elem = driver.find_element_by_id("id_role")
                elem.send_keys(name[2])
                elem = driver.find_element_by_id("id_bldgroom")
                elem.send_keys(name[3])
                elem = driver.find_element_by_id("id_account_number")
                elem.send_keys(name[4])
                elem = driver.find_element_by_id("id_address")
                elem.send_keys(name[5])
                elem = driver.find_element_by_id("id_city")
                elem.send_keys(name[6])
                elem = driver.find_element_by_id("id_state")
                elem.send_keys(name[7])
                elem = driver.find_element_by_id("id_zipcode")
                elem.send_keys(name[8])
                elem = driver.find_element_by_id("id_email")
                elem.send_keys(name[9])
                elem = driver.find_element_by_id("id_phone_number")
                elem.send_keys(name[10])
                time.sleep(5)
                elem.send_keys(Keys.RETURN)
                driver.get("http://kbaysa.pythonanywhere.com/customer_list")
        time.sleep(5)


    def tearDown(self):
        self.driver.close()




if __name__ == "__main__":
    unittest.main()
