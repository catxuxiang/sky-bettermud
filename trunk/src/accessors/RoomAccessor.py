'''
Created on 2012-6-1

@author: Sky
'''
from Db.RoomDatabase import RoomDB
from Entities.Action import Action

class room:
    def __init__(self, p_data):
        if type(p_data) == str:
            self.m_room = RoomDB.Get(p_data)
            self.m_room.AddRef()
        else:
            self.m_room.DelRef()
            self.m_room = p_data.m_room
            self.m_room.AddRef()
            
    def __del__(self):
        self.m_room.DelRef()
        
    def GetId(self):
        return self.m_room.GetId()
    
    def GetName(self):
        return self.m_room.GetName()
    
    def GetDescription(self):
        return self.m_room.GetDescription()
    
    def SetId(self, p_id):
        self.m_room.SetId(p_id)
        
    def SetName(self, p_name):
        self.m_room.SetName(p_name)
        
    def SetDescription(self, p_desc):
        self.m_room.SetDescription(p_desc)
        
    def GetRegion(self):
        return self.m_room.GetRegion()
    
    def SetRegion(self, p_region):
        self.m_room.SetRegion(p_region)
        
    def AddItem(self, p_id):
        self.m_room.AddItem(p_id)
        
    def DelItem(self, p_id):
        self.m_room.DelItem(p_id)
        
    def Items(self):
        return self.m_room.Items()
    
    def SeekItem(self, p_name):
        p_name = p_name.lower().strip()
        for i in self.m_room.m_items:
            if i.GetName().lower() == p_name:
                return i
        for i in self.m_room.m_items:
            if i.GetName().lower().find(p_name) == 0:
                return i
        return None
    
    def AddCharacter(self, p_id):
        self.m_room.AddCharacter(p_id)
        
    def DelCharacter(self, p_id):
        self.m_room.DelCharacter(p_id)
        
    def Characters(self):
        return self.m_room.Characters()
    
    def SeekCharacter(self, p_name):
        p_name = p_name.lower().strip()
        for i in self.m_room.m_characters:
            if i.GetName().lower() == p_name:
                return i
        for i in self.m_room.m_characters:
            if i.GetName().lower().find(p_name) == 0:
                return i
        return None
    
    def AddPortal(self, p_id):
        self.m_room.AddPortal(p_id)
        
    def DelPortal(self, p_id):
        self.m_room.DelPortal(p_id)
        
    def Portals(self):
        return self.m_room.Portals()
    
    def SeekPortal(self, p_name):
        p_name = p_name.lower().strip()
        for i in self.m_room.m_portals:
            if i.GetName().lower() == p_name:
                return i
        for i in self.m_room.m_portals:
            if i.GetName().lower().find(p_name) == 0:
                return i
        return None
    
    def AddLogic(self, p_logic):
        return self.m_room.AddLogic(p_logic)
    
    def AddExistingLogic(self, p_logic):
        return self.m_room.AddExistingLogic(p_logic)
    
    def DelLogic(self, p_logic):
        return self.m_room.DelLogic(p_logic)
    
    def GetLogic(self, p_logic):
        return self.m_room.GetLogic(p_logic)
    
    def HasLogic(self, p_logic):
        return self.m_room.HasLogic(p_logic)
    
    def DoAction(self, p_action, p_data1, p_data2, p_data3, p_data4, p_data):
        if type(p_action) != str:
            return self.m_room.DoAction(p_action)
        else:
            return self.m_room.DoAction(Action(p_action, p_data1, p_data2, p_data3, p_data4, p_data))
        
    def GetLogicAttribute(self, p_logic, p_attr):
        return self.m_room.GetLogicAttribute(p_logic, p_attr)
    
    def AddHook(self, p_hook):
        self.m_room.AddHook(p_hook)
        
    def DelHook(self, p_hook):
        self.m_room.DelHook(p_hook)
        
    def Hooks(self):
        return self.m_room.Hooks()
    
    def KillHook(self, p_act, p_stringdata):
        self.m_room.KillHook(p_act, p_stringdata)
        
    def ClearHooks(self):
        self.m_room.ClearHooks()
        
    def ClearLogicHooks(self, p_logic):
        self.m_room.ClearLogicHooks(p_logic)
        
    def GetAttribute(self, p_name):
        return self.m_room.GetAttribute(p_name)
    
    def SetAttribute(self, p_name, p_val):
        self.m_room.SetAttribute(p_name, p_val)
        
    def HasAttribute(self, p_name):
        return self.m_room.HasAttribute(p_name)
    
    def AddAttribute(self, p_name, p_initialval):
        self.m_room.AddAttribute(p_name, p_initialval)
        
    def DelAttribute(self, p_name):
        self.m_room.DelAttribute(p_name)