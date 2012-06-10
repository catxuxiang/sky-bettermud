'''
Created on 2012-6-9

@author: Sky
'''
from accessors.GameAccessor import GameWrap

class bettermudscript:

    # Initialize the script with an ID
    def Init( self, id1, p_arg2 = "0", p_arg3 = "0", p_arg4 = "0", p_arg5 = "0", p_arg6 = ""):
        self.me = id1
        self.mud = GameWrap()
        self.ScriptInit()

    def ScriptInit( self ):
        pass

    def Name( self, p_arg1 = "", p_arg2 = "0", p_arg3 = "0", p_arg4 = "0", p_arg5 = "0", p_arg6 = "" ):
        return self.name

    def LoadScript( self, s ):
        pass

    def SaveScript( self ):
        return ""  