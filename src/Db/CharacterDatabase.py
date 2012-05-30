'''
Created on 2012-5-30

@author: Sky
'''
from Db.Databases import TemplateInstanceDatabase
from Entities.Character import Character
class CharacterDatabase(TemplateInstanceDatabase):
    def SavePlayers(self):
        sr = TemplateInstanceDatabase.Sr
        sr.ltrim("PlayerList", 2, 1)
        for i in self.m_instances.values():
            if i.IsPlayer():
                sr.rpush("PlayerList", i.GetId())
                self.SaveEntity(i)
                
    def LoadPlayers(self):
        sr = TemplateInstanceDatabase.Sr
        for i in sr.llen("PlayerList"):
            id1 = sr.lindex("PlayerList", i)
            p = Character()
            p.SetId(id1)
            self.LoadEntity(p)
            
    def LoadTemplates(self):
        
{
    // load a single template file
    m_templates.LoadFile( "data/templates/characters/" + p_file );
}
{
    // load all the players
    m_instances.LoadDirectory( "data/players/" );
}
                

                

    
    
CharacterDB = CharacterDatabase()
    
     
