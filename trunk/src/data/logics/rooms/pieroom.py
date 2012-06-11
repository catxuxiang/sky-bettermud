from accessors.ItemAccessor import item
from data.logics.logic import logic

class pieroom( logic ):
    def Run( self, action, arg1, arg2, arg3, arg4, data ):
        if action == "getitem":
            item = item( arg2 )
            if item.GetTemplateId() == "2":
                self.mud.AddActionRelative( 5000, "vision", self.me, "0", "0", "0", "The Baker puts a new pie into the oven!" )
                self.mud.AddActionRelative( 1200000, "spawnitem", "2", self.me, "0", "0", "" )
                self.mud.AddActionRelative( 1200001, "vision", self.me, "0", "0", "0", "A freshly baked Pie pops out of the oven!" )
