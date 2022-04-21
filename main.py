#!/usr/bin env python3
import logging
from typing import Optional, Union

from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

import htmlcontent


def main():
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


if __name__ == '__main__':
    main()