'''
Created on 2012-5-30

@author: Sky
'''
from Db.Databases import TemplateInstanceDatabase
from Entities.Character import Character, CharacterTemplate
class CharacterDatabase(TemplateInstanceDatabase):
    def SavePlayers(self, prefix):
        sr = TemplateInstanceDatabase.Sr
        sr.ltrim("players", 2, 1)
        for i in self.m_instances.values():
            if i.IsPlayer():
                sr.rpush("players", i.GetId())
                self.SaveEntity(i, "players")
                
    def LoadPlayers(self):
        sr = TemplateInstanceDatabase.Sr
        for i in sr.llen("players"):
            id1 = sr.lindex("players", i)
            p = Character()
            p.SetId(id1)
            self.LoadEntity(p, "players")
            
    def LoadTemplates(self, p_key = ""):
        sr = TemplateInstanceDatabase.Sr
        folder = "templates:characters"
        if p_key == "":
            for i in sr.llen(folder):
                key = sr.lindex(folder, i)
                subfolder = folder + ":" + key
                for j in sr.llen(subfolder):
                    id1 = sr.lindex(subfolder, j)
                    ct = CharacterTemplate()
                    ct.SetId(id1)
                    self.LoadEntityTemplate(ct)
        else:
            subfolder = folder + ":" + p_key
            for j in sr.llen(subfolder):
                id1 = sr.lindex(subfolder, j)
                ct = CharacterTemplate()
                ct.SetId(id1)
                self.LoadEntityTemplate(ct) 
                
    def LoadPlayer(self, p_id):
        p = Character()
        p.SetId(p_id)
        self.LoadEntity(p)   
        
    def FindPlayerFull(self, p_name):
        for i in self.m_instances.values():
            if i.GetName().lower() == p_name.lower().strip():
                return i
        return None
    
    def FindPlayerPart(self, p_name):
        player = self.FindPlayerFull(p_name)
        if player != None:
            return player
        
        for i in self.m_instances.values():
            if i.GetName().lower().find(p_name.lower().strip()) == 0:
                return i
        return None  
    
    def SaveDb(self, folder, m_characters):
        sr = TemplateInstanceDatabase.Sr
        sr.ltrim(folder, 2, 1)
        for i in m_characters:
            sr.rpush(folder, i.GetId())
            self.SaveEntity(i, folder) 
            
    def LoadDb(self, folder):
        sr = TemplateInstanceDatabase.Sr
        characters = []
        for i in range(0, sr.llen(folder)):
            id1 = sr.lindex(folder, i)
            data = Character()
            data.SetId(id1)
            self.LoadEntity(data, folder)
            characters.append(data)
        return characters             

    
    
CharacterDB = CharacterDatabase()
    
     
