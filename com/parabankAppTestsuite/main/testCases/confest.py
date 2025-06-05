from selenium import webdriver
import pytest

def setup(browser):
    if browser=="chrome":
        driver=webdriver.Chrome()
    elif browser=="firefox":
        driver=webdriver.Firefox()
    else:
        driver=webdriver.Ie()
    return driver

