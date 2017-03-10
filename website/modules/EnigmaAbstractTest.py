# coding=utf-8
'''
Created on Mar 9, 2017

@author: DELL
'''
import os
import unittest
from website.modules.Config import Config
from website.actions.EnigmaFactoryPage import EnigmaFactoryPage
from website.actions.Common import generateUniqueValue, logWarning

class EnigmaAbstractTest(Config):
    
    def __init__(self):
        Config.__init__(self)
        
        # Set current path to environment
        os.environ['ENIGMA_PATH'] = (os.path.dirname(os.path.realpath(__file__)))
        print os.environ['ENIGMA_PATH'].replace("\\","/")+ "../../resources/chromedriver.exe"
        print os.path.isfile(os.environ['ENIGMA_PATH'].replace("\\","/")+ "/../../resources/chromedriver.exe")
        os.environ['ENIGMA_ERRORS'] = "0"
        os.environ['ENIGMA_WARNINGS'] = "0"
    
        # Generate log file path
        self.generateLogFilePath()
        
        # Load interface elements and private functions for Home page
        self.loginPage = EnigmaFactoryPage.getLogIn()
        
    def generateLogFilePath(self):
        try:
            logFileName = unittest.TestCase.id(self)
            logFileName = str(logFileName).split(".")[str(logFileName).count(".")-1] + "." + str(logFileName).split(".")[str(logFileName).count(".")]
            logFileName = logFileName.replace("__main__.", "")
            logFileName = logFileName.replace(".", "-")
            logFileName = logFileName + "-" + generateUniqueValue() + ".log"
            
            # Process to calculate the length of log file name
            if len(logFileName) > 124:
                logFileName = "..." + str(logFileName)[-121:]
                
            # Set current path to environment
            os.environ['ENIGMA_LOG_PATH'] = str(os.environ['ENIGMA_PATH']).replace("\\", "/") + "/../../../../../../_logs/" + logFileName
            
        except Exception, e:
            logWarning(str(e))