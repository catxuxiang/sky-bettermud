'''
Created on 2012-6-9

@author: Sky
'''
from accessors.GameAccessor import GameWrap
from accessors.CharacterAccessor import character
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
    
class UsageError(Exception):
    pass

class TargetError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)


def FindTarget( seekf, validf, getf, name ):
    seekf( name )
    if not validf(): raise TargetError( name )
    return getf()


class Command(bettermudscript):

    # Usage
    def Usage( self ):
        return self.usage

    # description
    def Description( self ):
        return self.description

    # the standard call method.
    def Execute( self, args ):
        try:
            self.Run( args )
        except UsageError:
            me = character( self.me )
            me.DoAction( "error", 0, 0, 0, 0, "Usage: " + self.Usage() )
        except TargetError as e:
            me = character( self.me )
            me.DoAction( "error", 0, 0, 0, 0, "Cannot find: " + e.value )    