#!/usr/bin env python3
import json
import logging
import os

from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

import htmlcontent

class WebScraping(object):
    """"""
    def __init__(self):
        """"""
        self.__config_dirname = 'webscraping_art'
        self.__config_filename = 'webscraping_art.json'
        self.__config_path = os.path.join(
            os.environ["HOME"], '.config',
            self.__config_dirname,
            self.__config_filename,
        )
        self.__configs = self.__load_configs()

    @property
    def config_dirname(self) -> str:
        """"""
        return self.__config_dirname

    @property
    def config_filename(self) -> str:
        """"""
        return self.__config_filename

    @property
    def config_path(self) -> str:
        """"""
        return self.__config_path

    @property
    def configs(self) -> dict:
        """"""
        return self.__configs

    def __load_configs(self) -> dict:
        #
        if os.path.isfile(self.__config_path):
            with open(self.__config_path, 'r') as json_file:
                return json.load(json_file)
        return {}

    def __save_configs(self, data: dict) -> None:
        #
        if not os.path.exists(self.__config_dirname):
            os.makedirs(self.__config_dirname)

        with open(self.__config_path, 'w') as json_file:
            json.dump(data, json_file)


if __name__ == '__main__':
    html = htmlcontent.HtmlContent()
    html.html_content_settings(
        url='https://www.python.org/',
        webdriver_common_by=(By.CLASS_NAME, 'introduction'),
        # webdriver_common_by=(By.CLASS_NAME, 'sticky-wrapper'),
    )
    soup = BeautifulSoup(html.html_content, 'html.parser')
    print(soup.text)
    """
    soup = BeautifulSoup(html.html_content, 'html.parser')
    for link in soup.find_all('a'):
        if 'likes' in link.text.lower():
            print(link.text[len('likes('): -1])
    """