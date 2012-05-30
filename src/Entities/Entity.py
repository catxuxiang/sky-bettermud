'''
Created on 2012-5-29

@author: Sky
'''
maxentityvalue = 0x7FFFFFFF

class Entity:
    def __init__(self):
        self.m_name = "UNDEFINED"
        self.m_description = "UNDEFINED"
        self.m_id = "0"
        self.m_refcount = 0
        
    def GetName(self):
        return self.m_name
    
    def GetDescription(self):
        return self.m_description
    
    def GetId(self):
        return self.m_id
    
    def AddRef(self):
        self.m_refcount += 1
        
    def DelRef(self):
        self.m_refcount -= 1
        
    def GetRef(self):
        return self.m_refcount
    
    def SetName(self, p_name):
        self.m_name = p_name
        
    def SetDescription(self, p_desc):
        self.m_description = p_desc
        
    def SetId(self, p_id):
        self.m_id = p_id
        
class HasRegion:
    def __init__(self):
        self.m_region = None
        
    def GetRegion(self):
        return self.m_region
    
    def SetRegion(self, p_region):
        self.m_region = p_region
        
class HasRoom:
    def __init__(self):
        self.m_room = None
        
    def GetRoom(self):
        return self.m_room
    
    def SetRoom(self, p_room):
        self.m_room = p_room
        
class HasTemplateId:
    def __init__(self):
        self.m_templateid = None
        
    def GetTemplateId(self):
        return self.m_templateid
    
    def SetTemplateId(self, p_templateid):
        self.m_templateid = p_templateid
        
class HasCharacters:
    def __init__(self):
        self.m_characters = []
        
    def AddCharacter(self, p_character):
        self.m_characters.append(p_character)
        
    def DelCharacter(self, p_character):
        i = 0
        index = -1
        for character in self.m_characters:
            if character == p_character:
                index = i
                break
            i += 1
        if index != -1:
            del self.m_characters[index]
            
    def Characters(self):
        return len(self.m_characters)
    
class HasItems:
    def __init__(self):
        self.m_items = []
        
    def AddItem(self, p_item):
        self.m_items.append(p_item)
        
    def DelItem(self, p_item):
        i = 0
        index = -1
        for item in self.m_items:
            if item == p_item:
                index = i
                break
            i += 1
        if index != -1:
            del self.m_items[index]
            
    def Items(self):
        return len(self.m_items)
    
class HasRooms:
    def __init__(self):
        self.m_rooms = []
        
    def AddRoom(self, p_room):
        self.m_rooms.append(p_room)
        
    def DelRoom(self, p_room):
        i = 0
        index = -1
        for item in self.m_rooms:
            if item == p_room:
                index = i
                break
            i += 1
        if index != -1:
            del self.m_rooms[index]
            
    def Rooms(self):
        return len(self.m_rooms)
    
class HasPortals:
    def __init__(self):
        self.m_portals = []
        
    def AddPortal(self, p_portal):
        self.m_portals.append(p_portal)
        
    def DelPortal(self, p_portal):
        i = 0
        index = -1
        for portal in self.m_portals:
            if portal == p_portal:
                index = i
                break
            i += 1
        if index != -1:
            del self.m_portals[index]
            
    def Portals(self):
        return len(self.m_portals)