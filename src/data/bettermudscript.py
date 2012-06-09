'''
Created on 2012-6-9

@author: Sky
'''
from accessors.GameAccessor import GameWrap

class bettermudscript:

    # Initialize the script with an ID
    def Init( self, id1 ):
        self.me = id1
        self.mud = GameWrap()
        self.ScriptInit()

    def ScriptInit( self ):
        pass

    def Name( self ):
        return self.name

    def LoadScript( self, s ):
        pass

    def SaveScript( self ):
        return ""  