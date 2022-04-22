#!/usr/bin env python3
import logging
from typing import Optional, Union

# Driver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# Browsers
from selenium.webdriver.firefox.options import Options as firefox_options
from selenium.webdriver.chrome.options import Options as chrome_coptions
# Time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class HtmlContent(object):
    """HTML content of a webpage
    
    Retrieves the HTML content of a web page using a webdriver (selenium)
    """
    def __init__(self) -> None:
        """HtmlContent Constructor"""
        self.__driver = self.__driver_config()
        self.__html_content = None
        self.__html_content_is_setting = False

    @property
    def html_content(self) -> str:
        """The HTML content

        :returns: HTML content as string
        :raises LookupError: html_content_settings() method not configured
        """
        if not self.__html_content_is_setting:
            error_message = (
                'The "html_content_settings()" method has not '
                'yet been configured.\n'
                'Set it to get the HTML content of the "html_content" property.'
            )
            raise LookupError(error_message)

        return self.__html_content

    @property
    def driver(self) -> Union[
            webdriver.firefox.webdriver.WebDriver,
            webdriver.chrome.webdriver.WebDriver,
            None]:
        """Selenium webdriver

        :returns: selenium webdriver of Chrome or Firefox
        """

        return self.__driver

    def html_content_settings(self, url: str, webdriver_common_by: tuple) -> str:
        """Configuration to get the html content
    
        Use webdriver.common.by, like:
            from selenium.webdriver.common.by import By
            ...
            new_html_content(
                url='https://www.python.org/',
                webdriver_common_by=(By.CLASS_NAME, 'introduction'
            )
        
        :param url: Address of the website you want to scan
        :param webdriver_common_by: A tuple containing the key and value of 
            the HTML tag
        :returns: The html content
        """

        # URL
        self.__driver.get(url)

        seconds_delay = 3
        element = None

        try:
            element = WebDriverWait(
                self.__driver, seconds_delay
            ).until(
                EC.presence_of_element_located(webdriver_common_by)
                # EC.presence_of_element_located((By.CLASS_NAME, 'top'))
            )
        except TimeoutException:
            logging.error('Loading took too much time!')
            self.__driver.close()

        if element:
            self.__html_content = element.get_attribute('outerHTML')
            self.__html_content_is_setting = True

        self.__driver.close()
        return self.__html_content

    def __driver_config(self):
        # Return a webdriver

        driver = None

        # Firefox driver
        try:
            logging.info('Trying to use Firefox driver...')

            driver_options = firefox_options()
            driver_options.headless = True
            driver = webdriver.Firefox(options=driver_options)
            return driver

        except:
            logging.error('Unable to use Firefox driver!')

        # Chrome driver
        try:
            logging.info('Trying to use Chrome driver...')

            driver_options = chrome_coptions()
            driver_options.headless = True
            driver = webdriver.Chrome(options=driver_options)
            return driver

        except:
            logging.error('Unable to use Chrome driver!')

        # Error
        # Message: 'geckodriver' executable needs to be in PATH
        # Make it’s in your PATH, e. g., place it in /usr/bin or /usr/local/bin.
        logging.error(
            'Unable to use available drivers! '
            'Please install Firefox or Google Chrome browser.')
        return driver


if __name__ == '__main__':
    from selenium.webdriver.common.by import By

    html = HtmlContent()
    html.html_content_settings(
        url='https://www.python.org/',
        webdriver_common_by=(By.CLASS_NAME, 'introduction'),
    )
    print(html.html_content)
