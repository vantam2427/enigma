# coding=utf-8
'''
Created on Mar 9, 2017

@author: DELL
'''
import unittest
from teamcity import is_running_under_teamcity
from teamcity.unittestpy import TeamcityTestRunner
from website.actions.Common import logInfo
from website.modules.admin.BaseAdmin import BaseAdmin

class LogIn(BaseAdmin):
    def test_Admin(self):
        logInfo('C45758 - Verify title of Bank Turn Kit PDP page displays as design')   
        
        # Pre-condition: 

        
if __name__ == '__main__':
    
    testcaseName = 'test_Admin'
    
    # If the test case name is not null, then run only this test case 
    if testcaseName != '':
        suite = unittest.TestSuite()
        suite.addTest(LogIn(testcaseName))
        runner = unittest.TextTestRunner()
        runner.run(suite)
    else:
        if is_running_under_teamcity():
            runner = TeamcityTestRunner()
        else:
            runner = unittest.TextTestRunner()
        unittest.main(testRunner=runner)