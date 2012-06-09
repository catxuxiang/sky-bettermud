import data.logics.logic
from accessors.CharacterAccessor import character
from accessors.ItemAccessor import item

class cantget( data.logics.logic.logic ):

    def Run( self, action, arg1, arg2, arg3, arg4, data ):
        if action == "cangetitem":
            c = character( arg1 )
            me = item( arg2 )
            self.mud.AddActionAbsolute( 0, "vision", c.Room(), 0, 0, 0, c.Name() + " almost has a hernia, trying to pull " + me.Name() + " out of the ground!" )
            return 1




class uberweight( data.logics.logic.logic ):

    def Run( self, action, arg1, arg2, arg3, arg4, data ):
        if action == "cangetitem":
            c = character( arg1 )
            me = item( arg2 )
            self.mud.AddActionAbsolute( 0, "vision", c.Room(), 0, 0, 0, c.Name() + " struggles like a madman trying to pull " + me.Name() + " off the ground, but it's stuck!" )
            return 1

        if action == "messagelogic":
            if data == "uberweight remove":
                self.mud.AddActionAbsolute( 0, "dellogic", 1, self.me, 0, 0, "uberweight" )
                me = item( self.me )
                self.mud.AddActionAbsolute( 0, "vision", me.Room(), 0, 0, 0, "The uberweight on " + me.Name() + " wears off!" )



class canread( data.logics.logic.logic ):
    def Run( self, action, arg1, arg2, arg3, arg4, data ):
        if action == "query" and data == "canread":
            return 1