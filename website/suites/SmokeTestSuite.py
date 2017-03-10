'''
Created on Mar 10, 2017

@author: DELL
'''
import os
from time import gmtime, strftime, sleep
import unittest
import HTMLTestRunner

os.environ.setdefault('SELENIUM_DEVICE',"Firefox") # Firefox / Chrome / Ie
os.environ.setdefault('REQUIRED_SITE',"Prod")
os.environ.setdefault('SELECT_LANGUAGE',"US")
os.environ.setdefault('RUN_FULL_LANGUAGES',"FALSE")

def smokeTestSuite(listTCs = []):
    
    # Create path
    pathFile = "C:\\test-reports\\"
    d = os.path.dirname(pathFile)
    if not os.path.exists(d):
        os.makedirs(d)
        
    dateTime = strftime("%Y%m%d%H%M%S", gmtime())
    pathFile = '%sMon_%s\\' % (pathFile, dateTime)
    d = os.path.dirname(pathFile)
    if not os.path.exists(d):
        os.makedirs(d)
    
    # Discover and load all unit tests in all files named ``*_test.py`` in ``./src/``    
    path = str(os.path.dirname(os.path.realpath(__file__))).replace("suites","module")
    
    print path

    ########################
    # List test cases want to runs
    ########################
    i = 1
    if len(listTCs) == 0:
        # Run test cases with full languages
        for all_test_suite in unittest.defaultTestLoader.discover(path, pattern='*.py'):
            print all_test_suite
            for test_suite in all_test_suite:
                try:
                    for test_case in test_suite:
                        testcaseName = str(test_case).split(" ")[0]
                        if testcaseName in listTCs:
                            print "=========================BEGIN TEST CASE======================="
                            print '%s - Running %s/%s' % (testcaseName, str(i), str(len(listTCs)))
                            testCaseName = str(str(test_case).split(" (")[0])
                            dateTime = strftime("%Y%m%d%H%M%S", gmtime())
                            pathFileSaved = '%s%s.html' % (pathFile, testCaseName)
                            buf = file(pathFileSaved + '','wb')
                            runner = HTMLTestRunner.HTMLTestRunner(
                                            stream=buf,
                                            title=testCaseName + ' - Test Results',
                                            description=testCaseName + ' result'
                                            )
                            runner.run(test_case)
                            i = i + 1
                            sleep(0.5)
                            print "=========================END TEST CASE========================="
                except Exception, e:
                    print str(e)   
        
if __name__ == "__main__":
    smokeTestSuite()