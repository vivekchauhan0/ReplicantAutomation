import unittest
from selenium import webdriver

# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.proxy import Proxy, ProxyType
import unittest, time, re
from bs4 import BeautifulSoup
import pickle
import random
import csv
import traceback
import Automation.WebAutomation.alog
import xml.parsers.expat as xmlerr
import shutil,os,zipfile,socket,time
import json
import sys
import csv
import xml.etree.cElementTree as ET
import pprint
import requests
from collections import defaultdict
import datetime
import math
from decimal import Decimal
import os
import platform
import zipfile
import mmap
import uuid
import os
import traceback
from threading import Thread
from time import sleep
import subprocess
from subprocess import call
from subprocess import Popen, PIPE
import threading
import glob
from threading import Lock
lock = Lock()
import multiprocessing
import time
import mmap
import pprint
import pytest
import nltk
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.opera.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
import Automation.WebAutomation.charlesProxyService as c
from Automation.WebAutomation.utilities import createFolder
import Automation.WebAutomation.webconfig as wc
from Automation.WebAutomation.mainWebTestRunner import _data
from inspect import currentframe, getframeinfo
import asyncio
import websockets
import base64
from websocket import create_connection
import ssl
import certifi
import asyncio
import websockets
import ssl
from bs4 import BeautifulSoup
from sys import platform
import pandas as pd
pp = pprint.PrettyPrinter(indent=4)
BASE_DIR = os.getcwd()
print("The current directory is")
print(BASE_DIR)
#os.path.join(BASE_DIR,
base_path = BASE_DIR
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print("The current directory is")
print(BASE_DIR)
BETA_URL = wc.BETA_URL
QA_URL = wc.QA_URL
PROD_URL = wc.PROD_URL

conversationBuilder_Bot = {}
conversationBuilder_Client = {}
conversationBuilder = {}

WEBDRIVERDIRECTORY = os.path.join(BASE_DIR, 'WebAutomation/Drivers', 'webdrivers')

############################################################
global test_results_dir_json_wire
global test_results_dir_csv
global test_results_dir_excel
global test_results_dir_html
global test_results_dir_json_reports

#############################  #############################
print("Getting the values for the Directories")
test_results_dir_json_wire = _data['test_results_dir_json_wire']
print(test_results_dir_json_wire)
test_results_dir_csv = _data['test_results_dir_csv']
print(test_results_dir_csv)
test_results_dir_excel = _data['test_results_dir_excel']
print(test_results_dir_excel)
test_results_dir_html = _data['test_results_dir_html']
print(test_results_dir_html)
test_results_dir_json_reports = _data['test_results_dir_json_reports']
print(test_results_dir_json_reports)

###########################################################

if platform == "linux" or platform == "linux2":
    print("Linux")
    platform = 'Linux'
    WEBDRIVERDIRECTORY_CHROMEDRIVER = os.path.join(WEBDRIVERDIRECTORY,'chromedriver','chromedriver_linux64')
    WEBDRIVERDIRECTORY_FIREFOXDRIVER = os.path.join(WEBDRIVERDIRECTORY, 'firefoxdriver','geckodriver-linux64')

if platform == "darwin":
    print("Darwin")
    platform = 'Darwin'
    WEBDRIVERDIRECTORY_CHROMEDRIVER = os.path.join(WEBDRIVERDIRECTORY, 'chromedriver', 'chromedriver_mac64')
    WEBDRIVERDIRECTORY_FIREFOXDRIVER = os.path.join(WEBDRIVERDIRECTORY, 'firefoxdriver', 'geckodriver-macos')
    WEBDRIVERDIRECTORY_SAFARIDRIVER = os.path.join(WEBDRIVERDIRECTORY, '', '')


if platform == "win32":
    print("Win32")
    platform = 'Win32'
    WEBDRIVERDIRECTORY_CHROMEDRIVER = os.path.join(WEBDRIVERDIRECTORY, 'chromedriver', 'chromedriver_win32')
    WEBDRIVERDIRECTORY_FIREFOXDRIVER = os.path.join(WEBDRIVERDIRECTORY, 'firefoxdriver', 'geckodriver-win64')

if platform == "win64":
    print("Win64")
    platform = 'Win64'
    WEBDRIVERDIRECTORY_CHROMEDRIVER = os.path.join(WEBDRIVERDIRECTORY, 'chromedriver', 'chromedriver_win32')
    WEBDRIVERDIRECTORY_FIREFOXDRIVER = os.path.join(WEBDRIVERDIRECTORY, 'firefoxdriver', 'geckodriver-win64')

ssl_context = ssl.create_default_context()
ssl_context.load_verify_locations(certifi.where())

@pytest.fixture(params=["firefox"],scope="class")
#############################  #############################


def driver_init(request):
    if request.param == "chrome":
        # Local webdriver implementation
        print("Starting Chrome test")
        if _data['MITM'] == 'True':
            print("Since the MITM Proxy is TRUE we will Set the Proxy option")
            myProxy = wc.MITMHOST + ':' + wc.MITMPORT
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--proxy-server=%s' % myProxy)
            chrome_options.add_argument('ignore-certificate-errors')
            if _data['HEADLESS'] == 'True':
                print("Setting the Headless option for Chrome")
                chrome_options.add_argument("--headless")
                chrome_options.add_argument('--no-sandbox')
                chrome_options.add_argument('--disable-dev-shm-usage')
            print("Chromedriver Location")
            print(WEBDRIVERDIRECTORY_CHROMEDRIVER + '/chromedriver')
            web_driver = webdriver.Chrome(executable_path=WEBDRIVERDIRECTORY_CHROMEDRIVER + '/chromedriver',options=chrome_options)
        else:
            print("Since the MITM Proxy is FALSE we will NOT Set the Proxy option")
            print("Chromedriver Location")
            print(WEBDRIVERDIRECTORY_CHROMEDRIVER + '/chromedriver')
            chrome_options = webdriver.ChromeOptions()
            if _data['HEADLESS'] == 'True':
                print("Setting the Headless option for Chrome")
                chrome_options.add_argument("--headless")
                chrome_options.add_argument('--no-sandbox')
                chrome_options.add_argument('--disable-dev-shm-usage')
            web_driver = webdriver.Chrome(executable_path=WEBDRIVERDIRECTORY_CHROMEDRIVER + '/chromedriver',options=chrome_options)

    if request.param == "firefox":
        print("Starting Firefox test")
        if _data['MITM'] == 'True':
            print("Since the MITM Proxy is TRUE we will Set the Proxy option")
            # Local webdriver implementation
            myProxy = wc.MITMHOST + ':' + wc.MITMPORT
            proxy = Proxy({
                'proxyType': ProxyType.MANUAL,
                'httpProxy': myProxy,
                'ftpProxy': myProxy,
                'sslProxy': myProxy,
                'noProxy': ''  # set this value as desired
            })

            fireFoxOptions = webdriver.FirefoxOptions()
            if _data['HEADLESS'] == 'True':
                print("Setting the Headless option for Firefox")
                fireFoxOptions.set_headless()
            fireFoxOptions.set_preference('network.http.phishy-userpass-length', 255)
            fireFoxOptions.set_preference("network.automatic-ntlm-auth.trusted-uris", PROD_URL)
            fireFoxOptions.set_preference("network.proxy.type", 1)
            fireFoxOptions.set_preference("network.proxy.http", wc.MITMHOST)
            fireFoxOptions.set_preference("network.proxy.http_port", wc.MITMPORT)
            ###############################
            # fireFoxOptions.set_preference('network.proxy.type', 1)
            # # Set the host/port.
            # fireFoxOptions.set_preference('network.proxy.http', proxy_host)
            fireFoxOptions.set_preference("browser.cache.disk.enable", True)
            fireFoxOptions.set_preference("browser.cache.memory.enable", True)
            fireFoxOptions.set_preference("browser.cache.offline.enable", True)
            fireFoxOptions.set_preference('network.proxy.https_port', wc.MITMPORT)
            fireFoxOptions.set_preference("network.proxy.ssl", wc.MITMHOST)
            fireFoxOptions.set_preference("network.proxy.ssl_port", int(wc.MITMPORT))
            print("Gecko Location")
            print(WEBDRIVERDIRECTORY_FIREFOXDRIVER + '/geckodriver')
            web_driver = webdriver.Firefox(executable_path=WEBDRIVERDIRECTORY_FIREFOXDRIVER + '/geckodriver', firefox_options=fireFoxOptions)
            web_driver.implicitly_wait(1)
            web_driver.delete_all_cookies()
        else:
            print("Since the MITM Proxy is FALSE we will NOT Set the Proxy option")
            print("Gecko Location")
            print(WEBDRIVERDIRECTORY_FIREFOXDRIVER + '/geckodriver')
            fireFoxOptions = webdriver.FirefoxOptions()
            if _data['HEADLESS'] == 'True':
                print("Setting the Headless option for Firefox")
                fireFoxOptions.set_headless()

            web_driver = webdriver.Firefox(executable_path=WEBDRIVERDIRECTORY_FIREFOXDRIVER + '/geckodriver', firefox_options=fireFoxOptions)
            web_driver.implicitly_wait(1)
            web_driver.delete_all_cookies()

    # if request.param == "safari":
    #     # Local webdriver implementation
    #     options = Options()

    request.cls.driver = web_driver
    yield
    web_driver.close()

@pytest.mark.usefixtures("driver_init")
class BasicTest:
    print("Initializing Basic Test")
    pass
class Test_URL(BasicTest):
        print("Initializing URL Open Test")

        #Test 1
        def test_greeting(self):
            try:
                counterConversation = 0
                _t = None
                print("Running the Test Open Url")
                if _data['MITM'] == 'True':
                    print("Clearing Cache as flag is True")
                    c.clearCache()
                time.sleep(2)
                ######################### Using Proxy Service ##########################################
                self.driver.delete_all_cookies()
                self.driver.get("https://chatbot-challenge.dev.replicant.ai")

                ################# Get Data from the Proxy for Validation instead of Web #####################
                time.sleep(2)
                parser = self.driver.page_source
                # Two Layers of Validation
                # First Option to get Data Scraped from Web
                # Second Option to get Data from Proxy
                # Third option to get data from Web Socket
                soup = BeautifulSoup(parser, "html.parser")
                pagelinks = soup.find_all('p', {'class': 'MuiTypography-root MuiTypography-body1'})
                #for pagenumber in pagelinks:
                try:
                        # print(pagenumber.text)
                        conversationBuilder[str(counterConversation)] = pagelinks[counterConversation].text

                        ############# Validation Type 1 with the Web #########################
                        assert "Greetings, friend! Type help to get started." in pagelinks[counterConversation].text
                        counterConversation = counterConversation + 1
                except:
                        print("Cannot Collect All the Page")
                        print(traceback.format_exc())

                ################ Now get the data from the MITM Proxy #########
                _t = c.getJSON("test_open_url", wc.SNIFFHOST)
                frameinfo = getframeinfo(currentframe())
                print(frameinfo.filename, frameinfo.lineno)
                print("Performance Data")
                print(_t[0]['response']['body']['text'])
                print(_t[0]['durations'])
                ###################### Validation Layer #####################################################
                _temp = _t[0]['response']['body']['text']
                #############################################################################################
                sleep(2)
                #########################################################
                print("Creating Local Test Folders for Test")
                simpleTest_Folder_dir_json_wire = os.path.join(test_results_dir_json_wire, "SimpleTest" + self.driver.name + "/test_greeting")
                print(simpleTest_Folder_dir_json_wire)
                createFolder(simpleTest_Folder_dir_json_wire)
                simpleTest_Folder_dir_csv = os.path.join(test_results_dir_csv, "SimpleTest" + self.driver.name + "/test_greeting")
                print(simpleTest_Folder_dir_csv)
                createFolder(simpleTest_Folder_dir_csv)
                simpleTest_Folder_dir_excel = os.path.join(test_results_dir_excel, "SimpleTest" + self.driver.name + "/test_greeting")
                print(simpleTest_Folder_dir_excel)
                createFolder(simpleTest_Folder_dir_excel)
                simpleTest_Folder_dir_html = os.path.join(test_results_dir_html, "SimpleTest" + self.driver.name + "/test_greeting")
                print(simpleTest_Folder_dir_html)
                createFolder(simpleTest_Folder_dir_html)

                ############## API ##############
                if _data['MITM'] == 'True':
                    print("Get Proxy data as flag is On")
                    _t = c.getJSON("test_greeting", wc.SNIFFHOST)
                    print(_t)
                    if _t == None:
                        print("No Data")
                    else:

                            print("Path")
                            print(_t[0]['path'] )
                            print("Performance Data")
                            print(_t[0]['times'])
                            print(_t[0]['durations'])
                            _responsebody = _t[0]['response']['body']['text']
                            print(_responsebody)

                    print("Got JSON Data")
                    print("We will perform assertion now")

            except:
                print(traceback.format_exc())

        # Test 2
        def test_incorrect_message(self):
            try:
                counterConversation = 0
                _t = None
                print("Running the Test Open Url")
                if _data['MITM'] == 'True':
                    print("Clearing Cache as flag is True")
                    c.clearCache()
                time.sleep(2)
                ######################### Using Proxy Service ##########################################
                self.driver.delete_all_cookies()
                self.driver.get("https://chatbot-challenge.dev.replicant.ai")

                ################# Get Data from the Proxy for Validation instead of Web #####################
                time.sleep(2)
                parser = self.driver.page_source
                # Two Layers of Validation
                # First Option to get Data Scraped from Web
                # Second Option to get Data from Proxy
                # Third option to get data from Web Socket
                soup = BeautifulSoup(parser, "html.parser")
                pagelinks = soup.find_all('p', {'class': 'MuiTypography-root MuiTypography-body1'})
                #for pagenumber in pagelinks:
                try:
                        # print(pagenumber.text)
                        conversationBuilder[str(counterConversation)] = pagelinks[counterConversation].text
                        ############# Validation Type 1 with the Web #########################
                        assert "Greetings, friend! Type help to get started." in pagelinks[counterConversation].text
                        counterConversation = counterConversation + 1
                except:
                        print("Cannot Collect All the Page")
                        print(traceback.format_exc())

                ################ Now get the data from the MITM Proxy #########
                _t = c.getJSON("test_open_url", wc.SNIFFHOST)
                frameinfo = getframeinfo(currentframe())
                print(frameinfo.filename, frameinfo.lineno)
                print("Performance Data")
                print(_t[0]['response']['body']['text'])
                print(_t[0]['durations'])
                ###################### Validation Layer #####################################################
                _temp = _t[0]['response']['body']['text']
                #############################################################################################
                #############################################################################################
                self.driver.find_element(By.CSS_SELECTOR, ".MuiInputBase-input").click()
                self.driver.find_element(By.CSS_SELECTOR, ".MuiInputBase-input").send_keys("hello")
                self.driver.find_element(By.CSS_SELECTOR, ".MuiInputBase-input").send_keys(Keys.ENTER)
                counterConversation = counterConversation + 1
                time.sleep(3)
                ############################ Two Layers of Validation #######################################
                # First Option to get Data Scraped from Web
                # Second Option to get Data from Proxy
                # Third option to get data from Web Socket
                parser = self.driver.page_source
                soup = BeautifulSoup(parser, "html.parser")
                pagelinks = soup.find_all('p', {'class': 'MuiTypography-root MuiTypography-body1'})
                # for pagenumber in pagelinks:
                try:
                    conversationBuilder[str(counterConversation)] = pagelinks[counterConversation].text
                    ############# Validation Type 1 with the Web #########################
                    assert "I'm sorry, I don't understand what you mean." in pagelinks[counterConversation].text

                except:
                        print("Cannot Collect All the Page")
                        print(traceback.format_exc())

                ################ Now get the data from the MITM Proxy #########
                _t = c.getJSON("test_open_url", wc.SNIFFHOST)
                frameinfo = getframeinfo(currentframe())
                print(frameinfo.filename, frameinfo.lineno)
                print("Performance Data")
                print(_t[0]['response']['body']['text'])
                print(_t[0]['durations'])
                ###################### Validation Layer #####################################################
                _temp = _t[0]['response']['body']['text']

                sleep(2)
                #########################################################
                print("Creating Local Test Folders for Test")
                simpleTest_Folder_dir_json_wire = os.path.join(test_results_dir_json_wire, "SimpleTest" + self.driver.name + "/test_incorrect_message")
                print(simpleTest_Folder_dir_json_wire)
                createFolder(simpleTest_Folder_dir_json_wire)
                simpleTest_Folder_dir_csv = os.path.join(test_results_dir_csv, "SimpleTest" + self.driver.name + "/test_incorrect_message")
                print(simpleTest_Folder_dir_csv)
                createFolder(simpleTest_Folder_dir_csv)
                simpleTest_Folder_dir_excel = os.path.join(test_results_dir_excel, "SimpleTest" + self.driver.name + "/test_incorrect_message")
                print(simpleTest_Folder_dir_excel)
                createFolder(simpleTest_Folder_dir_excel)
                simpleTest_Folder_dir_html = os.path.join(test_results_dir_html, "SimpleTest" + self.driver.name + "/test_incorrect_message")
                print(simpleTest_Folder_dir_html)
                createFolder(simpleTest_Folder_dir_html)

                ############## API ##############
                if _data['MITM'] == 'True':
                    print("Get Proxy data as flag is On")
                    _t = c.getJSON("test_greeting", wc.SNIFFHOST)
                    print(_t)
                    if _t == None:
                        print("No Data")
                    else:

                            print("Path")
                            print(_t[0]['path'] )
                            print("Performance Data")
                            print(_t[0]['times'])
                            print(_t[0]['durations'])
                            # _requestbody= base64.b64decode(_t[0]['request']['body']['encoded'])
                            # print(_requestbody)
                            _responsebody = _t[0]['response']['body']['text']
                            print(_responsebody)

                    print("Got JSON Data")
                    print("We will perform assertion now")

            except:
                print(traceback.format_exc())

        # Test 3
        def test_help_message(self):
            try:
                counterConversation = 0
                _t = None
                print("Running the Test Open Url")
                if _data['MITM'] == 'True':
                    print("Clearing Cache as flag is True")
                    c.clearCache()
                time.sleep(2)
                ######################### Using Proxy Service ##########################################
                self.driver.delete_all_cookies()
                self.driver.get("https://chatbot-challenge.dev.replicant.ai")

                ################# Get Data from the Proxy for Validation instead of Web #####################
                time.sleep(2)

                # Two Layers of Validation
                # First Option to get Data Scraped from Web
                # Second Option to get Data from Proxy
                # Third option to get data from Web Socket
                parser = self.driver.page_source
                soup = BeautifulSoup(parser, "html.parser")
                pagelinks = soup.find_all('p', {'class': 'MuiTypography-root MuiTypography-body1'})
                #for pagenumber in pagelinks:
                try:
                        # print(pagenumber.text)
                        conversationBuilder[str(counterConversation)] = pagelinks[counterConversation].text
                        ############# Validation Type 1 with the Web #########################
                        assert "Greetings, friend! Type help to get started." in pagelinks[counterConversation].text
                        counterConversation = counterConversation + 1
                except:
                        print("Cannot Collect All the Page")
                        print(traceback.format_exc())

                ################ Now get the data from the MITM Proxy #########
                _t = c.getJSON("test_open_url", wc.SNIFFHOST)
                frameinfo = getframeinfo(currentframe())
                print(frameinfo.filename, frameinfo.lineno)
                print("Performance Data")
                print(_t[0]['response']['body']['text'])
                print(_t[0]['durations'])
                ###################### Validation Layer #####################################################
                _temp = _t[0]['response']['body']['text']
                #############################################################################################
                #############################################################################################
                self.driver.find_element(By.CSS_SELECTOR, ".MuiInputBase-input").click()
                self.driver.find_element(By.CSS_SELECTOR, ".MuiInputBase-input").send_keys("help")
                self.driver.find_element(By.CSS_SELECTOR, ".MuiInputBase-input").send_keys(Keys.ENTER)
                counterConversation = counterConversation + 1
                time.sleep(3)
                ############################ Two Layers of Validation #######################################
                # First Option to get Data Scraped from Web
                # Second Option to get Data from Proxy
                # Third option to get data from Web Socket
                parser = self.driver.page_source
                soup = BeautifulSoup(parser, "html.parser")
                pagelinks = soup.find_all('p', {'class': 'MuiTypography-root MuiTypography-body1'})
                # for pagenumber in pagelinks:
                try:
                    conversationBuilder[str(counterConversation)] = pagelinks[counterConversation].text
                    ############# Validation Type 1 with the Web #########################
                    assert "I am a reminder bot, here to help you get organized. Here are some of the things you can ask me to do" in pagelinks[counterConversation].text

                except:
                        print("Cannot Collect All the Page")
                        print(traceback.format_exc())

                ################ Now get the data from the MITM Proxy #########
                _t = c.getJSON("test_open_url", wc.SNIFFHOST)
                frameinfo = getframeinfo(currentframe())
                print(frameinfo.filename, frameinfo.lineno)
                print("Performance Data")
                print(base64.b64decode(_t[0]['response']['body']['encoded']))
                print(_t[0]['durations'])
                ###################### Validation Layer #####################################################
                _temp = base64.b64decode(_t[0]['response']['body']['encoded'])
                #############################################################################################
                sleep(2)
                #########################################################
                print("Creating Local Test Folders for Test")
                simpleTest_Folder_dir_json_wire = os.path.join(test_results_dir_json_wire, "SimpleTest" + self.driver.name + "/test_help_message")
                print(simpleTest_Folder_dir_json_wire)
                createFolder(simpleTest_Folder_dir_json_wire)
                simpleTest_Folder_dir_csv = os.path.join(test_results_dir_csv, "SimpleTest" + self.driver.name + "/test_help_message")
                print(simpleTest_Folder_dir_csv)
                createFolder(simpleTest_Folder_dir_csv)
                simpleTest_Folder_dir_excel = os.path.join(test_results_dir_excel, "SimpleTest" + self.driver.name + "/test_help_message")
                print(simpleTest_Folder_dir_excel)
                createFolder(simpleTest_Folder_dir_excel)
                simpleTest_Folder_dir_html = os.path.join(test_results_dir_html, "SimpleTest" + self.driver.name + "/test_help_message")
                print(simpleTest_Folder_dir_html)
                createFolder(simpleTest_Folder_dir_html)

                ############## API ##############
                if _data['MITM'] == 'True':
                    print("Get Proxy data as flag is On")
                    _t = c.getJSON("test_greeting", simpleTest_Folder_dir_json_wire)
                    print(_t)
                    if _t == None:
                        print("No Data")
                    else:
                            print("Path")
                            print(_t[0]['path'] )
                            print("Performance Data")
                            print(_t[0]['times'])
                            print(_t[0]['durations'])
                            _responsebody = base64.b64decode(_t[0]['response']['body']['encoded'])
                            print(_responsebody)
                            _temp = _responsebody.decode(errors='replace').split('�')
                            print(_temp)

                    print("Got JSON Data")
                    print("We will perform assertion now")

            except:
                print(traceback.format_exc())

        # Test 4
        def test_show_all_reminders_with_no_reminders_set(self):
            try:
                counterConversation = 0
                _t = None
                print("Running the Test Open Url")
                if _data['MITM'] == 'True':
                    print("Clearing Cache as flag is True")
                    c.clearCache()
                time.sleep(2)
                ######################### Using Proxy Service ##########################################
                self.driver.delete_all_cookies()
                self.driver.get("https://chatbot-challenge.dev.replicant.ai")

                ################# Get Data from the Proxy for Validation instead of Web #####################
                time.sleep(2)
                parser = self.driver.page_source
                # Two Layers of Validation
                # First Option to get Data Scraped from Web
                # Second Option to get Data from Proxy
                # Third option to get data from Web Socket
                soup = BeautifulSoup(parser, "html.parser")
                pagelinks = soup.find_all('p', {'class': 'MuiTypography-root MuiTypography-body1'})
                #for pagenumber in pagelinks:
                try:
                        # print(pagenumber.text)
                        conversationBuilder[str(counterConversation)] = pagelinks[counterConversation].text
                        ############# Validation Type 1 with the Web #########################
                        assert "Greetings, friend! Type help to get started." in pagelinks[counterConversation].text
                        counterConversation = counterConversation + 1
                except:
                        print("Cannot Collect All the Page")
                        print(traceback.format_exc())

                ################ Now get the data from the MITM Proxy #########
                _t = c.getJSON("test_open_url", wc.SNIFFHOST)
                frameinfo = getframeinfo(currentframe())
                print(frameinfo.filename, frameinfo.lineno)
                print("Performance Data")
                print(_t[0]['response']['body']['text'])
                print(_t[0]['durations'])
                ###################### Validation Layer #####################################################
                _temp = _t[0]['response']['body']['text']
                #############################################################################################
                #############################################################################################
                self.driver.find_element(By.CSS_SELECTOR, ".MuiInputBase-input").click()
                self.driver.find_element(By.CSS_SELECTOR, ".MuiInputBase-input").send_keys("help")
                self.driver.find_element(By.CSS_SELECTOR, ".MuiInputBase-input").send_keys(Keys.ENTER)
                counterConversation = counterConversation + 1
                time.sleep(3)
                ############################ Two Layers of Validation #######################################
                # First Option to get Data Scraped from Web
                # Second Option to get Data from Proxy
                # Third option to get data from Web Socket
                parser = self.driver.page_source
                soup = BeautifulSoup(parser, "html.parser")
                pagelinks = soup.find_all('p', {'class': 'MuiTypography-root MuiTypography-body1'})
                # for pagenumber in pagelinks:
                try:
                    conversationBuilder[str(counterConversation)] = pagelinks[counterConversation].text
                    ############# Validation Type 1 with the Web #########################
                    assert "I am a reminder bot, here to help you get organized. Here are some of the things you can ask me to do" in pagelinks[counterConversation].text
                    counterConversation = counterConversation + 1
                except:
                        print("Cannot Collect All the Page")
                        print(traceback.format_exc())

                ################ Now get the data from the MITM Proxy #########
                _t = c.getJSON("test_open_url", wc.SNIFFHOST)
                frameinfo = getframeinfo(currentframe())
                print(frameinfo.filename, frameinfo.lineno)
                print("Performance Data")
                print(base64.b64decode(_t[0]['response']['body']['encoded']))
                print(_t[0]['durations'])
                ###################### Validation Layer #####################################################
                _temp = base64.b64decode(_t[0]['response']['body']['encoded'])
                #############################################################################################
                self.driver.find_element(By.CSS_SELECTOR, ".MuiInputBase-input").send_keys("show all reminders")
                self.driver.find_element(By.CSS_SELECTOR, ".MuiInputBase-input").send_keys(Keys.ENTER)
                counterConversation = counterConversation + 1
                time.sleep(4)
                ############################ Two Layers of Validation #######################################
                # First Option to get Data Scraped from Web
                # Second Option to get Data from Proxy
                # Third option to get data from Web Socket
                parser = self.driver.page_source
                soup = BeautifulSoup(parser, "html.parser")
                pagelinks = soup.find_all('p', {'class': 'MuiTypography-root MuiTypography-body1'})
                #for pagenumber in pagelinks:
                try:
                    conversationBuilder[str(counterConversation)] = pagelinks[counterConversation].text
                    ############# Validation Type 1 with the Web #########################
                    assert "You have no reminders." in pagelinks[counterConversation].text
                    counterConversation = counterConversation + 1

                except:
                    print("Cannot Collect All the Page")
                    print(traceback.format_exc())

                ################ Now get the data from the MITM Proxy #########
                _t = c.getJSON("test_open_url", wc.SNIFFHOST)
                frameinfo = getframeinfo(currentframe())
                print(frameinfo.filename, frameinfo.lineno)
                print("Performance Data")
                print(base64.b64decode(_t[0]['response']['body']['encoded']))
                print(_t[0]['durations'])
                ###################### Validation Layer #####################################################
                _temp = base64.b64decode(_t[0]['response']['body']['encoded'])

                #############################################################################################
                sleep(2)
                #########################################################
                print("Creating Local Test Folders for Test")
                simpleTest_Folder_dir_json_wire = os.path.join(test_results_dir_json_wire, "SimpleTest" + self.driver.name + "/test_show_all_reminders_with_no_reminders_set")
                print(simpleTest_Folder_dir_json_wire)
                createFolder(simpleTest_Folder_dir_json_wire)
                simpleTest_Folder_dir_csv = os.path.join(test_results_dir_csv, "SimpleTest" + self.driver.name + "/test_show_all_reminders_with_no_reminders_set")
                print(simpleTest_Folder_dir_csv)
                createFolder(simpleTest_Folder_dir_csv)
                simpleTest_Folder_dir_excel = os.path.join(test_results_dir_excel, "SimpleTest" + self.driver.name + "/test_show_all_reminders_with_no_reminders_set")
                print(simpleTest_Folder_dir_excel)
                createFolder(simpleTest_Folder_dir_excel)
                simpleTest_Folder_dir_html = os.path.join(test_results_dir_html, "SimpleTest" + self.driver.name + "/test_show_all_reminders_with_no_reminders_set")
                print(simpleTest_Folder_dir_html)
                createFolder(simpleTest_Folder_dir_html)

                ############## API ##############
                if _data['MITM'] == 'True':
                    print("Get Proxy data as flag is On")
                    _t = c.getJSON("test_greeting", wc.SNIFFHOST)
                    print(_t)
                    if _t == None:
                        print("No Data")
                    else:

                            print("Path")
                            print(_t[0]['path'] )
                            print("Performance Data")
                            print(_t[0]['times'])
                            print(_t[0]['durations'])
                            _requestbody= base64.b64decode(_t[0]['request']['body']['encoded'])
                            print(_requestbody)
                            _responsebody = base64.b64decode(_t[0]['response']['body']['encoded'])
                            print(_responsebody)
                            _temp = _responsebody.decode(errors='replace').split('�')
                            print(_temp)

                    print("Got JSON Data")
                    print("We will perform assertion now")

            except:
                print(traceback.format_exc())

        # Test 5
        def test_clear_all_reminders_with_no_reminders_set(self):
            try:
                counterConversation = 0
                _t = None
                print("Running the Test Open Url")
                if _data['MITM'] == 'True':
                    print("Clearing Cache as flag is True")
                    c.clearCache()
                time.sleep(2)
                ######################### Using Proxy Service ##########################################
                self.driver.delete_all_cookies()
                self.driver.get("https://chatbot-challenge.dev.replicant.ai")

                ################# Get Data from the Proxy for Validation instead of Web #####################
                time.sleep(2)
                parser = self.driver.page_source
                # Two Layers of Validation
                # First Option to get Data Scraped from Web
                # Second Option to get Data from Proxy
                # Third option to get data from Web Socket
                soup = BeautifulSoup(parser, "html.parser")
                pagelinks = soup.find_all('p', {'class': 'MuiTypography-root MuiTypography-body1'})
                #for pagenumber in pagelinks:
                try:
                        # print(pagenumber.text)
                        conversationBuilder[str(counterConversation)] = pagelinks[counterConversation].text
                        ############# Validation Type 1 with the Web #########################
                        assert "Greetings, friend! Type help to get started." in pagelinks[counterConversation].text
                        counterConversation = counterConversation + 1
                except:
                        print("Cannot Collect All the Page")
                        print(traceback.format_exc())

                ################ Now get the data from the MITM Proxy #########
                _t = c.getJSON("test_open_url", wc.SNIFFHOST)
                frameinfo = getframeinfo(currentframe())
                print(frameinfo.filename, frameinfo.lineno)
                print("Performance Data")
                print(_t[0]['response']['body']['text'])
                print(_t[0]['durations'])
                ###################### Validation Layer #####################################################
                _temp = _t[0]['response']['body']['text']
                #############################################################################################
                #############################################################################################
                self.driver.find_element(By.CSS_SELECTOR, ".MuiInputBase-input").click()
                self.driver.find_element(By.CSS_SELECTOR, ".MuiInputBase-input").send_keys("help")
                self.driver.find_element(By.CSS_SELECTOR, ".MuiInputBase-input").send_keys(Keys.ENTER)
                counterConversation = counterConversation + 1
                time.sleep(3)
                ############################ Two Layers of Validation #######################################
                # First Option to get Data Scraped from Web
                # Second Option to get Data from Proxy
                # Third option to get data from Web Socket
                parser = self.driver.page_source
                soup = BeautifulSoup(parser, "html.parser")
                pagelinks = soup.find_all('p', {'class': 'MuiTypography-root MuiTypography-body1'})
                # for pagenumber in pagelinks:
                try:
                    conversationBuilder[str(counterConversation)] = pagelinks[counterConversation].text
                    ############# Validation Type 1 with the Web #########################
                    assert "I am a reminder bot, here to help you get organized. Here are some of the things you can ask me to do" in pagelinks[counterConversation].text
                    counterConversation = counterConversation + 1
                except:
                        print("Cannot Collect All the Page")
                        print(traceback.format_exc())

                ################ Now get the data from the MITM Proxy #########
                _t = c.getJSON("test_open_url", wc.SNIFFHOST)
                frameinfo = getframeinfo(currentframe())
                print(frameinfo.filename, frameinfo.lineno)
                print("Performance Data")
                print(base64.b64decode(_t[0]['response']['body']['encoded']))
                print(_t[0]['durations'])
                ###################### Validation Layer #####################################################
                _temp = base64.b64decode(_t[0]['response']['body']['encoded'])
                #############################################################################################
                self.driver.find_element(By.CSS_SELECTOR, ".MuiInputBase-input").send_keys("clear reminders")
                self.driver.find_element(By.CSS_SELECTOR, ".MuiInputBase-input").send_keys(Keys.ENTER)
                counterConversation = counterConversation + 1
                time.sleep(4)
                ############################ Two Layers of Validation #######################################
                # First Option to get Data Scraped from Web
                # Second Option to get Data from Proxy
                # Third option to get data from Web Socket
                parser = self.driver.page_source
                soup = BeautifulSoup(parser, "html.parser")
                pagelinks = soup.find_all('p', {'class': 'MuiTypography-root MuiTypography-body1'})
                #for pagenumber in pagelinks:
                try:
                    conversationBuilder[str(counterConversation)] = pagelinks[counterConversation].text
                    ############# Validation Type 1 with the Web #########################
                    assert "You have no reminders." in pagelinks[counterConversation].text
                    counterConversation = counterConversation + 1

                except:
                    print("Cannot Collect All the Page")
                    print(traceback.format_exc())

                ################ Now get the data from the MITM Proxy #########
                _t = c.getJSON("test_open_url", wc.SNIFFHOST)
                frameinfo = getframeinfo(currentframe())
                print(frameinfo.filename, frameinfo.lineno)
                print("Performance Data")
                print(base64.b64decode(_t[0]['response']['body']['encoded']))
                print(_t[0]['durations'])
                ###################### Validation Layer #####################################################
                _temp = base64.b64decode(_t[0]['response']['body']['encoded'])

                #############################################################################################
                sleep(2)
                #########################################################
                print("Creating Local Test Folders for Test")
                simpleTest_Folder_dir_json_wire = os.path.join(test_results_dir_json_wire, "SimpleTest" + self.driver.name + "/test_clear_all_reminders_with_no_reminders_set")
                print(simpleTest_Folder_dir_json_wire)
                createFolder(simpleTest_Folder_dir_json_wire)
                simpleTest_Folder_dir_csv = os.path.join(test_results_dir_csv, "SimpleTest" + self.driver.name + "/test_clear_all_reminders_with_no_reminders_set")
                print(simpleTest_Folder_dir_csv)
                createFolder(simpleTest_Folder_dir_csv)
                simpleTest_Folder_dir_excel = os.path.join(test_results_dir_excel, "SimpleTest" + self.driver.name + "/test_clear_all_reminders_with_no_reminders_set")
                print(simpleTest_Folder_dir_excel)
                createFolder(simpleTest_Folder_dir_excel)
                simpleTest_Folder_dir_html = os.path.join(test_results_dir_html, "SimpleTest" + self.driver.name + "/test_clear_all_reminders_with_no_reminders_set")
                print(simpleTest_Folder_dir_html)
                createFolder(simpleTest_Folder_dir_html)

                ############## API ##############
                if _data['MITM'] == 'True':
                    print("Get Proxy data as flag is On")
                    _t = c.getJSON("test_greeting", wc.SNIFFHOST)
                    print(_t)
                    if _t == None:
                        print("No Data")
                    else:

                            print("Path")
                            print(_t[0]['path'] )
                            print("Performance Data")
                            print(_t[0]['times'])
                            print(_t[0]['durations'])
                            _requestbody= base64.b64decode(_t[0]['request']['body']['encoded'])
                            print(_requestbody)
                            _responsebody = base64.b64decode(_t[0]['response']['body']['encoded'])
                            print(_responsebody)
                            _temp = _responsebody.decode(errors='replace').split('�')
                            print(_temp)

                    print("Got JSON Data")
                    print("We will perform assertion now")

            except:
                print(traceback.format_exc())

        #Test 6
        def test_add_a_reminders_with_no_reminders_set(self):
            try:
                counterConversation = 0
                _t = None
                print("Running the Test Open Url")
                if _data['MITM'] == 'True':
                    print("Clearing Cache as flag is True")
                    c.clearCache()
                time.sleep(2)
                ######################### Using Proxy Service ##########################################
                self.driver.delete_all_cookies()
                self.driver.get("https://chatbot-challenge.dev.replicant.ai")

                ################# Get Data from the Proxy for Validation instead of Web #####################
                time.sleep(2)
                parser = self.driver.page_source
                # Two Layers of Validation
                # First Option to get Data Scraped from Web
                # Second Option to get Data from Proxy
                # Third option to get data from Web Socket
                soup = BeautifulSoup(parser, "html.parser")
                pagelinks = soup.find_all('p', {'class': 'MuiTypography-root MuiTypography-body1'})
                #for pagenumber in pagelinks:
                try:
                        # print(pagenumber.text)
                        conversationBuilder[str(counterConversation)] = pagelinks[counterConversation].text
                        ############# Validation Type 1 with the Web #########################
                        assert "Greetings, friend! Type help to get started." in pagelinks[counterConversation].text
                        counterConversation = counterConversation + 1
                except:
                        print("Cannot Collect All the Page")
                        print(traceback.format_exc())

                ################ Now get the data from the MITM Proxy #########
                _t = c.getJSON("test_open_url", wc.SNIFFHOST)
                frameinfo = getframeinfo(currentframe())
                print(frameinfo.filename, frameinfo.lineno)
                print("Performance Data")
                print(_t[0]['response']['body']['text'])
                print(_t[0]['durations'])
                ###################### Validation Layer #####################################################
                _temp = _t[0]['response']['body']['text']
                #############################################################################################
                #############################################################################################
                self.driver.find_element(By.CSS_SELECTOR, ".MuiInputBase-input").click()
                self.driver.find_element(By.CSS_SELECTOR, ".MuiInputBase-input").send_keys("help")
                self.driver.find_element(By.CSS_SELECTOR, ".MuiInputBase-input").send_keys(Keys.ENTER)
                counterConversation = counterConversation + 1
                time.sleep(3)
                ############################ Two Layers of Validation #######################################
                # First Option to get Data Scraped from Web
                # Second Option to get Data from Proxy
                # Third option to get data from Web Socket
                parser = self.driver.page_source
                soup = BeautifulSoup(parser, "html.parser")
                pagelinks = soup.find_all('p', {'class': 'MuiTypography-root MuiTypography-body1'})
                # for pagenumber in pagelinks:
                try:
                    conversationBuilder[str(counterConversation)] = pagelinks[counterConversation].text
                    ############# Validation Type 1 with the Web #########################
                    assert "I am a reminder bot, here to help you get organized. Here are some of the things you can ask me to do" in pagelinks[counterConversation].text
                    counterConversation = counterConversation + 1
                except:
                        print("Cannot Collect All the Page")
                        print(traceback.format_exc())

                ################ Now get the data from the MITM Proxy #########
                _t = c.getJSON("test_open_url", wc.SNIFFHOST)
                frameinfo = getframeinfo(currentframe())
                print(frameinfo.filename, frameinfo.lineno)
                print("Performance Data")
                print(base64.b64decode(_t[0]['response']['body']['encoded']))
                print(_t[0]['durations'])
                ###################### Validation Layer #####################################################
                _temp = base64.b64decode(_t[0]['response']['body']['encoded'])
                #############################################################################################
                self.driver.find_element(By.CSS_SELECTOR, ".MuiInputBase-input").send_keys("remind me to make dinner in 5 minutes.")
                self.driver.find_element(By.CSS_SELECTOR, ".MuiInputBase-input").send_keys(Keys.ENTER)
                counterConversation = counterConversation + 1
                time.sleep(4)
                ############################ Two Layers of Validation #######################################
                # First Option to get Data Scraped from Web
                # Second Option to get Data from Proxy
                # Third option to get data from Web Socket
                parser = self.driver.page_source
                soup = BeautifulSoup(parser, "html.parser")
                pagelinks = soup.find_all('p', {'class': 'MuiTypography-root MuiTypography-body1'})
                #for pagenumber in pagelinks:
                try:

                    conversationBuilder[str(counterConversation)] = pagelinks[counterConversation].text
                    ############# Validation Type 1 with the Web #########################
                    assert "Ok, I will remind you to make dinner in 300 seconds." in pagelinks[counterConversation].text
                    counterConversation = counterConversation + 1

                except:
                        print("Cannot Collect All the Page")
                        print(traceback.format_exc())

                ################ Now get the data from the MITM Proxy #########
                _t = c.getJSON("test_open_url", wc.SNIFFHOST)
                frameinfo = getframeinfo(currentframe())
                print(frameinfo.filename, frameinfo.lineno)
                print("Performance Data")
                print(base64.b64decode(_t[0]['response']['body']['encoded']))
                print(_t[0]['durations'])
                ###################### Validation Layer #####################################################
                _temp = base64.b64decode(_t[0]['response']['body']['encoded'])
                #############################################################################################
                #############################################################################################

                sleep(2)
                #########################################################
                print("Creating Local Test Folders for Test")
                simpleTest_Folder_dir_json_wire = os.path.join(test_results_dir_json_wire, "SimpleTest" + self.driver.name + "/test_greeting")
                print(simpleTest_Folder_dir_json_wire)
                createFolder(simpleTest_Folder_dir_json_wire)
                simpleTest_Folder_dir_csv = os.path.join(test_results_dir_csv, "SimpleTest" + self.driver.name + "/test_greeting")
                print(simpleTest_Folder_dir_csv)
                createFolder(simpleTest_Folder_dir_csv)
                simpleTest_Folder_dir_excel = os.path.join(test_results_dir_excel, "SimpleTest" + self.driver.name + "/test_greeting")
                print(simpleTest_Folder_dir_excel)
                createFolder(simpleTest_Folder_dir_excel)
                simpleTest_Folder_dir_html = os.path.join(test_results_dir_html, "SimpleTest" + self.driver.name + "/test_greeting")
                print(simpleTest_Folder_dir_html)
                createFolder(simpleTest_Folder_dir_html)

                ############## API ##############
                if _data['MITM'] == 'True':
                    print("Get Proxy data as flag is On")
                    _t = c.getJSON("test_greeting", simpleTest_Folder_dir_json_wire)
                    print(_t)
                    if _t == None:
                        print("No Data")
                    else:

                            print("Path")
                            print(_t[0]['path'] )
                            print("Performance Data")
                            print(_t[0]['times'])
                            print(_t[0]['durations'])
                            _requestbody= base64.b64decode(_t[0]['request']['body']['encoded'])
                            print(_requestbody)
                            _responsebody = base64.b64decode(_t[0]['response']['body']['encoded'])
                            print(_responsebody)
                            _temp = _responsebody.decode(errors='replace').split('�')
                            print(_temp)

                    print("Got JSON Data")
                    print("We will perform assertion now")

            except:
                print(traceback.format_exc())

        #Test 7
        def test_list_reminders_with_one_reminders_set(self):
            try:
                counterConversation = 0
                _t = None
                print("Running the Test Open Url")
                if _data['MITM'] == 'True':
                    print("Clearing Cache as flag is True")
                    c.clearCache()
                time.sleep(2)
                ######################### Using Proxy Service ##########################################
                self.driver.delete_all_cookies()
                self.driver.get("https://chatbot-challenge.dev.replicant.ai")

                ################# Get Data from the Proxy for Validation instead of Web #####################
                time.sleep(2)
                parser = self.driver.page_source
                # Two Layers of Validation
                # First Option to get Data Scraped from Web
                # Second Option to get Data from Proxy
                # Third option to get data from Web Socket
                soup = BeautifulSoup(parser, "html.parser")
                pagelinks = soup.find_all('p', {'class': 'MuiTypography-root MuiTypography-body1'})
                #for pagenumber in pagelinks:
                try:
                        # print(pagenumber.text)
                        conversationBuilder[str(counterConversation)] = pagelinks[counterConversation].text
                        ############# Validation Type 1 with the Web #########################
                        assert "Greetings, friend! Type help to get started." in pagelinks[counterConversation].text
                        counterConversation = counterConversation + 1
                except:
                        print("Cannot Collect All the Page")
                        print(traceback.format_exc())

                ################ Now get the data from the MITM Proxy #########
                _t = c.getJSON("test_open_url", wc.SNIFFHOST)
                frameinfo = getframeinfo(currentframe())
                print(frameinfo.filename, frameinfo.lineno)
                print("Performance Data")
                print(_t[0]['response']['body']['text'])
                print(_t[0]['durations'])
                ###################### Validation Layer #####################################################
                _temp = _t[0]['response']['body']['text']
                #############################################################################################
                #############################################################################################
                self.driver.find_element(By.CSS_SELECTOR, ".MuiInputBase-input").click()
                self.driver.find_element(By.CSS_SELECTOR, ".MuiInputBase-input").send_keys("help")
                self.driver.find_element(By.CSS_SELECTOR, ".MuiInputBase-input").send_keys(Keys.ENTER)
                counterConversation = counterConversation + 1
                time.sleep(3)
                ############################ Two Layers of Validation #######################################
                # First Option to get Data Scraped from Web
                # Second Option to get Data from Proxy
                # Third option to get data from Web Socket
                parser = self.driver.page_source
                soup = BeautifulSoup(parser, "html.parser")
                pagelinks = soup.find_all('p', {'class': 'MuiTypography-root MuiTypography-body1'})
                # for pagenumber in pagelinks:
                try:
                    conversationBuilder[str(counterConversation)] = pagelinks[counterConversation].text
                    ############# Validation Type 1 with the Web #########################
                    assert "I am a reminder bot, here to help you get organized. Here are some of the things you can ask me to do" in pagelinks[counterConversation].text
                    counterConversation = counterConversation + 1
                except:
                        print("Cannot Collect All the Page")
                        print(traceback.format_exc())

                ################ Now get the data from the MITM Proxy #########
                _t = c.getJSON("test_open_url", wc.SNIFFHOST)
                frameinfo = getframeinfo(currentframe())
                print(frameinfo.filename, frameinfo.lineno)
                print("Performance Data")
                print(base64.b64decode(_t[0]['response']['body']['encoded']))
                print(_t[0]['durations'])
                ###################### Validation Layer #####################################################
                _temp = base64.b64decode(_t[0]['response']['body']['encoded'])
                #############################################################################################
                self.driver.find_element(By.CSS_SELECTOR, ".MuiInputBase-input").send_keys("remind me to make dinner in 5 minutes.")
                self.driver.find_element(By.CSS_SELECTOR, ".MuiInputBase-input").send_keys(Keys.ENTER)
                counterConversation = counterConversation + 1
                time.sleep(4)
                ############################ Two Layers of Validation #######################################
                # First Option to get Data Scraped from Web
                # Second Option to get Data from Proxy
                # Third option to get data from Web Socket
                parser = self.driver.page_source
                soup = BeautifulSoup(parser, "html.parser")
                pagelinks = soup.find_all('p', {'class': 'MuiTypography-root MuiTypography-body1'})
                #for pagenumber in pagelinks:
                try:

                    conversationBuilder[str(counterConversation)] = pagelinks[counterConversation].text
                    ############# Validation Type 1 with the Web #########################
                    assert "Ok, I will remind you to make dinner in 300 seconds." in pagelinks[counterConversation].text
                    counterConversation = counterConversation + 1

                except:
                        print("Cannot Collect All the Page")
                        print(traceback.format_exc())

                ################ Now get the data from the MITM Proxy #########
                _t = c.getJSON("test_open_url", wc.SNIFFHOST)
                frameinfo = getframeinfo(currentframe())
                print(frameinfo.filename, frameinfo.lineno)
                print("Performance Data")
                print(base64.b64decode(_t[0]['response']['body']['encoded']))
                print(_t[0]['durations'])
                ###################### Validation Layer #####################################################
                _temp = base64.b64decode(_t[0]['response']['body']['encoded'])
                #############################################################################################
                #############################################################################################
                self.driver.find_element(By.CSS_SELECTOR, ".MuiInputBase-input").send_keys("show all reminders")
                self.driver.find_element(By.CSS_SELECTOR, ".MuiInputBase-input").send_keys(Keys.ENTER)
                counterConversation = counterConversation + 1
                time.sleep(3)
                ############################ Two Layers of Validation #######################################
                # First Option to get Data Scraped from Web
                # Second Option to get Data from Proxy
                # Third option to get data from Web Socket
                parser = self.driver.page_source
                soup = BeautifulSoup(parser, "html.parser")
                pagelinks = soup.find_all('p', {'class': 'MuiTypography-root MuiTypography-body1'})
                #for pagenumber in pagelinks:

                try:
                        conversationBuilder[str(counterConversation)] = pagelinks[counterConversation].text
                        ############# Validation Type 1 with the Web #########################
                        assert "make dinner" in pagelinks[counterConversation].text
                        counterConversation = counterConversation + 1

                except:
                        print("Cannot Collect All the Page")
                        print(traceback.format_exc())

                ################ Now get the data from the MITM Proxy #########
                _t = c.getJSON("test_open_url", wc.SNIFFHOST)
                frameinfo = getframeinfo(currentframe())
                print(frameinfo.filename, frameinfo.lineno)
                print("Performance Data")
                print(base64.b64decode(_t[0]['response']['body']['encoded']))
                print(_t[0]['durations'])
                ###################### Validation Layer #####################################################
                _temp = base64.b64decode(_t[0]['response']['body']['encoded'])
                #############################################################################################

                sleep(2)
                #########################################################
                print("Creating Local Test Folders for Test")
                simpleTest_Folder_dir_json_wire = os.path.join(test_results_dir_json_wire, "SimpleTest" + self.driver.name + "/test_greeting")
                print(simpleTest_Folder_dir_json_wire)
                createFolder(simpleTest_Folder_dir_json_wire)
                simpleTest_Folder_dir_csv = os.path.join(test_results_dir_csv, "SimpleTest" + self.driver.name + "/test_list_reminders_with_one_reminders_set")
                print(simpleTest_Folder_dir_csv)
                createFolder(simpleTest_Folder_dir_csv)
                simpleTest_Folder_dir_excel = os.path.join(test_results_dir_excel, "SimpleTest" + self.driver.name + "/test_list_reminders_with_one_reminders_set")
                print(simpleTest_Folder_dir_excel)
                createFolder(simpleTest_Folder_dir_excel)
                simpleTest_Folder_dir_html = os.path.join(test_results_dir_html, "SimpleTest" + self.driver.name + "/test_list_reminders_with_one_reminders_set")
                print(simpleTest_Folder_dir_html)
                createFolder(simpleTest_Folder_dir_html)

                ############## API ##############
                if _data['MITM'] == 'True':
                    print("Get Proxy data as flag is On")
                    _t = c.getJSON("test_greeting", simpleTest_Folder_dir_json_wire)
                    print(_t)
                    if _t == None:
                        print("No Data")
                    else:

                            print("Path")
                            print(_t[0]['path'] )
                            print("Performance Data")
                            print(_t[0]['times'])
                            print(_t[0]['durations'])
                            _requestbody= base64.b64decode(_t[0]['request']['body']['encoded'])
                            print(_requestbody)
                            _responsebody = base64.b64decode(_t[0]['response']['body']['encoded'])
                            print(_responsebody)
                            _temp = _responsebody.decode(errors='replace').split('�')
                            print(_temp)


                    print("Got JSON Data")
                    print("We will perform assertion now")

            except:
                print(traceback.format_exc())

        # Test 8
        def test_list_reminders_with_two_reminders_set(self):
            try:
                counterConversation = 0
                _t = None
                print("Running the Test Open Url")
                if _data['MITM'] == 'True':
                    print("Clearing Cache as flag is True")
                    c.clearCache()
                time.sleep(2)
                ######################### Using Proxy Service ##########################################
                self.driver.delete_all_cookies()
                self.driver.get("https://chatbot-challenge.dev.replicant.ai")

                ################# Get Data from the Proxy for Validation instead of Web #####################
                time.sleep(2)
                parser = self.driver.page_source
                # Two Layers of Validation
                # First Option to get Data Scraped from Web
                # Second Option to get Data from Proxy
                # Third option to get data from Web Socket
                soup = BeautifulSoup(parser, "html.parser")
                pagelinks = soup.find_all('p', {'class': 'MuiTypography-root MuiTypography-body1'})
                #for pagenumber in pagelinks:
                try:
                        # print(pagenumber.text)
                        conversationBuilder[str(counterConversation)] = pagelinks[counterConversation].text
                        ############# Validation Type 1 with the Web #########################
                        assert "Greetings, friend! Type help to get started." in pagelinks[counterConversation].text
                        counterConversation = counterConversation + 1
                except:
                        print("Cannot Collect All the Page")
                        print(traceback.format_exc())

                ################ Now get the data from the MITM Proxy #########
                _t = c.getJSON("test_open_url", wc.SNIFFHOST)
                frameinfo = getframeinfo(currentframe())
                print(frameinfo.filename, frameinfo.lineno)
                print("Performance Data")
                print(_t[0]['response']['body']['text'])
                print(_t[0]['durations'])
                ###################### Validation Layer #####################################################
                _temp = _t[0]['response']['body']['text']
                #############################################################################################
                #############################################################################################
                self.driver.find_element(By.CSS_SELECTOR, ".MuiInputBase-input").click()
                self.driver.find_element(By.CSS_SELECTOR, ".MuiInputBase-input").send_keys("help")
                self.driver.find_element(By.CSS_SELECTOR, ".MuiInputBase-input").send_keys(Keys.ENTER)
                counterConversation = counterConversation + 1
                time.sleep(3)
                ############################ Two Layers of Validation #######################################
                # First Option to get Data Scraped from Web
                # Second Option to get Data from Proxy
                # Third option to get data from Web Socket
                parser = self.driver.page_source
                soup = BeautifulSoup(parser, "html.parser")
                pagelinks = soup.find_all('p', {'class': 'MuiTypography-root MuiTypography-body1'})
                # for pagenumber in pagelinks:
                try:
                    conversationBuilder[str(counterConversation)] = pagelinks[counterConversation].text
                    ############# Validation Type 1 with the Web #########################
                    assert "I am a reminder bot, here to help you get organized. Here are some of the things you can ask me to do" in pagelinks[counterConversation].text
                    counterConversation = counterConversation + 1
                except:
                        print("Cannot Collect All the Page")
                        print(traceback.format_exc())

                ################ Now get the data from the MITM Proxy #########
                _t = c.getJSON("test_open_url", wc.SNIFFHOST)
                frameinfo = getframeinfo(currentframe())
                print(frameinfo.filename, frameinfo.lineno)
                print("Performance Data")
                print(base64.b64decode(_t[0]['response']['body']['encoded']))
                print(_t[0]['durations'])
                ###################### Validation Layer #####################################################
                _temp = base64.b64decode(_t[0]['response']['body']['encoded'])
                #############################################################################################
                self.driver.find_element(By.CSS_SELECTOR, ".MuiInputBase-input").send_keys("remind me to make dinner in 5 minutes.")
                self.driver.find_element(By.CSS_SELECTOR, ".MuiInputBase-input").send_keys(Keys.ENTER)
                counterConversation = counterConversation + 1
                time.sleep(4)
                ############################ Two Layers of Validation #######################################
                # First Option to get Data Scraped from Web
                # Second Option to get Data from Proxy
                # Third option to get data from Web Socket
                parser = self.driver.page_source
                soup = BeautifulSoup(parser, "html.parser")
                pagelinks = soup.find_all('p', {'class': 'MuiTypography-root MuiTypography-body1'})
                #for pagenumber in pagelinks:
                try:
                        conversationBuilder[str(counterConversation)] = pagelinks[counterConversation].text
                        assert "Ok, I will remind you to make dinner in 300 seconds." in pagelinks[counterConversation].text
                        counterConversation = counterConversation + 1
                        # conversationBuilder[str(counterConversation)] = pagenumber.text

                except:
                        print("Cannot Collect All the Page")
                        print(traceback.format_exc())

                ################ Now get the data from the MITM Proxy #########
                _t = c.getJSON("test_open_url", wc.SNIFFHOST)
                frameinfo = getframeinfo(currentframe())
                print(frameinfo.filename, frameinfo.lineno)
                print("Performance Data")
                print(base64.b64decode(_t[0]['response']['body']['encoded']))
                print(_t[0]['durations'])
                ###################### Validation Layer #####################################################
                _temp = base64.b64decode(_t[0]['response']['body']['encoded'])
                #############################################################################################
                #############################################################################################
                self.driver.find_element(By.CSS_SELECTOR, ".MuiInputBase-input").send_keys("remind me to take out trash in 20 minutes.")
                self.driver.find_element(By.CSS_SELECTOR, ".MuiInputBase-input").send_keys(Keys.ENTER)
                counterConversation = counterConversation + 1
                time.sleep(3)
                ############################ Two Layers of Validation #######################################
                # First Option to get Data Scraped from Web
                # Second Option to get Data from Proxy
                # Third option to get data from Web Socket
                parser = self.driver.page_source
                soup = BeautifulSoup(parser, "html.parser")
                pagelinks = soup.find_all('p', {'class': 'MuiTypography-root MuiTypography-body1'})
                try:
                    conversationBuilder[str(counterConversation)] = pagelinks[counterConversation].text
                    assert "Ok, I will remind you to take out trash in 1200 seconds." in pagelinks[counterConversation].text
                    counterConversation = counterConversation + 1
                    # conversationBuilder[str(counterConversation)] = pagenumber.text

                except:
                    print("Cannot Collect All the Page")
                    print(traceback.format_exc())

                ################ Now get the data from the MITM Proxy #########
                _t = c.getJSON("test_open_url", wc.SNIFFHOST)
                frameinfo = getframeinfo(currentframe())
                print(frameinfo.filename, frameinfo.lineno)
                print("Performance Data")
                print(base64.b64decode(_t[0]['response']['body']['encoded']))
                print(_t[0]['durations'])
                ###################### Validation Layer #####################################################
                _temp = base64.b64decode(_t[0]['response']['body']['encoded'])
                #############################################################################################
                #############################################################################################
                self.driver.find_element(By.CSS_SELECTOR, ".MuiInputBase-input").send_keys("show all reminders")
                self.driver.find_element(By.CSS_SELECTOR, ".MuiInputBase-input").send_keys(Keys.ENTER)
                counterConversation = counterConversation + 1
                ################# Get Data from the Proxy for Validation instead of Web #####################
                time.sleep(3)
                ############################ Two Layers of Validation #######################################
                # First Option to get Data Scraped from Web
                # Second Option to get Data from Proxy
                # Third option to get data from Web Socket
                parser = self.driver.page_source
                soup = BeautifulSoup(parser, "html.parser")
                pagelinks = soup.find_all('p', {'class': 'MuiTypography-root MuiTypography-body1'})
                try:
                    conversationBuilder[str(counterConversation)] = pagelinks[counterConversation].text
                    assert "make dinner" in pagelinks[counterConversation].text
                    assert "take out trash" in pagelinks[counterConversation].text
                    counterConversation = counterConversation + 1
                    # conversationBuilder[str(counterConversation)] = pagenumber.text

                except:
                    print("Cannot Collect All the Page")
                    print(traceback.format_exc())
                ################ Now get the data from the MITM Proxy #########
                _t = c.getJSON("test_open_url", wc.SNIFFHOST)
                frameinfo = getframeinfo(currentframe())
                print(frameinfo.filename, frameinfo.lineno)
                print("Performance Data")
                print(base64.b64decode(_t[0]['response']['body']['encoded']))
                print(_t[0]['durations'])
                ###################### Validation Layer #####################################################
                _temp = base64.b64decode(_t[0]['response']['body']['encoded'])
                #############################################################################################

                time.sleep(2)

                #########################################################
                print("Creating Local Test Folders for Test")
                simpleTest_Folder_dir_json_wire = os.path.join(test_results_dir_json_wire, "SimpleTest" + self.driver.name + "/test_list_reminders_with_two_reminders_set")
                print(simpleTest_Folder_dir_json_wire)
                createFolder(simpleTest_Folder_dir_json_wire)
                simpleTest_Folder_dir_csv = os.path.join(test_results_dir_csv, "SimpleTest" + self.driver.name + "/test_list_reminders_with_two_reminders_set")
                print(simpleTest_Folder_dir_csv)
                createFolder(simpleTest_Folder_dir_csv)
                simpleTest_Folder_dir_excel = os.path.join(test_results_dir_excel, "SimpleTest" + self.driver.name + "/test_list_reminders_with_two_reminders_set")
                print(simpleTest_Folder_dir_excel)
                createFolder(simpleTest_Folder_dir_excel)
                simpleTest_Folder_dir_html = os.path.join(test_results_dir_html, "SimpleTest" + self.driver.name + "/test_list_reminders_with_two_reminders_set")
                print(simpleTest_Folder_dir_html)
                createFolder(simpleTest_Folder_dir_html)

                ############## API ##############
                if _data['MITM'] == 'True':
                    print("Get Proxy data as flag is On")
                    _t = c.getJSON("test_greeting", simpleTest_Folder_dir_json_wire)
                    print(_t)
                    if _t == None:
                        print("No Data")
                    else:

                            print("Path")
                            print(_t[0]['path'] )
                            print("Performance Data")
                            print(_t[0]['times'])
                            print(_t[0]['durations'])
                            _requestbody= base64.b64decode(_t[0]['request']['body']['encoded'])
                            print(_requestbody)
                            _responsebody = base64.b64decode(_t[0]['response']['body']['encoded'])
                            print(_responsebody)
                            _temp = _responsebody.decode(errors='replace').split('�')
                            print(_temp)

                    print("Got JSON Data")
                    print("We will perform assertion now")

            except:
                print(traceback.format_exc())

        # # Test 9
        def test_reminder_time_after_sleep_with_one_reminders(self):
            try:
                counterConversation = 0
                _t = None
                print("Running the Test Open Url")
                if _data['MITM'] == 'True':
                    print("Clearing Cache as flag is True")
                    c.clearCache()
                time.sleep(2)
                ######################### Using Proxy Service ##########################################
                self.driver.delete_all_cookies()
                self.driver.get("https://chatbot-challenge.dev.replicant.ai")

                ################# Get Data from the Proxy for Validation instead of Web #####################
                time.sleep(2)
                parser = self.driver.page_source
                # Two Layers of Validation
                # First Option to get Data Scraped from Web
                # Second Option to get Data from Proxy
                # Third option to get data from Web Socket
                soup = BeautifulSoup(parser, "html.parser")
                pagelinks = soup.find_all('p', {'class': 'MuiTypography-root MuiTypography-body1'})
                #for pagenumber in pagelinks:
                try:
                        # print(pagenumber.text)
                        conversationBuilder[str(counterConversation)] = pagelinks[counterConversation].text
                        ############# Validation Type 1 with the Web #########################
                        assert "Greetings, friend! Type help to get started." in pagelinks[counterConversation].text
                        counterConversation = counterConversation + 1
                except:
                        print("Cannot Collect All the Page")
                        print(traceback.format_exc())

                ################ Now get the data from the MITM Proxy #########
                _t = c.getJSON("test_open_url", wc.SNIFFHOST)
                frameinfo = getframeinfo(currentframe())
                print(frameinfo.filename, frameinfo.lineno)
                print("Performance Data")
                print(_t[0]['response']['body']['text'])
                print(_t[0]['durations'])
                ###################### Validation Layer #####################################################
                _temp = _t[0]['response']['body']['text']
                #############################################################################################
                #############################################################################################
                self.driver.find_element(By.CSS_SELECTOR, ".MuiInputBase-input").click()
                self.driver.find_element(By.CSS_SELECTOR, ".MuiInputBase-input").send_keys("help")
                self.driver.find_element(By.CSS_SELECTOR, ".MuiInputBase-input").send_keys(Keys.ENTER)
                counterConversation = counterConversation + 1
                time.sleep(3)
                ############################ Two Layers of Validation #######################################
                # First Option to get Data Scraped from Web
                # Second Option to get Data from Proxy
                # Third option to get data from Web Socket
                parser = self.driver.page_source
                soup = BeautifulSoup(parser, "html.parser")
                pagelinks = soup.find_all('p', {'class': 'MuiTypography-root MuiTypography-body1'})
                try:
                    conversationBuilder[str(counterConversation)] = pagelinks[counterConversation].text
                    ############# Validation Type 1 with the Web #########################
                    assert "I am a reminder bot, here to help you get organized. Here are some of the things you can ask me to do" in pagelinks[counterConversation].text
                    counterConversation = counterConversation + 1
                except:
                        print("Cannot Collect All the Page")
                        print(traceback.format_exc())

                ################ Now get the data from the MITM Proxy #########
                _t = c.getJSON("test_open_url", wc.SNIFFHOST)
                frameinfo = getframeinfo(currentframe())
                print(frameinfo.filename, frameinfo.lineno)
                print("Performance Data")
                print(base64.b64decode(_t[0]['response']['body']['encoded']))
                print(_t[0]['durations'])
                ###################### Validation Layer #####################################################
                _temp = base64.b64decode(_t[0]['response']['body']['encoded'])
                #############################################################################################
                self.driver.find_element(By.CSS_SELECTOR, ".MuiInputBase-input").send_keys("remind me to make dinner in 5 minutes.")
                self.driver.find_element(By.CSS_SELECTOR, ".MuiInputBase-input").send_keys(Keys.ENTER)
                counterConversation = counterConversation + 1
                time.sleep(4)
                ############################ Two Layers of Validation #######################################
                # First Option to get Data Scraped from Web
                # Second Option to get Data from Proxy
                # Third option to get data from Web Socket
                parser = self.driver.page_source
                soup = BeautifulSoup(parser, "html.parser")
                pagelinks = soup.find_all('p', {'class': 'MuiTypography-root MuiTypography-body1'})
                #for pagenumber in pagelinks:
                try:
                    # print(pagenumber.text)
                    conversationBuilder[str(counterConversation)] = pagelinks[counterConversation].text
                    ############# Validation Type 1 with the Web #########################
                    assert "Ok, I will remind you to make dinner in 300 seconds." in pagelinks[counterConversation].text
                    counterConversation = counterConversation + 1
                except:
                    print("Cannot Collect All the Page")
                    print(traceback.format_exc())

                ################ Now get the data from the MITM Proxy #########
                _t = c.getJSON("test_open_url", wc.SNIFFHOST)
                frameinfo = getframeinfo(currentframe())
                print(frameinfo.filename, frameinfo.lineno)
                print("Performance Data")
                print(base64.b64decode(_t[0]['response']['body']['encoded']))
                print(_t[0]['durations'])
                ###################### Validation Layer #####################################################
                _temp = base64.b64decode(_t[0]['response']['body']['encoded'])
                #############################################################################################
                time.sleep(60)
                #############################################################################################
                self.driver.find_element(By.CSS_SELECTOR, ".MuiInputBase-input").send_keys("show all reminders")
                self.driver.find_element(By.CSS_SELECTOR, ".MuiInputBase-input").send_keys(Keys.ENTER)
                counterConversation = counterConversation + 1
                time.sleep(3)
                ############################ Two Layers of Validation #######################################
                # First Option to get Data Scraped from Web
                # Second Option to get Data from Proxy
                # Third option to get data from Web Socket
                parser = self.driver.page_source
                soup = BeautifulSoup(parser, "html.parser")
                pagelinks = soup.find_all('p', {'class': 'MuiTypography-root MuiTypography-body1'})
                try:
                    # print(pagenumber.text)
                    conversationBuilder[str(counterConversation)] = pagelinks[counterConversation].text
                    ############# Validation Type 1 with the Web #########################
                    assert "make dinner" in pagelinks[counterConversation].text
                    # We will not match the exact time as we have to wait for some time to stablize web
                    assert "seconds remaining" in pagelinks[counterConversation].text
                    counterConversation = counterConversation + 1
                except:
                    print("Cannot Collect All the Page")
                    print(traceback.format_exc())

                ################ Now get the data from the MITM Proxy #########
                _t = c.getJSON("test_open_url", wc.SNIFFHOST)
                frameinfo = getframeinfo(currentframe())
                print(frameinfo.filename, frameinfo.lineno)
                print("Performance Data")
                print(base64.b64decode(_t[0]['response']['body']['encoded']))
                print(_t[0]['durations'])
                ###################### Validation Layer #####################################################
                _temp = base64.b64decode(_t[0]['response']['body']['encoded'])
                #############################################################################################

                #########################################################
                print("Creating Local Test Folders for Test")
                simpleTest_Folder_dir_json_wire = os.path.join(test_results_dir_json_wire, "SimpleTest" + self.driver.name + "/test_reminder_time_after_sleep_with_one_reminders")
                print(simpleTest_Folder_dir_json_wire)
                createFolder(simpleTest_Folder_dir_json_wire)
                simpleTest_Folder_dir_csv = os.path.join(test_results_dir_csv, "SimpleTest" + self.driver.name + "/test_reminder_time_after_sleep_with_one_reminders")
                print(simpleTest_Folder_dir_csv)
                createFolder(simpleTest_Folder_dir_csv)
                simpleTest_Folder_dir_excel = os.path.join(test_results_dir_excel, "SimpleTest" + self.driver.name + "/test_reminder_time_after_sleep_with_one_reminders")
                print(simpleTest_Folder_dir_excel)
                createFolder(simpleTest_Folder_dir_excel)
                simpleTest_Folder_dir_html = os.path.join(test_results_dir_html, "SimpleTest" + self.driver.name + "/test_reminder_time_after_sleep_with_one_reminders")
                print(simpleTest_Folder_dir_html)
                createFolder(simpleTest_Folder_dir_html)

                ############## API ##############
                if _data['MITM'] == 'True':
                    print("Get Proxy data as flag is On")
                    _t = c.getJSON("test_greeting", simpleTest_Folder_dir_json_wire)
                    print(_t)
                    if _t == None:
                        print("No Data")
                    else:

                            print("Path")
                            print(_t[0]['path'] )
                            print("Performance Data")
                            print(_t[0]['times'])
                            print(_t[0]['durations'])
                            _requestbody= base64.b64decode(_t[0]['request']['body']['encoded'])
                            print(_requestbody)
                            _responsebody = base64.b64decode(_t[0]['response']['body']['encoded'])
                            print(_responsebody)
                            _temp = _responsebody.decode(errors='replace').split('�')
                            print(_temp)


                    print("Got JSON Data")
                    print("We will perform assertion now")

            except:
                print(traceback.format_exc())

        # # Test 10
        def test_remove_list_reminders_with_two_reminders_set(self):
            try:
                counterConversation = 0
                _t = None
                print("Running the Test Open Url")
                if _data['MITM'] == 'True':
                    print("Clearing Cache as flag is True")
                    c.clearCache()
                time.sleep(2)
                ######################### Using Proxy Service ##########################################
                self.driver.delete_all_cookies()
                self.driver.get("https://chatbot-challenge.dev.replicant.ai")

                ################# Get Data from the Proxy for Validation instead of Web #####################
                time.sleep(2)
                parser = self.driver.page_source
                # Two Layers of Validation
                # First Option to get Data Scraped from Web
                # Second Option to get Data from Proxy
                # Third option to get data from Web Socket
                soup = BeautifulSoup(parser, "html.parser")
                pagelinks = soup.find_all('p', {'class': 'MuiTypography-root MuiTypography-body1'})
                #for pagenumber in pagelinks:
                try:
                        # print(pagenumber.text)
                        conversationBuilder[str(counterConversation)] = pagelinks[counterConversation].text
                        ############# Validation Type 1 with the Web #########################
                        assert "Greetings, friend! Type help to get started." in pagelinks[counterConversation].text
                        counterConversation = counterConversation + 1
                except:
                        print("Cannot Collect All the Page")
                        print(traceback.format_exc())

                ################ Now get the data from the MITM Proxy #########
                _t = c.getJSON("test_open_url", wc.SNIFFHOST)
                frameinfo = getframeinfo(currentframe())
                print(frameinfo.filename, frameinfo.lineno)
                print("Performance Data")
                print(_t[0]['response']['body']['text'])
                print(_t[0]['durations'])
                ###################### Validation Layer #####################################################
                _temp = _t[0]['response']['body']['text']
                #############################################################################################
                #############################################################################################
                self.driver.find_element(By.CSS_SELECTOR, ".MuiInputBase-input").click()
                self.driver.find_element(By.CSS_SELECTOR, ".MuiInputBase-input").send_keys("help")
                self.driver.find_element(By.CSS_SELECTOR, ".MuiInputBase-input").send_keys(Keys.ENTER)
                counterConversation = counterConversation + 1
                time.sleep(3)
                ############################ Two Layers of Validation #######################################
                # First Option to get Data Scraped from Web
                # Second Option to get Data from Proxy
                # Third option to get data from Web Socket
                parser = self.driver.page_source
                soup = BeautifulSoup(parser, "html.parser")
                pagelinks = soup.find_all('p', {'class': 'MuiTypography-root MuiTypography-body1'})
                # for pagenumber in pagelinks:
                try:
                    conversationBuilder[str(counterConversation)] = pagelinks[counterConversation].text
                    ############# Validation Type 1 with the Web #########################
                    assert "I am a reminder bot, here to help you get organized. Here are some of the things you can ask me to do" in pagelinks[counterConversation].text
                    counterConversation = counterConversation + 1
                except:
                        print("Cannot Collect All the Page")
                        print(traceback.format_exc())

                ################ Now get the data from the MITM Proxy #########
                _t = c.getJSON("test_open_url", wc.SNIFFHOST)
                frameinfo = getframeinfo(currentframe())
                print(frameinfo.filename, frameinfo.lineno)
                print("Performance Data")
                print(base64.b64decode(_t[0]['response']['body']['encoded']))
                print(_t[0]['durations'])
                ###################### Validation Layer #####################################################
                _temp = base64.b64decode(_t[0]['response']['body']['encoded'])
                #############################################################################################
                self.driver.find_element(By.CSS_SELECTOR, ".MuiInputBase-input").send_keys("remind me to make dinner in 5 minutes.")
                self.driver.find_element(By.CSS_SELECTOR, ".MuiInputBase-input").send_keys(Keys.ENTER)
                counterConversation = counterConversation + 1
                time.sleep(4)
                ############################ Two Layers of Validation #######################################
                # First Option to get Data Scraped from Web
                # Second Option to get Data from Proxy
                # Third option to get data from Web Socket
                parser = self.driver.page_source
                soup = BeautifulSoup(parser, "html.parser")
                pagelinks = soup.find_all('p', {'class': 'MuiTypography-root MuiTypography-body1'})
                #for pagenumber in pagelinks:
                try:
                    conversationBuilder[str(counterConversation)] = pagelinks[counterConversation].text
                    ############# Validation Type 1 with the Web #########################
                    assert "Ok, I will remind you to make dinner in 300 seconds." in pagelinks[counterConversation].text
                    counterConversation = counterConversation + 1
                except:
                    print("Cannot Collect All the Page")
                    print(traceback.format_exc())
                ################ Now get the data from the MITM Proxy #########
                _t = c.getJSON("test_open_url", wc.SNIFFHOST)
                frameinfo = getframeinfo(currentframe())
                print(frameinfo.filename, frameinfo.lineno)
                print("Performance Data")
                print(base64.b64decode(_t[0]['response']['body']['encoded']))
                print(_t[0]['durations'])
                ###################### Validation Layer #####################################################
                _temp = base64.b64decode(_t[0]['response']['body']['encoded'])
                #############################################################################################
                #############################################################################################
                self.driver.find_element(By.CSS_SELECTOR, ".MuiInputBase-input").send_keys("remind me to take out trash in 20 minutes.")
                self.driver.find_element(By.CSS_SELECTOR, ".MuiInputBase-input").send_keys(Keys.ENTER)
                counterConversation = counterConversation + 1
                time.sleep(3)
                ############################ Two Layers of Validation #######################################
                # First Option to get Data Scraped from Web
                # Second Option to get Data from Proxy
                # Third option to get data from Web Socket
                parser = self.driver.page_source
                soup = BeautifulSoup(parser, "html.parser")
                pagelinks = soup.find_all('p', {'class': 'MuiTypography-root MuiTypography-body1'})
                try:
                    conversationBuilder[str(counterConversation)] = pagelinks[counterConversation].text
                    ############# Validation Type 1 with the Web #########################
                    assert "Ok, I will remind you to take out trash in 1200 seconds." in pagelinks[counterConversation].text
                    counterConversation = counterConversation + 1
                except:
                    print("Cannot Collect All the Page")
                    print(traceback.format_exc())

                ################ Now get the data from the MITM Proxy #########
                _t = c.getJSON("test_open_url", wc.SNIFFHOST)
                frameinfo = getframeinfo(currentframe())
                print(frameinfo.filename, frameinfo.lineno)
                print("Performance Data")
                print(base64.b64decode(_t[0]['response']['body']['encoded']))
                print(_t[0]['durations'])
                ###################### Validation Layer #####################################################
                _temp = base64.b64decode(_t[0]['response']['body']['encoded'])
                #############################################################################################
                #############################################################################################
                self.driver.find_element(By.CSS_SELECTOR, ".MuiInputBase-input").send_keys("show all reminders")
                self.driver.find_element(By.CSS_SELECTOR, ".MuiInputBase-input").send_keys(Keys.ENTER)
                counterConversation = counterConversation + 1
                ################# Get Data from the Proxy for Validation instead of Web #####################
                time.sleep(3)
                ############################ Two Layers of Validation #######################################
                # First Option to get Data Scraped from Web
                # Second Option to get Data from Proxy
                # Third option to get data from Web Socket
                parser = self.driver.page_source
                soup = BeautifulSoup(parser, "html.parser")
                pagelinks = soup.find_all('p', {'class': 'MuiTypography-root MuiTypography-body1'})
                try:
                    conversationBuilder[str(counterConversation)] = pagelinks[counterConversation].text
                    ############# Validation Type 1 with the Web #########################
                    assert "make dinner" in pagelinks[counterConversation].text
                    assert "take out trash" in pagelinks[counterConversation].text
                    counterConversation = counterConversation + 1
                except:
                    print("Cannot Collect All the Page")
                    print(traceback.format_exc())

                ################ Now get the data from the MITM Proxy #########
                _t = c.getJSON("test_open_url", wc.SNIFFHOST)
                frameinfo = getframeinfo(currentframe())
                print(frameinfo.filename, frameinfo.lineno)
                print("Performance Data")
                print(base64.b64decode(_t[0]['response']['body']['encoded']))
                print(_t[0]['durations'])
                ###################### Validation Layer #####################################################
                _temp = base64.b64decode(_t[0]['response']['body']['encoded'])
                #############################################################################################
                #############################################################################################
                self.driver.find_element(By.CSS_SELECTOR, ".MuiInputBase-input").send_keys("clear reminder 2")
                self.driver.find_element(By.CSS_SELECTOR, ".MuiInputBase-input").send_keys(Keys.ENTER)
                counterConversation = counterConversation + 1
                ################# Get Data from the Proxy for Validation instead of Web #####################
                time.sleep(2)
                ############################ Two Layers of Validation #######################################
                # First Option to get Data Scraped from Web
                # Second Option to get Data from Proxy
                # Third option to get data from Web Socket
                parser = self.driver.page_source
                soup = BeautifulSoup(parser, "html.parser")
                pagelinks = soup.find_all('p', {'class': 'MuiTypography-root MuiTypography-body1'})
                try:
                    conversationBuilder[str(counterConversation)] = pagelinks[counterConversation].text
                    ############# Validation Type 1 with the Web #########################
                    assert "Ok, I will not remind you to" in pagelinks[counterConversation].text
                    counterConversation = counterConversation + 1
                except:
                    print("Cannot Collect All the Page")
                    print(traceback.format_exc())

                ################ Now get the data from the MITM Proxy #########
                _t = c.getJSON("test_open_url", wc.SNIFFHOST)
                frameinfo = getframeinfo(currentframe())
                print(frameinfo.filename, frameinfo.lineno)
                print("Performance Data")
                print(base64.b64decode(_t[0]['response']['body']['encoded']))
                print(_t[0]['durations'])
                ###################### Validation Layer #####################################################
                _temp = base64.b64decode(_t[0]['response']['body']['encoded'])
                #############################################################################################
                sleep(2)
                #########################################################
                print("Creating Local Test Folders for Test")
                simpleTest_Folder_dir_json_wire = os.path.join(test_results_dir_json_wire, "SimpleTest" + self.driver.name + "/test_remove_list_reminders_with_two_reminders_set")
                print(simpleTest_Folder_dir_json_wire)
                createFolder(simpleTest_Folder_dir_json_wire)
                simpleTest_Folder_dir_csv = os.path.join(test_results_dir_csv, "SimpleTest" + self.driver.name + "/test_remove_list_reminders_with_two_reminders_set")
                print(simpleTest_Folder_dir_csv)
                createFolder(simpleTest_Folder_dir_csv)
                simpleTest_Folder_dir_excel = os.path.join(test_results_dir_excel, "SimpleTest" + self.driver.name + "/test_remove_list_reminders_with_two_reminders_set")
                print(simpleTest_Folder_dir_excel)
                createFolder(simpleTest_Folder_dir_excel)
                simpleTest_Folder_dir_html = os.path.join(test_results_dir_html, "SimpleTest" + self.driver.name + "/test_remove_list_reminders_with_two_reminders_set")
                print(simpleTest_Folder_dir_html)
                createFolder(simpleTest_Folder_dir_html)

                ############## API ##############
                if _data['MITM'] == 'True':
                    print("Get Proxy data as flag is On")
                    _t = c.getJSON("test_greeting", simpleTest_Folder_dir_json_wire)
                    print(_t)
                    if _t == None:
                        print("No Data")
                    else:

                            print("Path")
                            print(_t[0]['path'] )
                            print("Performance Data")
                            print(_t[0]['times'])
                            print(_t[0]['durations'])
                            _requestbody= base64.b64decode(_t[0]['request']['body']['encoded'])
                            print(_requestbody)
                            _responsebody = base64.b64decode(_t[0]['response']['body']['encoded'])
                            print(_responsebody)
                            _temp = _responsebody.decode(errors='replace').split('�')
                            print(_temp)

                    print("Got JSON Data")
                    print("We will perform assertion now")

            except:
                print(traceback.format_exc())

        #Test 11
        def test_remove_all_reminder_with_two_reminders_set(self):
            try:
                counterConversation = 0
                _t = None
                print("Running the Test Open Url")
                if _data['MITM'] == 'True':
                    print("Clearing Cache as flag is True")
                    c.clearCache()
                time.sleep(2)
                ######################### Using Proxy Service ##########################################
                self.driver.delete_all_cookies()
                self.driver.get("https://chatbot-challenge.dev.replicant.ai")

                ################# Get Data from the Proxy for Validation instead of Web #####################
                time.sleep(2)
                parser = self.driver.page_source
                # Two Layers of Validation
                # First Option to get Data Scraped from Web
                # Second Option to get Data from Proxy
                # Third option to get data from Web Socket
                soup = BeautifulSoup(parser, "html.parser")
                pagelinks = soup.find_all('p', {'class': 'MuiTypography-root MuiTypography-body1'})
                #for pagenumber in pagelinks:
                try:
                        # print(pagenumber.text)
                        conversationBuilder[str(counterConversation)] = pagelinks[counterConversation].text
                        ############# Validation Type 1 with the Web #########################
                        assert "Greetings, friend! Type help to get started." in pagelinks[counterConversation].text
                        counterConversation = counterConversation + 1
                except:
                        print("Cannot Collect All the Page")
                        print(traceback.format_exc())

                ################ Now get the data from the MITM Proxy #########
                _t = c.getJSON("test_open_url", wc.SNIFFHOST)
                frameinfo = getframeinfo(currentframe())
                print(frameinfo.filename, frameinfo.lineno)
                print("Performance Data")
                print(_t[0]['response']['body']['text'])
                print(_t[0]['durations'])
                ###################### Validation Layer #####################################################
                _temp = _t[0]['response']['body']['text']
                #############################################################################################
                #############################################################################################
                self.driver.find_element(By.CSS_SELECTOR, ".MuiInputBase-input").click()
                self.driver.find_element(By.CSS_SELECTOR, ".MuiInputBase-input").send_keys("help")
                self.driver.find_element(By.CSS_SELECTOR, ".MuiInputBase-input").send_keys(Keys.ENTER)
                counterConversation = counterConversation + 1
                time.sleep(3)
                ############################ Two Layers of Validation #######################################
                # First Option to get Data Scraped from Web
                # Second Option to get Data from Proxy
                # Third option to get data from Web Socket
                parser = self.driver.page_source
                soup = BeautifulSoup(parser, "html.parser")
                pagelinks = soup.find_all('p', {'class': 'MuiTypography-root MuiTypography-body1'})
                # for pagenumber in pagelinks:
                try:
                    conversationBuilder[str(counterConversation)] = pagelinks[counterConversation].text
                    ############# Validation Type 1 with the Web #########################
                    assert "I am a reminder bot, here to help you get organized. Here are some of the things you can ask me to do" in pagelinks[counterConversation].text
                    counterConversation = counterConversation + 1
                except:
                        print("Cannot Collect All the Page")
                        print(traceback.format_exc())

                ################ Now get the data from the MITM Proxy #########
                _t = c.getJSON("test_open_url", wc.SNIFFHOST)
                frameinfo = getframeinfo(currentframe())
                print(frameinfo.filename, frameinfo.lineno)
                print("Performance Data")
                print(base64.b64decode(_t[0]['response']['body']['encoded']))
                print(_t[0]['durations'])
                ###################### Validation Layer #####################################################
                _temp = base64.b64decode(_t[0]['response']['body']['encoded'])
                #############################################################################################
                self.driver.find_element(By.CSS_SELECTOR, ".MuiInputBase-input").send_keys("remind me to make dinner in 5 minutes.")
                self.driver.find_element(By.CSS_SELECTOR, ".MuiInputBase-input").send_keys(Keys.ENTER)
                counterConversation = counterConversation + 1
                time.sleep(4)
                ############################ Two Layers of Validation #######################################
                # First Option to get Data Scraped from Web
                # Second Option to get Data from Proxy
                # Third option to get data from Web Socket
                parser = self.driver.page_source
                soup = BeautifulSoup(parser, "html.parser")
                pagelinks = soup.find_all('p', {'class': 'MuiTypography-root MuiTypography-body1'})
                #for pagenumber in pagelinks:
                try:
                    conversationBuilder[str(counterConversation)] = pagelinks[counterConversation].text
                    ############# Validation Type 1 with the Web #########################
                    assert "Ok, I will remind you to make dinner in 300 seconds." in pagelinks[counterConversation].text
                    counterConversation = counterConversation + 1
                except:
                    print("Cannot Collect All the Page")
                    print(traceback.format_exc())

                ################ Now get the data from the MITM Proxy #########
                _t = c.getJSON("test_open_url", wc.SNIFFHOST)
                frameinfo = getframeinfo(currentframe())
                print(frameinfo.filename, frameinfo.lineno)
                print("Performance Data")
                print(base64.b64decode(_t[0]['response']['body']['encoded']))
                print(_t[0]['durations'])
                ###################### Validation Layer #####################################################
                _temp = base64.b64decode(_t[0]['response']['body']['encoded'])
                #############################################################################################
                #############################################################################################
                self.driver.find_element(By.CSS_SELECTOR, ".MuiInputBase-input").send_keys("remind me to take out trash in 20 minutes.")
                self.driver.find_element(By.CSS_SELECTOR, ".MuiInputBase-input").send_keys(Keys.ENTER)
                counterConversation = counterConversation + 1
                time.sleep(3)
                ############################ Two Layers of Validation #######################################
                # First Option to get Data Scraped from Web
                # Second Option to get Data from Proxy
                # Third option to get data from Web Socket
                parser = self.driver.page_source
                soup = BeautifulSoup(parser, "html.parser")
                pagelinks = soup.find_all('p', {'class': 'MuiTypography-root MuiTypography-body1'})
                try:
                    conversationBuilder[str(counterConversation)] = pagelinks[counterConversation].text
                    ############# Validation Type 1 with the Web #########################
                    assert "Ok, I will remind you to take out trash in 1200 seconds" in pagelinks[counterConversation].text
                    counterConversation = counterConversation + 1
                except:
                    print("Cannot Collect All the Page")
                    print(traceback.format_exc())

                ################ Now get the data from the MITM Proxy #########
                _t = c.getJSON("test_open_url", wc.SNIFFHOST)
                frameinfo = getframeinfo(currentframe())
                print(frameinfo.filename, frameinfo.lineno)
                print("Performance Data")
                print(base64.b64decode(_t[0]['response']['body']['encoded']))
                print(_t[0]['durations'])
                ###################### Validation Layer #####################################################
                _temp = base64.b64decode(_t[0]['response']['body']['encoded'])
                #############################################################################################
                #############################################################################################
                self.driver.find_element(By.CSS_SELECTOR, ".MuiInputBase-input").send_keys("show all reminders")
                self.driver.find_element(By.CSS_SELECTOR, ".MuiInputBase-input").send_keys(Keys.ENTER)
                counterConversation = counterConversation + 1
                ################# Get Data from the Proxy for Validation instead of Web #####################
                time.sleep(3)
                ############################ Two Layers of Validation #######################################
                # First Option to get Data Scraped from Web
                # Second Option to get Data from Proxy
                # Third option to get data from Web Socket
                parser = self.driver.page_source
                soup = BeautifulSoup(parser, "html.parser")
                pagelinks = soup.find_all('p', {'class': 'MuiTypography-root MuiTypography-body1'})
                try:
                    conversationBuilder[str(counterConversation)] = pagelinks[counterConversation].text
                    ############# Validation Type 1 with the Web #########################
                    assert "make dinner" in pagelinks[counterConversation].text
                    assert "take out trash" in pagelinks[counterConversation].text
                    counterConversation = counterConversation + 1
                except:
                    print("Cannot Collect All the Page")
                    print(traceback.format_exc())

                ################ Now get the data from the MITM Proxy #########
                _t = c.getJSON("test_open_url", wc.SNIFFHOST)
                frameinfo = getframeinfo(currentframe())
                print(frameinfo.filename, frameinfo.lineno)
                print("Performance Data")
                print(base64.b64decode(_t[0]['response']['body']['encoded']))
                print(_t[0]['durations'])
                ###################### Validation Layer #####################################################
                _temp = base64.b64decode(_t[0]['response']['body']['encoded'])
                #############################################################################################
                #############################################################################################
                self.driver.find_element(By.CSS_SELECTOR, ".MuiInputBase-input").send_keys("clear all reminders")
                self.driver.find_element(By.CSS_SELECTOR, ".MuiInputBase-input").send_keys(Keys.ENTER)
                counterConversation = counterConversation + 1
                ################# Get Data from the Proxy for Validation instead of Web #####################
                time.sleep(2)
                ############################ Two Layers of Validation #######################################
                # First Option to get Data Scraped from Web
                # Second Option to get Data from Proxy
                # Third option to get data from Web Socket
                parser = self.driver.page_source
                soup = BeautifulSoup(parser, "html.parser")
                pagelinks = soup.find_all('p', {'class': 'MuiTypography-root MuiTypography-body1'})
                try:
                    conversationBuilder[str(counterConversation)] = pagelinks[counterConversation].text
                    ############# Validation Type 1 with the Web #########################
                    assert "Ok, I have cleared all of your reminders." in pagelinks[counterConversation].text
                    counterConversation = counterConversation + 1
                except:
                    print("Cannot Collect All the Page")
                    print(traceback.format_exc())

                ################ Now get the data from the MITM Proxy #########
                _t = c.getJSON("test_open_url", wc.SNIFFHOST)
                frameinfo = getframeinfo(currentframe())
                print(frameinfo.filename, frameinfo.lineno)
                print("Performance Data")
                print(base64.b64decode(_t[0]['response']['body']['encoded']))
                print(_t[0]['durations'])
                ###################### Validation Layer #####################################################
                _temp = base64.b64decode(_t[0]['response']['body']['encoded'])
                #############################################################################################
                #############################################################################################

                self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(2)").click()
                self.driver.find_element(By.CSS_SELECTOR, ".MuiInputBase-input").click()
                self.driver.find_element(By.CSS_SELECTOR, ".MuiInputBase-input").send_keys("show all reminders")
                self.driver.find_element(By.CSS_SELECTOR, ".MuiInputBase-input").send_keys(Keys.ENTER)
                counterConversation = counterConversation + 1
                time.sleep(3)
                ################# Get Data from the Proxy for Validation instead of Web #####################
                ############################ Two Layers of Validation #######################################
                # First Option to get Data Scraped from Web
                # Second Option to get Data from Proxy
                # Third option to get data from Web Socket
                parser = self.driver.page_source
                soup = BeautifulSoup(parser, "html.parser")
                pagelinks = soup.find_all('p', {'class': 'MuiTypography-root MuiTypography-body1'})
                try:
                    conversationBuilder[str(counterConversation)] = pagelinks[counterConversation].text
                    ############# Validation Type 1 with the Web #########################
                    assert "You have no reminders." in pagelinks[counterConversation].text
                    counterConversation = counterConversation + 1
                except:
                    print("Cannot Collect All the Page")
                    print(traceback.format_exc())

                ################ Now get the data from the MITM Proxy #########
                _t = c.getJSON("test_open_url", wc.SNIFFHOST)
                frameinfo = getframeinfo(currentframe())
                print(frameinfo.filename, frameinfo.lineno)
                print("Performance Data")
                print(base64.b64decode(_t[0]['response']['body']['encoded']))
                print(_t[0]['durations'])
                ###################### Validation Layer #####################################################
                _temp = base64.b64decode(_t[0]['response']['body']['encoded'])
                #############################################################################################

                sleep(2)
                #########################################################
                print("Creating Local Test Folders for Test")
                simpleTest_Folder_dir_json_wire = os.path.join(test_results_dir_json_wire, "SimpleTest" + self.driver.name + "/test_remove_all_reminder_with_two_reminders_set")
                print(simpleTest_Folder_dir_json_wire)
                createFolder(simpleTest_Folder_dir_json_wire)
                simpleTest_Folder_dir_csv = os.path.join(test_results_dir_csv, "SimpleTest" + self.driver.name + "/test_remove_all_reminder_with_two_reminders_set")
                print(simpleTest_Folder_dir_csv)
                createFolder(simpleTest_Folder_dir_csv)
                simpleTest_Folder_dir_excel = os.path.join(test_results_dir_excel, "SimpleTest" + self.driver.name + "/test_remove_all_reminder_with_two_reminders_set")
                print(simpleTest_Folder_dir_excel)
                createFolder(simpleTest_Folder_dir_excel)
                simpleTest_Folder_dir_html = os.path.join(test_results_dir_html, "SimpleTest" + self.driver.name + "/test_remove_all_reminder_with_two_reminders_set")
                print(simpleTest_Folder_dir_html)
                createFolder(simpleTest_Folder_dir_html)

                ############## API ##############
                if _data['MITM'] == 'True':
                    print("Get Proxy data as flag is On")
                    _t = c.getJSON("test_greeting", simpleTest_Folder_dir_json_wire)
                    print(_t)
                    if _t == None:
                        print("No Data")
                    else:

                            print("Path")
                            print(_t[0]['path'] )
                            print("Performance Data")
                            print(_t[0]['times'])
                            print(_t[0]['durations'])
                            _requestbody= base64.b64decode(_t[0]['request']['body']['encoded'])
                            print(_requestbody)
                            _responsebody = base64.b64decode(_t[0]['response']['body']['encoded'])
                            print(_responsebody)
                            _temp = _responsebody.decode(errors='replace').split('�')
                            print(_temp)
                            # [w for w in _temp if w.isalnum()]
                            # for w in _temp:
                            #     if w.isalnum():
                            #         print(w)
                            print(_temp)

                    print("Got JSON Data")
                    print("We will perform assertion now")

            except:
                print(traceback.format_exc())