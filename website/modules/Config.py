# coding=utf-8
'''
Created on Mar 9, 2017

@author: DELL
'''
import os

verificationErrors = 0

class Config():
    def __init__(self):
        self.cfDriver = os.environ.get('SELENIUM_DEVICE',"Chrome") #Firefox, Chrome, Ie
        self.cfRequiredSite = os.environ.get('REQUIRED_SITE',"Prod")
        self.cfLongTimeWait = 180
        self.cfNormalTimeWait = 120
        self.cfShortTimeWait = 60
        self.cfImplicitlyTimeWait = 90
        self.cfPageLoadTimeout = 600
        self.cfShortTime = 20
        
        # Enigma URLs
        self.cfProdAdminUrl = "http://enigma:cie1yiVa@admin-dev.enigma.bz"
        
        # Estimated Tax
        self.cfUSProductTax = "$13.87"
        self.cfUKProductTax = u"£25.00"
        
        # Month Values
        self.cfMonthCheckoutList = ['1 - January', '2 - February', '3 - March', '4 - April', '5 - May', '6 - June', '7 - July',
                                    '8 - August', '9 - September', '10 - October', '11 - November', '12 - December']
        self.cfMonthCheckoutDEList = ['1 - Januar', '2 - Februar', '3 - März', '4 - April', '5 - Mai', '6 - Juni', '7 - Juli',
                                    '8 - August', '9 - September', '10 - Oktober', '11 - November', '12 - Dezember']
        