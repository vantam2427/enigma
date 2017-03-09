'''
Created on Mar 9, 2017

@author: DELL
'''
import os
import unittest


class BaseAccessoriesGeneralTestCase(unittest.TestCase, AnkiAbstractTest):
    def setUp(self):
        AnkiAbstractTest.__init__(self)
        
        # Navigate to Home page
        self.homePage.navigateToWeb(self.cfTrackLandingUrl, self.cfDriver)
    
    def tearDown(self):
        self.homePage.closeBrowser()
        self.assertEqual(int(os.environ['ANKI_WARNINGS']), int(os.environ['ANKI_ERRORS']))