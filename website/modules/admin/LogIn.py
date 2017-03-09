# coding=utf-8
'''
Created on Mar 9, 2017

@author: DELL
'''
import unittest
from teamcity import is_running_under_teamcity
from teamcity.unittestpy import TeamcityTestRunner
from com.anki.test.automation.overdrive.module.overdrive.tracks.BaseTracksGeneralTestCase import BaseTracksGeneralTestCase
from website.actions.Common import logInfo

class GeneralBankTurnKitPDP(BaseTracksGeneralTestCase):
    def test_c45758(self):
        # US, CA, UK, DE
        logInfo('C45758 - Verify title of Bank Turn Kit PDP page displays as design')   
        
        # Pre-condition: User is on Bank Turn Kit PDP
        # Main steps
        logInfo('Go to Bank Turn Kit PDP %s language'% self.cfRanLanguage)
        self.tracksPage.navigateToWebAndLanguage(url = self.cfBankTurnKitPDPUrl, language = self.cfRanLanguage)
        
        logInfo('VP - The title of US Bank Turn Kit PDP should be displayed correctly')
        self.bankTurnKitPDP.checkTheTitleOfPageIsDisplayedCorrectly()
        
    def test_c45765(self):
        # US, CA, UK, DE
        logInfo('C45765 - Verify currency unit of item price for each language displays correctly')   
        
        # Pre-condition: User is on Bank Turn Kit PDP
        # Main steps
        logInfo('Go to Bank Turn Kit PDP %s language'% self.cfRanLanguage)
        self.tracksPage.navigateToWebAndLanguage(url = self.cfBankTurnKitPDPUrl, language = self.cfRanLanguage)
        
        logInfo('Step 1 - Observe currency unit of item price')
        logInfo('VP - Verify displayed currency unit of item price for US language should be $ xxx.xx')
        self.bankTurnKitPDP.checkCurrencyUnitIsDisplayed()
        
    @unittest.skip('Removed test case')
    def test_c27265(self):
        # US, CA, UK, DE
        logInfo('C27265 - Verify if scrolling over the Hero section, the Bank Turn Kit nav is displayed as design')   
        
        # Pre-condition: User is on Bank Turn Kit PDP
        # Main steps
        logInfo('Go to Bank Turn Kit PDP')
        self.tracksPage.clickAccessoryDetailsLinkByName(self.cfAccessoryNameBANKTURNKIT)
        
        logInfo('Test with %s language' % self.cfRanLanguage)
        self.footer.switchToAnotherLanguage(language = self.cfRanLanguage)
        
        logInfo('Step 1 - Hover on Privacy Policy link')
        self.bankTurnKitPDP.hoverOnPrivacyPolicyLink()
        
        logInfo('VP - Verify the Bank Turn Kit nav is displayed as design')
        self.bankTurnKitPDP.checkBankTurnKitNavIsDisplayedAsDesign()
              
    def test_c57206(self):
        logInfo("C57206 - Verify all 'www' urls redirect to non-www urls ")   
        
        # Pre-condition: User is on Bank Turn Kit page
        # Main steps
        logInfo('Go to Bank Turn Kit PDP %s language'% self.cfRanLanguage)
        self.tracksPage.navigateToWebAndLanguage(url = self.cfBankTurnKitPDPUrl, language = self.cfRanLanguage)
        
        logInfo('Step 1 - Navigate to %s Bank Turn Kit page with www urls' % self.cfRanLanguage)
        self.homePage.navigateToWebAndLanguage(self.cfBankTurnKitPDPUrl.replace('https://', 'http://www.'), self.cfRanLanguage)
        
        logInfo('VP - The %s Home page with www urls should be redirected to non-www urls' % self.cfRanLanguage)
        self.bankTurnKitPDP.checkTheFirstPartWWWOfTheURLIsRedirectedToHTTPS()
        
    def test_c57207(self):
        logInfo("C57207 - Verify all http:// urls will redirect to https://  urls")   
        
        # Pre-condition: User is on Bank Turn Kit page
        # Main steps
        logInfo('Go to Bank Turn Kit PDP %s language'% self.cfRanLanguage)
        self.tracksPage.navigateToWebAndLanguage(url = self.cfBankTurnKitPDPUrl, language = self.cfRanLanguage)
        
        logInfo('Step 1 - Navigate to %s Bank Turn Kit page with http://'' urls' % self.cfRanLanguage)
        self.homePage.navigateToWebAndLanguage(self.cfBankTurnKitPDPUrl.replace('https://', 'http://'), self.cfRanLanguage)
        
        logInfo('VP - The %s Home page with http:// urls should be redirected to https:// urls' % self.cfRanLanguage)
        self.bankTurnKitPDP.checkTheFirstPartHTTPOfTheURLIsRedirectedToHTTPS()
        
if __name__ == '__main__':
    
    testcaseName = 'test_c23108'
    
    # If the test case name is not null, then run only this test case 
    if testcaseName != '':
        suite = unittest.TestSuite()
        suite.addTest(GeneralBankTurnKitPDP(testcaseName))
        runner = unittest.TextTestRunner()
        runner.run(suite)
    else:
        if is_running_under_teamcity():
            runner = TeamcityTestRunner()
        else:
            runner = unittest.TextTestRunner()
        unittest.main(testRunner=runner)