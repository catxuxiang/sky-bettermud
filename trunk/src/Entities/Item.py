'''
Created on 2012-6-1

@author: Sky
'''
from Entities.Entity import Entity, HasRoom, HasRegion, HasTemplateId
from Entities.DataEntity import DataEntity
from Entities.LogicEntity import LogicEntity
from accessors.CharacterAccessor import character
from accessors.RegionAccessor import region
from accessors.RoomAccessor import room

class ItemTemplate(Entity, DataEntity):
    def __init__(self):
        self.m_isquantity = False
        self.m_quantity = 1
        self.m_logics = []
        
    def IsQuantity(self):
        return self.m_isquantity
    
    def GetQuantity(self):
        return self.m_quantity
    
    def Load(self, sr, prefix):
        self.m_name = sr.get(prefix + ":NAME")
        self.m_description = sr.get(prefix + ":DESCRIPTION")
        self.m_isquantity = sr.get(prefix + ":ISQUANTITY")
        if self.m_isquantity == "False":
            self.m_isquantity = False
        else:
            self.m_isquantity = True
        self.m_quantity = int(sr.get(prefix + ":QUANTITY"))
        
        self.Load(sr, prefix)
        
        logics = sr.get(prefix + ":LOGICS").split(" ")
        self.m_logics = []
        for i in logics:
            self.m_logics.append(i)
    
    def GetName(self):
        if self.m_isquantity:
            return self.m_name.replace("<#>", str(self.m_quantity))
        else:
            return self.m_name


    
class Item(LogicEntity, DataEntity, HasRoom, HasRegion, HasTemplateId):
    def __init__(self):
        self.m_isquantity = False
        self.m_quantity = 1
        
    def IsQuantity(self):
        return self.m_isquantity
    
    def GetQuantity(self):
        return self.m_quantity
    
    def SetQuantity(self, p_quantity):
        self.m_quantity = p_quantity
        
    def LoadTemplate(self, p_template):
        self.m_templateid = p_template.GetId()
        self.m_name = p_template.GetName()
        self.m_description = p_template.GetDescription()
        self.m_isquantity = p_template.m_isquantity
        self.m_quantity = p_template.m_quantity
        self.m_attributes = p_template.m_attributes
        
        for i in p_template.m_logics:
            self.AddLogic(i)
            
    def Load(self, sr, prefix):
        prefix += ":" + self.GetId()
        self.Remove()
        
        self.m_name = sr.get(prefix + ":NAME")
        self.m_description = sr.get(prefix + ":DESCRIPTION")
        self.m_room = sr.get(prefix + ":ROOM")
        self.m_region = sr.get(prefix + ":REGION")
        self.m_isquantity = sr.get(prefix + ":ISQUANTITY")
        if self.m_isquantity == "False":
            self.m_isquantity = False
        else:
            self.m_isquantity = True
        self.m_quantity = int(sr.get(prefix + ":QUANTITY"))
        
        self.m_templateid = sr.get(prefix + ":TEMPLATEID")
        
        self.m_attributes.Load(sr, prefix)
        
        self.m_logic.Load(sr, prefix, self.m_id)
        
        self.Add()
        
    def Save(self, sr, prefix):
        prefix += ":" + self.GetId()
        sr.set(prefix + ":NAME", self.m_name)
        sr.set(prefix + ":DESCRIPTION", self.m_description)
        sr.set(prefix + ":ROOM", self.m_room.GetId())
        sr.set(prefix + ":REGION", self.m_region.GetId())
        sr.set(prefix + ":ISQUANTITY", str(self.m_isquantity))
        sr.set(prefix + ":QUANTITY", str(self.m_quantity))
        sr.set(prefix + ":TEMPLATEID", self.m_templateid)
        
        self.m_attributes.Save(sr, prefix)
        
        self.m_logic.Save(sr, prefix)
        
    def Add(self):
        if self.m_region == None:
            # when regions are 0, that means the item is on a character
            c = character(self.m_room)
            c.AddItem(self.m_id)
        else:
            reg = region(self.m_region)
            reg.AddItem(self.m_id)
            
            r = room(self.m_room)
            r.AddItem(self.m_id)
            
    def Remove(self):
        if self.m_room == None:
            return
        
        # when regions are 0, that means the item is on a character
        if self.m_region == None:
            c = character(self.m_room)
            c.DelItem(self.m_id)
        else:
            reg = region(self.m_region)
            reg.DelItem(self.m_id)
            
            r = room(self.m_room)
            r.DelItem(self.m_id)