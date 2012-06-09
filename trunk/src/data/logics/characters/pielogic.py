import data.logics.logic
from accessors.CharacterAccessor import character
from accessors.ItemAccessor import item

class pies( data.logics.logic.logic ):
    def Run( self, action, arg1, arg2, arg3, arg4, data ):
        me = character( self.me )
        if action == "say" and data.find( "pies" ) != -1 and arg1 != me.ID():
            c = character( arg1 )
            self.mud.AddActionAbsolute( 0, "attemptsay", me.ID(), 0, 0, 0, c.Name() + ": YES!!! PIES!!!!!" )

        return 0


class glarepie( data.logics.logic.logic ):
    def Run( self, action, arg1, arg2, arg3, arg4, data ):
        if action == "getitem":
            item = item( arg2 )
            print item.TemplateID()
            print "lies"
            if item.TemplateID() == 2:
                print "pies"
                self.mud.AddActionAbsolute( 0, "attemptsay", self.me, 0, 0, 0, "Hey!!!! Thos-a Pies aren't-a FREE!" )
                print "cries"

        return 0
