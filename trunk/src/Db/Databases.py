'''
Created on 2012-5-30

@author: Sky
'''
from BasicLib.Redis import sr
class Database:
    def Size(self):
        return len(self.m_container)
    
    def Create(self, p_item):
        raise Exception("Abstract Method!")
    
    
    def LoadEntity(self, p_entity):
        self.Create(p_entity)
        p_entity.Load(sr)

    def SaveEntity(self, p_entity):
        p_entity.Save(sr)
        
    def Purge(self):
        raise Exception("Abstract Method!")

class VectorDatabase:
    def __init__(self):
        self.m_container = []
        
    def IsValid(self, p_id):
        p_id = int(p_id)
        return p_id <= len(self.m_container) and p_id != 0
    
    def Get(self, p_id):
        p_id = int(p_id)
        if p_id > len(self.m_container) or p_id == 0:
            raise Exception("Out of bounds error in vector database")

        if self.m_container[p_id - 1].GetId() == "0":
            raise Exception("Invalid Item in vector database")

        return self.m_container[p_id - 1]

    def Create(self, p_item):
        self.m_container.append(p_item)
        
    def FindName(self, p_name):
        for i in self.m_container:
            if i.GetName().lower() == p_name.lower().strip():
                return i
        return None
    
    def Purge(self):
        self.m_container = []  
    
class MapDatabase:
    def __init__(self):
        self.m_container = {}
        
    def IsValid(self, p_id):
        p_id = int(p_id)
        return p_id > 0 and p_id <= len(self.m_container)
    
    def Get(self, p_id):
        if int(p_id) <= 0 or int(p_id) > len(self.m_container):
            raise Exception("Out of bounds error in map database")
        else:
            return self.m_container[p_id]
        
    def Create(self, p_item):
        self.m_container[p_item.GetId()] = p_item
        
    def Erase(self, p_id):
        if int(p_id) <= 0 or int(p_id) > len(self.m_container):
            raise Exception("Out of bounds error in map database")
        else:
            del self.m_container[p_id]
            
    def FindOpenId(self):
        if len(self.m_container) == 0:
            return "1"
        id1 = 0
        for i in self.m_container.keys():
            if int(i) > id1:
                id1 = int(i)
        return str(id1 + 1)
    
    def FindName(self, p_name):
        for i in self.m_container.values():
            if i.GetName().lower() == p_name.lower().strip():
                return i
        return None
    
    def Purge(self):
        self.m_container = {}    
    
class TemplateInstanceDatabase:
    Sr = sr
    def __init__(self):
        self.m_templates = VectorDatabase()
        self.m_instances = MapDatabase()
        self.m_cleanup = []
                
    def Get(self, p_id):
        for i in self.m_cleanup:
            if i.GetId() == p_id:
                raise Exception("Template Instance Database: Cleaned Up Item Reference!")
        return self.m_instances.Get(p_id)
    
    def Size(self):
        return len(self.m_instances)
    
    def SizeTemplates(self):
        return len(self.m_templates)
    
    def GetTemplate(self, p_id):
        return self.m_templates.Get(p_id)
    
    #This method perhaps havs some errors!
    def Generate(self, p_templateId, p_item):
        id1 = self.m_instances.FindOpenId()
        p_item.SetId(id1)
        self.m_instances.Create(p_item)

        p_item.LoadTemplate(self.m_templates.Get(p_templateId))
        return id1
    
    def Erase(self, p_id):
        self.m_cleanup.append(p_id)
        
    def Cleanup(self):
        for i in self.m_cleanup:
            self.m_instances.Erase(i)
        self.m_cleanup = []
        
    def FindName(self, p_name):
        return self.m_instances.FindName(p_name)
    
    def LoadEntityTemplate(self, p_entity):
        self.m_templates.LoadEntity(p_entity)
        
    def SaveEntityTemplate(self, p_entity):
        self.m_templates.SaveEntity(p_entity)
        
    def LoadEntity(self, p_entity):
        self.m_instances.LoadEntity(p_entity)
        
    def SaveEntity(self, p_entity):
        self.m_instances.SaveEntity(p_entity)

    def Purge(self):
        self.m_templates.Purge()
        self.m_instances.Purge()
        
    def IsValid(self, p_id):
        for i in self.m_cleanup:
            if i == p_id:
                return False
        return self.m_instances.IsValid(p_id)
