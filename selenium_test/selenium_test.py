#! /usr/bin/python3
import traceback
import logging
from random import randint, random
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from yaml import safe_load
import sys

with open('resources/config.yaml') as yaml_in:
    config = safe_load(yaml_in)


class BrowserTest:
    def __init__(self, count):
        self.count = count
        options = Options()
        options.headless = True
        self.browser = webdriver.Firefox(
            options=options, firefox_profile=webdriver.FirefoxProfile())

    def open_home(self):
        print("---------------------------------------")
        print("Opening the URL!\n")
        try:
            self.browser.set_page_load_timeout(30)
            self.browser.get(config['selenium_test_url'])
            sleep(randint(5, 10) + random())
            assert 'URL Shortener' in self.browser.title
            print("Pass openhome")
        except Exception as e:
            logging.error("Failed open_home!!!" + config['selenium_test_url'] +
                          "\n" + traceback.format_exc())
            print("Failed open_home!!!" + "\n" + traceback.format_exc())
            sys.exit(1)

    def check_empty_link(self):
        print("---------------------------------------")
        print("Test empty link.\n")
        try:
            sleep(randint(1, 3) + random())
            assert self.browser.find_element_by_class_name(
                'invalid-feedback').is_displayed() == False
            assert len(
                self.browser.find_elements_by_id('cloud_url_output')) == 0
            self.browser.find_element_by_class_name('btn.btn-primary').click()
            assert self.browser.find_element_by_class_name(
                'invalid-feedback').is_displayed() == True
            assert len(
                self.browser.find_elements_by_id('cloud_url_output')) == 0
            print("Pass check empty link")
        except AssertionError as e:
            logging.error("Failed check_empty_link\n" + traceback.format_exc())
            self.count += 1
            print("Failed check_empty_link" + "\n" + traceback.format_exc())

    def check_regular_link(self):
        print("----------------------------------------")
        print("Test the regular links.\n")
        # testcase1
        # https://github.com/yachinz/format_test
        # http://localhost:5000/aloEv2
        try:
            sleep(randint(1, 3) + random())
            self.browser.find_element_by_id('cloud_url_input').send_keys(
                "https://github.com/yachinz/format_test")
            sleep(randint(1, 3) + random())
            self.browser.find_element_by_class_name('btn.btn-primary').click()
            sleep(randint(3, 5) + random())
            # check if this return a URL as wishes
            assert self.browser.find_element_by_id('cloud_url_output').get_attribute("value") == \
                'http://localhost:5000/aloEv2'
            sleep(randint(1, 3) + random())
            self.browser.find_element_by_id('cloud_url_input').clear()
            sleep(randint(1, 3) + random())
            print("Pass testcase 1 in regular link")
        except AssertionError as e:
            logging.error(
                "regular_link 1: https://github.com/yachinz/format_test\n" +
                traceback.format_exc())
            self.count += 1
            print(
                "Failed, regular_link 1: https://github.com/yachinz/format_test"
                + traceback.format_exc())

        # testcase2
        # https://github.com/yachinz/live2d-widget
        # http://localhost:5000/4nSynq
        try:
            self.browser.find_element_by_id('cloud_url_input').send_keys(
                "https://github.com/yachinz/live2d-widget")
            sleep(randint(1, 3) + random())
            self.browser.find_element_by_class_name('btn.btn-primary').click()
            sleep(randint(3, 5) + random())
            # check if this return a URL as wishes
            assert self.browser.find_element_by_id('cloud_url_output').get_attribute("value") == \
                config['selenium_test_url'] + '4nSynq'
            sleep(randint(1, 3) + random())
            self.browser.find_element_by_id('cloud_url_input').clear()
            sleep(randint(1, 3) + random())
            print("Pass testcase 2 in regular link")
        except AssertionError as e:
            logging.error(
                "regular_link 2: https://github.com/yachinz/live2d-widget\n" +
                traceback.format_exc())
            print(
                "Failed, regular_link 2: https://github.com/yachinz/live2d-widget\n"
                + traceback.format_exc())
            self.count += 1

        # testcase3
        # https://github.com/yachinz/easy-animator
        # http://localhost:5000/1JbS5c
        try:
            self.browser.find_element_by_id('cloud_url_input').send_keys(
                "https://github.com/yachinz/easy-animator")
            sleep(randint(1, 3) + random())
            self.browser.find_element_by_class_name('btn.btn-primary').click()
            sleep(randint(3, 5) + random())
            # check if this return a URL as wishes
            assert self.browser.find_element_by_id('cloud_url_output').get_attribute("value") == \
                config['selenium_test_url'] + '1JbS5c'
            sleep(randint(1, 3) + random())
            self.browser.find_element_by_id('cloud_url_input').clear()
            sleep(randint(1, 3) + random())
            print("Pass testcase 3 in regular link")
        except AssertionError as e:
            logging.error(
                "regular_link 3: https://github.com/yachinz/easy-animator\n" +
                traceback.format_exc())
            print(
                "Failed, regular_link 3: https://github.com/yachinz/easy-animator\n"
                + traceback.format_exc())
            self.count += 1

        # testcase4
        # github.com/yachinz/live2d-widget
        # http://localhost:5000/6UErY0
        try:
            self.browser.find_element_by_id('cloud_url_input').send_keys(
                "github.com/yachinz/live2d-widget")
            sleep(randint(1, 3) + random())
            self.browser.find_element_by_class_name('btn.btn-primary').click()
            sleep(randint(3, 5) + random())
            # check if this return a URL as wishes
            assert self.browser.find_element_by_id('cloud_url_output').get_attribute("value") == \
                config['selenium_test_url'] + '6UErY0'
            sleep(randint(1, 3) + random())
            self.browser.find_element_by_id('cloud_url_input').clear()
            sleep(randint(1, 3) + random())
            print("Pass testcase 4 in regular link")
        except AssertionError as e:
            logging.error(
                "regular_link 4: github.com/yachinz/live2d-widget\n" +
                traceback.format_exc())
            print(
                "Failed, regular_link 4: github.com/yachinz/live2d-widget\n" +
                traceback.format_exc())
            self.count += 1

    def check_redirect(self):
        print("-----------------------------------------------")
        print("Test redirect.\n")
        try:
            # testcase1
            # https://github.com/yachinz/format_test
            # http://localhost:5000/aloEv2
            self.browser.get(config['selenium_test_url'] + 'aloEv2')
            sleep(randint(5, 10) + random())
            assert self.browser.current_url == 'https://github.com/yachinz/format_test'
            print("Pass testcase 1 in check_redirect")
        except AssertionError as e:
            logging.error("redirect_link 1: http://localhost:5000/aloEv2, " +
                          "https://github.com/yachinz/format_test\n" +
                          traceback.format_exc())
            print("Failed, redirect_link 1: " + config['selenium_test_url'] +
                  'aloEv2,' + "https://github.com/yachinz/format_test" +
                  traceback.format_exc())
            self.count += 1

        # testcase2
        # https://github.com/yachinz/live2d-widget
        # http://localhost:5000/4nSynq
        try:
            self.browser.get(config['selenium_test_url'] + '4nSynq')
            sleep(randint(5, 10) + random())
            assert self.browser.current_url == 'https://github.com/yachinz/live2d-widget'
            print("Pass testcase 2 in check_redirect")
        except AssertionError as a:
            logging.error(
                "Failed, redirect_link 2: http://localhost:5000/4nSynq, " +
                "https://github.com/yachinz/live2d-widget\n" +
                traceback.format_exc())
            print("Failed, redirect_link 2: " + config['selenium_test_url'] +
                  '4nSynq, ' + "https://github.com/yachinz/live2d-widget" +
                  traceback.format_exc())
            self.count += 1

        # testcase3
        # https://github.com/yachinz/easy-animator
        # http://localhost:5000/1JbS5c
        try:
            self.browser.get(config['selenium_test_url'] + '1JbS5c')
            sleep(randint(5, 10) + random())
            assert self.browser.current_url == 'https://github.com/yachinz/easy-animator'
            print("Pass testcase 3 in check_redirect")
        except AssertionError as a:
            logging.error("redirect_link 3: http://localhost:5000/1JbS5c, " +
                          "https://github.com/yachinz/easy-animator\n" +
                          traceback.format_exc())
            print("Failed, redirect_link 3: " + config['selenium_test_url'] +
                  "1JbS5c, " + "https://github.com/yachinz/easy-animator" +
                  traceback.format_exc())
            self.count += 1

        # testcase4
        # github.com/yachinz/live2d-widget
        # http://localhost:5000/6UErY0
        try:
            self.browser.get(config['selenium_test_url'] + '6UErY0')
            sleep(randint(5, 10) + random())
            assert self.browser.current_url == 'https://github.com/yachinz/live2d-widget'
            print("Pass testcase 4 in check_redirect")
        except AssertionError as a:
            logging.error(
                "failed, redirect_link 4: http://localhost:5000/6UErY0, " +
                "https://github.com/yachinz/live2d-widget\n" +
                traceback.format_exc())
            print("Failed, redirect_link 4: " + config['selenium_test_url'] +
                  "6UErY0, " + "https://github.com/yachinz/live2d-widget" +
                  traceback.format_exc())
            self.count += 1

    def integration(self):
        print("----------------------------------------------")
        print("Integration test 1")
        try:
            self.browser.get(config['selenium_test_url'])
            sleep(randint(1, 3) + random())
            # Input the url link.
            self.browser.find_element_by_id('cloud_url_input').send_keys(
                "https://www.northeastern.edu/")
            sleep(randint(1, 3) + random())

            # Click the submit Button.
            self.browser.find_element_by_class_name('btn.btn-primary').click()
            sleep(randint(3, 5) + random())

            # Get the url from the column
            shortURL = self.browser.find_element_by_id(
                'cloud_url_output').get_attribute("value")
            self.browser.get(shortURL)
            sleep(randint(1, 3) + random())
            assert self.browser.current_url == 'https://www.northeastern.edu/'
            print('Pass, integration test 1')
        except Exception:
            logging.error(
                "Failed, integration test: https://www.northeastern.edu/\n" +
                traceback.format_exc())
            print("Failed, integration test 1!!!" + "\n" +
                  traceback.format_exc())
            self.count += 1

        print("Integration test 2")
        try:
            self.browser.get(config['selenium_test_url'])
            sleep(randint(1, 3) + random())
            # Input the url link.
            self.browser.find_element_by_id('cloud_url_input').send_keys(
                "https://github.com/CS6620-S21/Building-an-Enhanced-CI-Pipeline/tree/main/UI/build"
            )
            sleep(randint(1, 3) + random())

            # Click the submit Button.
            self.browser.find_element_by_class_name('btn.btn-primary').click()
            sleep(randint(3, 5) + random())

            # Get the url from the column
            shortURL = self.browser.find_element_by_id(
                'cloud_url_output').get_attribute("value")
            self.browser.get(shortURL)
            sleep(randint(1, 3) + random())
            assert self.browser.current_url == "https://github.com/CS6620-S21/Building-an" + \
             "-Enhanced-CI-Pipeline/tree/main/UI/build"
            print('Pass, integration test 2')
        except Exception:
            logging.error("Failed, integration test: https://github.com/CS6620-S21/" + \
             "Building-an-Enhanced-CI-Pipeline/tree/main/UI/build/\n" + traceback.format_exc())
            print("Failed, integration test 2!!!" + "\n" +
                  traceback.format_exc())
            self.count += 1

        print("Integration test 3")
        try:
            self.browser.get(config['selenium_test_url'])
            sleep(randint(1, 3) + random())
            # Input the url link.
            self.browser.find_element_by_id('cloud_url_input').send_keys(
                "https://github.com/yachinz/bu_cicd_example_selenium_test/blob/master/selenium_test.py"
            )
            sleep(randint(1, 3) + random())

            # Click the submit Button.
            self.browser.find_element_by_class_name('btn.btn-primary').click()
            sleep(randint(3, 5) + random())

            # Get the url from the column
            shortURL = self.browser.find_element_by_id(
                'cloud_url_output').get_attribute("value")
            self.browser.get(shortURL)
            sleep(randint(1, 3) + random())
            assert self.browser.current_url == "https://github.com/yachinz/bu_cicd_example" +\
            "_selenium_test/blob/master/selenium_test.py"
            print('Pass, integration test 3')
        except Exception:
            logging.error(
                "Failed, integration test: https://github.com/yachinz/bu_cicd"
                + "_example_selenium_test/blob/master/selenium_test.py/\n" +
                traceback.format_exc())
            print("Failed, integration test 3" + "\n" + traceback.format_exc())
            self.count += 1

    def close_browser(self):
        print("***********************************************")
        self.browser.quit()
        print("Browser closed")


if __name__ == '__main__':
    logging.basicConfig(
        filename='log_record.log',
        level=logging.ERROR,
        filemode='w',
        format='[%(asctime)s] [%(levelname)s] >>>  %(message)s',
        datefmt='%Y-%m-%d %I:%M:%S')
    new_browser = BrowserTest(0)
    new_browser.open_home()
    new_browser.check_empty_link()
    # new_browser.check_regular_link()
    # new_browser.check_redirect()
    # new_browser.integration()
    new_browser.close_browser()
    if new_browser.count > 0:
        sys.exit(1)
