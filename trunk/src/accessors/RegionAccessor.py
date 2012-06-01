'''
Created on 2012-6-1

@author: Sky
'''
from Entities.Action import Action
class region:
    def __init__(self, p_data):
        if type(p_data) == str:
            self.m_region = RegionDB.Get(p_data)
            self.m_region.AddRef()
        else:
            self.m_region.DelRef()
            self.m_region = p_data.m_region
            self.m_region.AddRef()
            
    def __del__(self):
        self.m_region.DelRef()
        
    def GetId(self):
        return self.m_region.GetId()
    
    def GetName(self):
        return self.m_region.GetName()
    
    def GetDescription(self):
        return self.m_region.GetDescription()
    
    def SetId(self, p_id):
        self.m_region.SetId(p_id)
        
    def SetName(self, p_name):
        self.m_region.SetName(p_name)
        
    def SetDescription(self, p_desc):
        self.m_region.SetDescription(p_desc)
        
    def AddItem(self, p_id):
        self.m_region.AddItem(p_id)
        
    def DelItem(self, p_id):
        self.m_region.DelItem(p_id)
        
    def Items(self):
        return self.m_region.m_items
    
    def SeekItem(self, p_name):
        p_name = p_name.lower().strip()
        for i in self.m_region.m_items:
            if i.GetName().lower() == p_name:
                return i
        for i in self.m_region.m_items:
            if i.GetName().lower().find(p_name) == 0:
                return i
        return None
    
    def AddCharacter(self, p_id):
        self.m_region.AddCharacter(p_id)
        
    def DelCharacter(self, p_id):
        self.m_region.DelCharacter(p_id)
        
    def Characters(self):
        return self.m_region.Characters()
    
    def SeekCharacter(self, p_name):
        p_name = p_name.lower().strip()
        for i in self.m_region.m_characters:
            if i.GetName().lower() == p_name:
                return i
        for i in self.m_region.m_characters:
            if i.GetName().lower().find(p_name) == 0:
                return i
        return None
    
    def AddRoom(self, p_id):
        self.m_region.AddRoom(p_id)
        
    def DelRoom(self, p_id):
        self.m_region.DelRoom(p_id)
        
    def Rooms(self):
        return self.m_region.Rooms()
    
    def SeekRoom(self, p_name):
        p_name = p_name.lower().strip()
        for i in self.m_region.m_rooms:
            if i.GetName().lower() == p_name:
                return i
        for i in self.m_region.m_rooms:
            if i.GetName().lower().find(p_name) == 0:
                return i
        return None
    
    def AddPortal(self, p_id):
        self.m_region.AddPortal(p_id)
        
    def DelPortal(self, p_id):
        self.m_region.DelPortal(p_id)
        
    def Portals(self):
        return self.m_region.Portals()
    
    def SeekPortal(self, p_name):
        p_name = p_name.lower().strip()
        for i in self.m_region.m_portals:
            if i.GetName().lower() == p_name:
                return i
        for i in self.m_region.m_portals:
            if i.GetName().lower().find(p_name) == 0:
                return i
        return None
    
    def AddLogic(self, p_logic):
        return self.m_region.AddLogic(p_logic)
    
    def AddExistingLogic(self, p_logic):
        return self.m_region.AddExistingLogic(p_logic)
    
    def DelLogic(self, p_logic):
        return self.m_region.DelLogic(p_logic)
    
    def GetLogic(self, p_logic):
        return self.m_region.GetLogic(p_logic)
    
    def HasLogic(self, p_logic):
        return self.m_region.HasLogic(p_logic)
    
    def DoAction(self, p_action, p_data1, p_data2, p_data3, p_data4, p_data):
        if type(p_action) != str:
            return self.m_region.DoAction(p_action)
        else:
            return self.m_region.DoAction(Action(p_action, p_data1, p_data2, p_data3, p_data4, p_data))
        
    def GetLogicAttribute(self, p_logic, p_attr):
        return self.m_region.GetLogicAttribute(p_logic, p_attr)
    
    def AddHook(self, p_hook):
        self.m_region.AddHook(p_hook)
        
    def DelHook(self, p_hook):
        self.m_region.DelHook(p_hook)
        
    def Hooks(self):
        return self.m_region.Hooks()
    
    def KillHook(self, p_act, p_stringdata):
        self.m_region.KillHook(p_act, p_stringdata)
        
    def ClearHooks(self):
        self.m_region.ClearHooks()
        
    def ClearLogicHooks(self, p_logic):
        self.m_region.ClearLogicHooks(p_logic)
        
    def GetAttribute(self, p_name):
        return self.m_region.GetAttribute(p_name)
    
    def SetAttribute(self, p_name, p_val):
        self.m_region.SetAttribute(p_name, p_val)
        
    def HasAttribute(self, p_name):
        return self.m_region.HasAttribute(p_name)
    
    def AddAttribute(self, p_name, p_initialval):
        self.m_region.AddAttribute(p_name, p_initialval)
        
    def DelAttribute(self, p_name):
        self.m_region.DelAttribute(p_name)