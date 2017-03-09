# coding=utf-8
'''
Created on Mar 9, 2017

@author: DELL
'''
from website.actions.LogIn import LogIn

class EnigmaFactoryPage(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
    
    ''' Factory methods to create page objects
    '''
    @staticmethod
    def getLogIn():
        return LogIn()
    
