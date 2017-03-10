'''
Created on Mar 9, 2017

@author: DELL
'''
import os
import unittest
from website.modules.EnigmaAbstractTest import EnigmaAbstractTest


class BaseAdmin(unittest.TestCase, EnigmaAbstractTest):
    def setUp(self):
        EnigmaAbstractTest.__init__(self)
        
        # Navigate to Home page
        self.loginPage.navigateToWeb(self.cfProdAdminUrl, self.cfDriver)
    
    def tearDown(self):
        self.homePage.closeBrowser()
        self.assertEqual(int(os.environ['ANKI_WARNINGS']), int(os.environ['ANKI_ERRORS']))