#! /usr/bin/python3
import traceback
import logging
# from argparse import ArgumentParser
from random import randint, random
# from threading import Lock, Thread
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from pyvirtualdisplay import Display
from selenium.webdriver.firefox.options import Options
from yaml import safe_load
import sys

with open('resources/config.yaml') as yaml_in:
    config = safe_load(yaml_in)
class BrowserTest:
    def __init__(self):
        # self.browser = webdriver.Chrome(executable_path='E:/cs6620/proj/raw/driver/chromedriver.exe')
        options = Options()
        options.headless = True
        self.browser = webdriver.Firefox(
            options=options, executable_path='./geckodriver.exe')

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
            logging.error("Failed open_home!!!"+ config['selenium_test_url'] 
            +"\n" + traceback.format_exc())
            print("Failed open_home!!!")
            sys.exit()


    # test if the warning shows when the input is empty. Need some fix.
    def check_empty_link(self):
        print("---------------------------------------")
        print("Test empty link.\n")
        try:
            # not show
            # assert len(self.browser.find_element_by_tag_name('Form.Control.Feedback')) == 0
            sleep(randint(1, 3) + random())
            assert self.browser.find_element_by_class_name(
                'invalid-feedback').is_displayed() == False
            assert len(self.browser.find_elements_by_id(
                'cloud_url_output')) == 0
            self.browser.find_element_by_class_name('btn.btn-primary').click()
            assert self.browser.find_element_by_class_name(
                'invalid-feedback').is_displayed() == True
            assert len(self.browser.find_elements_by_id(
                'cloud_url_output')) == 0
            print("Pass check empty link")
        except AssertionError as e:
            logging.error("Falied check_empty_link\n" + traceback.format_exc())
            print("Falied check_empty_link")

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
            logging.error("regular_link 1: https://github.com/yachinz/format_test\n" 
            + traceback.format_exc())
            print("Falied, regular_link 1: https://github.com/yachinz/format_test")

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
                'http://localhost:5000/4nSynq'
            sleep(randint(1, 3) + random())
            self.browser.find_element_by_id('cloud_url_input').clear()
            sleep(randint(1, 3) + random())
            print("Pass testcase 2 in regular link")
        except AssertionError as e:
            logging.error("regular_link 2: https://github.com/yachinz/live2d-widget\n" 
            + traceback.format_exc())
            print("Falied, regular_link 2: https://github.com/yachinz/live2d-widget")

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
                'http://localhost:5000/1JbS5c'
            sleep(randint(1, 3) + random())
            self.browser.find_element_by_id('cloud_url_input').clear()
            sleep(randint(1, 3) + random())
            print("Pass testcase 3 in regular link")
        except AssertionError as e:
            logging.error("regular_link 3: https://github.com/yachinz/easy-animator\n" 
            + traceback.format_exc())
            print("Falied, regular_link 3: https://github.com/yachinz/easy-animator")

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
                'http://localhost:5000/6UErY0'
            sleep(randint(1, 3) + random())
            self.browser.find_element_by_id('cloud_url_input').clear()
            sleep(randint(1, 3) + random())
            print("Pass testcase 4 in regular link")
        except AssertionError as e:
            logging.error("regular_link 4: github.com/yachinz/live2d-widget\n" 
            + traceback.format_exc())
            print("Falied, regular_link 4: github.com/yachinz/live2d-widget")

    def check_redirect(self):
        print("-----------------------------------------------")
        print("Test redirect.\n")
        try:
            # testcase1
            # https://github.com/yachinz/format_test
            # http://localhost:5000/aloEv2
            self.browser.get('http://localhost:5000/aloEv2')
            sleep(randint(5, 10) + random())
            assert self.browser.current_url == 'https://github.com/yachinz/format_test'
            print("Pass testcase 1 in check_redirect")
        except AssertionError as e:
            logging.error("redirect_link 1: http://localhost:5000/aloEv2, " 
            + "https://github.com/yachinz/format_test\n" 
            + traceback.format_exc())
            print(
                "Falied, redirect_link 1: http://localhost:5000/aloEv2, " 
                + "https://github.com/yachinz/format_test")

        # testcase2
        # https://github.com/yachinz/live2d-widget
        # http://localhost:5000/4nSynq
        try:
            self.browser.get('http://localhost:5000/4nSynq')
            sleep(randint(5, 10) + random())
            assert self.browser.current_url == 'https://github.com/yachinz/live2d-widget'
            print("Pass testcase 2 in check_redirect")
        except AssertionError as a:
            logging.error("Falied, redirect_link 2: http://localhost:5000/4nSynq, "
            + "https://github.com/yachinz/live2d-widget\n" 
            + traceback.format_exc())
            print("Failed, redirect_link 2: http://localhost:5000/4nSynq, " 
            + "https://github.com/yachinz/live2d-widget")

        # testcase3
        # https://github.com/yachinz/easy-animator
        # http://localhost:5000/1JbS5c
        try:
            self.browser.get('http://localhost:5000/1JbS5c')
            sleep(randint(5, 10) + random())
            assert self.browser.current_url == 'https://github.com/yachinz/easy-animator'
            print("Pass testcase 3 in check_redirect")
        except AssertionError as a:
            logging.error("redirect_link 3: http://localhost:5000/1JbS5c, " 
            + "https://github.com/yachinz/easy-animator\n" 
            + traceback.format_exc())
            print("Failed, redirect_link 3: http://localhost:5000/1JbS5c, " 
            + "https://github.com/yachinz/easy-animator")

        # testcase4
        # github.com/yachinz/live2d-widget
        # http://localhost:5000/6UErY0
        try:
            self.browser.get('http://localhost:5000/6UErY0')
            sleep(randint(5, 10) + random())
            assert self.browser.current_url == 'https://github.com/yachinz/live2d-widget'
            print("Pass testcase 4 in check_redirect")
        except AssertionError as a:
            logging.error("Falied, redirect_link 4: http://localhost:5000/6UErY0, " 
            + "https://github.com/yachinz/live2d-widget\n" 
            + traceback.format_exc())
            print("Failed, redirect_link 4: http://localhost:5000/6UErY0, " 
            + "https://github.com/yachinz/live2d-widget")

    def integration(self):
        print("----------------------------------------------")
        print("Integration test")
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

            # Copy the short url in clipboard.
            # I don't know how paste it in get() so I skipped this part

            # Get the url from the column
            shortURL = self.browser.find_element_by_id(
                'cloud_url_output').get_attribute("value")
            self.browser.get(shortURL)
            sleep(randint(1, 3) + random())
            assert self.browser.current_url == 'https://www.northeastern.edu/'
            print('Pass, integration test')
        except Exception:
            logging.error("Falied, integration test: https://www.northeastern.edu/\n" + traceback.format_exc())
            print("Failed, integration test!!!")

    def close_browser(self):
        print("***********************************************")
        self.browser.quit()
        print("Browser closed")

class ArgParser:
    def __init__(self):
        description = 'Usage: python selenium_test.py  '
        parser = ArgumentParser(description=description)
        parser.add_argument('-x', '--headless', required=False, action='store_true',
                            help='add -x option to run in terminal only (no GUI)')
        self.args = parser.parse_args()

    def get_args(self):
        return self.args


# class MultiBrowserTest(ArgParser):
#     def __init__(self, n):
#         super().__init__()

#         self.browsers = [None for _ in range(n)]
#         self.lock = Lock()

#     def _browser_thread(self, index):
#         new_browser = BrowserTest()
#         with self.lock:
#             self.browsers[index] = new_browser
#         new_browser.open_home()
#         # new_browser.check_heading()
#         new_browser.click_api()

#     def open_browsers(self):
#         try:
#             threads = []
#             for index in range(len(self.browsers)):
#                 current_thread = Thread(target=self._browser_thread, args=[index])
#                 current_thread.start()
#                 threads.append(current_thread)
#             _ = [fin_thread.join() for fin_thread in threads]
#         finally:
#             sleep(randint(60, 70) + random())
#             _ = [obj.close_browser() for obj in self.browsers if obj is not None]


if __name__ == '__main__':
    logging.basicConfig(filename='log_record.log',
    level=logging.ERROR, filemode='w', format='[%(asctime)s] [%(levelname)s] >>>  %(message)s',
                    datefmt='%Y-%m-%d %I:%M:%S')
    new_browser = BrowserTest()
    new_browser.open_home()
    new_browser.check_empty_link()
    new_browser.check_regular_link()
    new_browser.check_redirect()
    new_browser.integration()
    new_browser.close_browser()

    # sel_test = MultiBrowserTest(1)
    # if not sel_test.get_args().headless:
    #     sel_test.open_browsers()
    # else:
    #     with Display():
    #         sel_test.open_browsers()
