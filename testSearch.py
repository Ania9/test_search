__author__ = "Anna Zarecka"

import unittest
from selenium.webdriver.common.by import By

from glsdp import GLBaseTestCase
from glsdp import GLSupportUI
from glsdp import GLWait
from glsdp import GLHelper


class Search(GLBaseTestCase, GLSupportUI):

    driverType = GLHelper.CHROME
    driverPath = "C:\Python27\webdrivers\chromedriver.exe"
    searched = "Java Developer"

    def glAfterSetUp(self):
        GLWait.whilePageLoaderIsVisible(self.driver)

    def testSearch(self):

        # Click on the search icon in the upper right corner of the page
        element = self.driver.find_element_by_xpath('//*[@class="button extrabtn btn-primary"]')
        element.click()

        # Enter a search term into the search field, then press 'enter'
        element = self.driver.find_element_by_xpath('//*[@class="button extrabtn btn-primary"]')
        self.findElementAndPutText(self.driver, By.XPATH, '//*[@id="mod-search-searchword"]', self.searched)
        element.submit()
        GLWait.whilePageLoaderIsVisible(self.driver)

        # Select option "exact phrase"
        element = self.driver.find_element_by_xpath('//*[@id = "searchphraseexact"]')
        element.click()

        # Click search button
        element = self.driver.find_element_by_xpath('//*[@name = "Search"]')
        element.click()
        GLWait.whilePageLoaderIsVisible(self.driver)

        # Check if there is any search result
        element = self.driver.find_element_by_xpath('//*[@id="searchForm"]/div/p/strong/span')
        if element.get_attribute("innerText") == "0":
            assert False

if __name__ == "__main__":
    unittest.main()