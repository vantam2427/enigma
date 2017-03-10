'''
Created on Mar 10, 2017

@author: DELL
'''
import os
from selenium import webdriver
os.environ['ENIGMA_PATH'] = (os.path.dirname(os.path.realpath(__file__)))
print os.environ['ENIGMA_PATH'].replace("website\suites","resources")