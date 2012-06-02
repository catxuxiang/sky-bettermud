'''
Created on 2012-6-2

@author: Sky
'''
from Entities.Entity import HasRegion
from Entities.LogicEntity import LogicEntity
from Entities.DataEntity import DataEntity
from accessors.RegionAccessor import region
from accessors.RoomAccessor import room

class portalentry:
    def __init__(self):
        self.startroom = None
        self.directionname = ""
        self.destinationroom = None
        
    def Load(self, sr, prefix):
        self.startroom = sr.get(prefix + ":STARTROOM")
        self.directionname = sr.get(prefix + ":DIRECTION")
        self.destinationroom = sr.get(prefix + ":DESTROOM")
        
    def Save(self, sr, prefix):
        sr.set(prefix + ":STARTROOM", self.startroom.GetId())
        sr.set(prefix + ":DIRECTION", self.directionname)
        sr.set(prefix + ":DESTROOM", self.destinationroom.GetId())

class Portal(LogicEntity, DataEntity, HasRegion):
    def __init__(self):
        self.m_portals = []
        
    def Load(self, sr, prefix):
        self.Remove()
        
        self.m_region = sr.get(prefix + ":REGION")
        self.m_name = sr.get(prefix + ":NAME")
        self.m_description = sr.get(prefix + ":DESCRIPTION")
        
        self.m_portals = []
        for i in sr.llen(prefix + ":ENTRIES"):
            data = sr.lindex(prefix + ":ENTRIES", i)
            e = portalentry()
            e.Load(sr, prefix + ":" + data)
            self.m_portals.append(e)
            
        self.m_attributes.Load(sr, prefix)
        
        self.m_logic.Load(sr, prefix, self.m_id)
        
        self.Add()
        
    def Save(self, sr, prefix):
        sr.set(prefix + ":REGION", self.m_region.GetId())
        sr.set(prefix + ":NAME", self.m_name)
        sr.set(prefix + ":DESCRIPTION", self.m_description)
        
        sr.ltrim(prefix + ":ENTRIES", 2, 1)
        i = 0
        for portal in self.m_portals:
            sr.rpush(prefix + ":ENTRIES", i)
            portal.Save(sr, prefix + ":ENTRIES:" + i)
            
        self.m_attributes.Save(sr, prefix)
        
        self.m_logic.Save(sr, prefix)
        
    def Remove(self):
        if self.m_region != None:
            reg = region(self.m_region)
            reg.DelPortal(self.m_id)
            
        for i in self.m_portals:
            r = room(i.startroom)
            r.DelPortal(self.m_id)
            
    def Add(self):
        if self.m_region != None:
            reg = region(self.m_region)
            reg.AddPortal(self.m_id)
            
        for i in self.m_portals:
            r = room(i.startroom)
            r.AddPortal(self.m_id)