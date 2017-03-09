'''
Created on Mar 9, 2017

@author: DELL
'''
class LogInPage():
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        # Assign interface to variables
        self.txtEmail = "//title[contains(text(),'Cozmo') and contains(text(),'Amazon.com')]"
        self.txtPassword = "//title[contains(text(),'Amazon.com') and contains(text(),'Anki OVERDRIVE')]"  