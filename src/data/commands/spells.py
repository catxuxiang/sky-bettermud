from Scripts.bettermudscript import Command, UsageError, FindTarget
from accessors.CharacterAccessor import character
from accessors.RoomAccessor import room
from accessors.ItemAccessor import item


class superglue( Command ):
    name = "superglue"
    usage = "\"superglue <character>\""
    description = "superglues someone to the floor"
    def Run( self, args ):
        if not args: raise UsageError

        me = character( self.me )
        r = room( me.Room() )

        # find the name:
        id1 = FindTarget( r.SeekCharacter, r.IsValidCharacter, r.CurrentCharacter, args )
        c = character( id1 )
        name = c.Name()

        self.mud.AddActionAbsolute( 0, "addlogic", 0, id1, 0, 0, "superglue" )
        self.mud.AddActionAbsolute( 0, "vision", r.ID(), 0, 0, 0, "<#FF0000>OMG!!! " + me.Name() + " just SUPERGLUED " + name + " to the floor!!!!!" )
        self.mud.AddActionRelative( 20000, "messagelogic", 0, id1, 0, 0, "superglue remove" )



class uberweight( Command ):
    name = "uberweight"
    usage = "\"uberweight <item>\""
    description = "puts a magical weight on an item"
    def ScriptInit( self ):
        # init the next execution time to 0, so you can execute it right away
        self.executiontime = 0

    def Run( self, args ):
        if not args: raise UsageError

        me = character( self.me )
        r = room( me.Room() )

        time = self.mud.GetTime()
        if time < self.executiontime:
            me.DoAction( "error", 0, 0, 0, 0, "You need to wait " + str( (self.executiontime - time) / 1000 ) + " more seconds to use this again!" )
            return

        id1 = FindTarget( r.SeekItem, r.IsValidItem, r.CurrentItem, args )
        item = item( id1 )
        name = item.Name()

        # add 120 seconds; 2 minutes
        self.executiontime = time + 120000

        self.mud.AddActionAbsolute( 0, "addlogic", 1, id1, 0, 0, "uberweight" )
        self.mud.AddActionAbsolute( 0, "vision", r.ID(), 0, 0, 0, "<#FF0000>" + me.Name() + " just cast UBERWEIGHT on " + name + "!" )
        self.mud.AddActionRelative( 20000, "messagelogic", 1, id1, 0, 0, "uberweight remove" )
