# coding=utf-8
'''
Created on Mar 9, 2017

@author: DELL
'''

from website.actions.AbstractPage import AbstractPage
from website.interfaces.LogInPage import LogInPage

class LogIn(AbstractPage, LogInPage):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        AbstractPage.__init__(self)
        LogInPage.__init__(self)
   
    def checkTheOverDriveAppPageExisted(self):
        pagExist = self.doesElementExisted(self.pagOverDrive)
        self.verifyTrue(pagExist, "The OverDrive app page is displayed", "The OverDrive app page is not displayed")
        self.closeAndSwitchToLatestWindow()
        