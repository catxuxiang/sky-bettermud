'''
Created on 2012-6-3

@author: Sky
'''
SCRIPTRELOADMODE_LEAVEEXISTING = 0
SCRIPTRELOADMODE_RELOADFUNCTIONS = 1

class Script:
    def Load(self, sr, prefix):
        raise Exception("Virtual Method!")
    
    def Save(self, sr, prefix):
        raise Exception("Virtual Method!")
        
    def GetName(self):
        raise Exception("Virtual Method!")
    
    def __del__(self):
        raise Exception("Virtual Method!")
