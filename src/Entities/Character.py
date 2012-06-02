'''
Created on 2012-5-30

@author: Sky
'''
from Entities.Entity import Entity, HasRoom, HasRegion, HasTemplateId, HasItems
from Entities.DataEntity import DataEntity
from Entities.LogicEntity import LogicEntity
from Db.ItemDatabase import ItemDB
from Db.CommandDatabase import CommandDB
from accessors.RegionAccessor import region
from accessors.RoomAccessor import room

class CharacterTemplate(Entity, DataEntity):
    def __init__(self):
        Entity.__init__(self)
        self.m_commands = []
        self.m_logics = []
        
    def Load(self, sr, prefix):
        prefix += ":" + self.GetId()
        self.m_name = sr.get(prefix + ":NAME")
        self.m_description = sr.get(prefix + ":DESCRIPTION")
        
        self.m_attributes.Load(prefix + ":")
        
        commands = sr.get(prefix + ":COMMANDS").split(" ")
        self.m_commands = []
        for i in commands:
            self.m_commands.append(i)
            
        logics = sr.get(prefix + ":LOGICS").split(" ")
        self.m_logics = []
        for i in logics:
            self.m_logics.append(i)
            
class Character(LogicEntity, DataEntity, HasRoom, HasRegion, HasTemplateId, HasItems):
    def __init__(self):
        self.m_account = None
        self.m_loggedin = False
        self.m_quiet = False
        self.m_verbose = True
        
    def LoadTemplate(self, p_template):
        self.m_templateid = p_template.GetId()
        self.m_name = p_template.GetName()
        self.m_description = p_template.GetDescription()
        self.m_attributes = p_template.m_attributes
        
        for i in p_template.m_commands:
            self.AddCommand(i)
            
        for i in p_template.m_logics:
            self.AddLogic(i)
            
    def Load(self, sr, prefix):
        if (not self.IsPlayer()) or self.IsLoggedIn():
            self.Remove()
            
        prefix += ":" + self.GetId()
        self.m_name = sr.get(prefix + ":NAME")
        self.m_description = sr.get(prefix + ":DESCRIPTION")
        self.m_room = sr.get(prefix + ":ROOM")
        self.m_region = sr.get(prefix + ":REGION")
        
        self.m_templateid = sr.get(prefix + ":TEMPLATEDID")
        self.m_account = sr.get(prefix + ":DESCRIPTION")
        self.m_quiet = sr.get(prefix + ":QUIET")
        if self.m_quiet == "False":
            self.m_quiet = False
        else:
            self.m_quiet = True
        self.m_verbose = sr.get(prefix + ":VERBOSE")
        if self.m_verbose == "False":
            self.m_verbose = False
        else:
            self.m_verbose = True
            
        # load attributes
        self.m_attributes.Load(sr, prefix)
        
        self.m_commands = []
        for i in range(0, sr.llen(prefix + ":COMMANDS")):
            command = sr.lindex(prefix + ":COMMANDS", i)
            if self.AddCommand(command):
                c = self.m_commands[len(self.m_commands) - 1]
                c.Load(sr, prefix + ":COMMANDS")
            else:
                raise Exception("Cannot load command: " + command)
            
        self.m_logic.Load(sr, prefix, self.m_id)
        
        self.m_items = []
        for i in range(0, sr.llen(prefix + ":ITEMS")):
            id1 = sr.lindex(prefix + ":ITEMS", i)
            self.m_items.append(prefix + ":ITEMS:" + id1)
            
        if (not self.IsPlayer()) or self.IsLoggedIn():
            self.Add()
            
    def Save(self, sr, prefix):
        prefix += ":" + self.GetId()
        sr.set(prefix + ":NAME", self.m_name)
        sr.set(prefix + ":DESCRIPTION", self.m_description)
        sr.set(prefix + ":ROOM", self.m_room.GetId())
        sr.set(prefix + ":REGION", self.m_region.GetId())
        
        sr.set(prefix + ":DESCRIPTION", self.m_templateid)
        sr.set(prefix + ":DESCRIPTION", self.m_account.GetId())
        sr.set(prefix + ":DESCRIPTION", str(self.m_quiet))
        sr.set(prefix + ":DESCRIPTION", str(self.m_verbose))
        
        # save my attributes to disk
        self.m_attributes.Save(sr, prefix)
        
        sr.ltrim(prefix + ":COMMANDS", 2, 1)
        for i in self.m_commands:
            name = i.GetName()
            sr.rpush(prefix + ":COMMANDS", name)
            i.Save(sr, prefix + ":COMMANDS")
            
        self.m_logic.Save(sr, prefix)
        
        sr.ltrim(prefix + ":ITEMS", 2, 1)
        for i in self.m_items:
            sr.rpush(prefix + ":ITEMS", i.GetId())
            ItemDB.SaveEntity(i, prefix + ":ITEMS")
            
    def FindCommand(self, p_name):
        for i in self.m_commands:
            if i.GetName().lower() == p_name.lower().strip():
                return i
            
        for i in self.m_commands:
            if i.GetName().lower().find(p_name.lower().strip()) == 0:
                return i
            
        return None
    
    def HasCommand(self, p_command):
        for i in self.m_commands:
            if i.GetName().lower() == p_command.lower().strip():
                return True
        return False

    def AddCommand(self, p_command):
        if self.HasCommand(p_command):
            return False
        
        try:
            self.m_commands.append(CommandDB.Generate(p_command, self.GetId()))
            return True
        except Exception:
            return False
        
    def DelCommand(self, p_command):
        index = -1
        i = 0
        for command in self.m_commands:
            if command.GetName().lower() == p_command.lower().strip():
                index = i
            i += 1
        if index != -1:
            del self.m_commands[index]
            return True
        else:
            return False
        
    def Add(self):
        reg = region(self.m_region)
        reg.AddCharacter(self.m_id)
        
        r = room(self.m_room)
        r.AddCharacter(self.m_id)
        
    def Remove(self):
        if self.m_region != None and self.m_room != None:
            reg = region(self.m_region)
            reg.DelCharacter(self.m_id)
            
            r = room(self.m_room)
            r.DelCharacter(self.m_id)
     