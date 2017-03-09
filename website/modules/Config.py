# coding=utf-8
'''
Created on Mar 9, 2017

@author: DELL
'''
import os

verificationErrors = 0

class Config():
    def __init__(self):
        self.cfSelectedLanguage = os.environ.get('SELECT_LANGUAGE',"US-CA-UK-DE")
        self.cfRanLanguage = os.environ.get('RAN_LANGUAGE','US')
        self.cfRunFullLanguages = os.environ.setdefault('RUN_FULL_LANGUAGES',"False")
        self.cfDriver = os.environ.get('SELENIUM_DEVICE',"Firefox") #Firefox, Chrome, Ie
        self.cfCheckOrder = os.environ.get('CHECK_ORDER',"True")
        self.cfRequiredRun = os.environ.get('REQUIRED_RUN',"False")
        self.cfRequiredSite = os.environ.get('REQUIRED_SITE',"Prod")
        self.cfSikuliIDEPathFile = "C:\\Program Files (x86)\\Sikuli X\\Sikuli-IDE.bat"
        self.cfLongTimeWait = 180
        self.cfNormalTimeWait = 120
        self.cfShortTimeWait = 60
        self.cfImplicitlyTimeWait = 90
        self.cfPageLoadTimeout = 600
        self.cfShortTime = 20
        
        # Product Price
        self.cfProductPriceSTARTERKIT = "$149.99"
        self.cfUKProductPriceSTARTERKIT = u"£149.99"
        self.cfCAProductPriceSTARTERKIT = "CA$199.99"
        self.cfDEProductPriceSTARTERKIT = u"179,99 €"
        self.cfATProductPriceSTARTERKIT = u"179,99 €"
        self.cfCHProductPriceSTARTERKIT = u"179,99 €"
        
        # Estimated Tax
        self.cfUSProductTax = "$13.87"
        self.cfUKProductTax = u"£25.00"
        self.cfDEProductTax = u"28,74 €"
        
        # Month Values
        self.cfMonthCheckoutList = ['1 - January', '2 - February', '3 - March', '4 - April', '5 - May', '6 - June', '7 - July',
                                    '8 - August', '9 - September', '10 - October', '11 - November', '12 - December']
        self.cfMonthCheckoutDEList = ['1 - Januar', '2 - Februar', '3 - März', '4 - April', '5 - Mai', '6 - Juni', '7 - Juli',
                                    '8 - August', '9 - September', '10 - Oktober', '11 - November', '12 - Dezember']
        