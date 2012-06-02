'''
Created on 2012-6-2

@author: Sky
'''
from Entities.LogicEntity import LogicEntity
from Entities.DataEntity import DataEntity
from Entities.Entity import HasRegion, HasCharacters, HasItems, HasPortals
from accessors.RegionAccessor import region

class Room(LogicEntity, DataEntity, HasRegion, HasCharacters, HasItems, HasPortals):
    def Load(self, sr, prefix):
        self.Remove()
        
        prefix += ":" + self.m_id
        
        self.m_region = sr.get(prefix + ":REGION")
        self.m_name = sr.get(prefix + ":NAME")
        self.m_description = sr.get(prefix + ":DESCRIPTION")
        
        self.m_attributes.Load(sr, prefix)
        
        self.m_logic.Load(sr, prefix, self.m_id)
        
        self.Add()
        
    def Save(self, sr, prefix):
        prefix += ":" + self.m_id
        
        sr.set(prefix + ":REGION", self.m_region.GetId())
        sr.set(prefix + ":NAME", self.m_name)
        sr.set(prefix + ":DESCRIPTION", self.m_description)
        
        self.m_attributes.Save(sr, prefix)
        
        self.m_logic.Save(sr, prefix)
        
    def Add(self):
        if self.m_region != None and self.m_id != "0":
            r = region(self.m_region)
            r.AddRoom(self.m_id)
            
    def Remove(self):
        if self.m_region != None and self.m_id != "0":
            r = region(self.m_region)
            r.DelRoom(self.m_id)
