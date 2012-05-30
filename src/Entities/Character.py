'''
Created on 2012-5-30

@author: Sky
'''
from Entities.Entity import Entity, HasRoom, HasRegion, HasTemplateId, HasItems
from Entities.DataEntity import DataEntity
class CharacterTemplate(Entity, DataEntity):
    def __init__(self):
        Entity.__init__(self)
        self.m_commands = []
        self.m_logics = []
        
    def Load(self, sr):
        id1 = self.GetId()
        self.m_name = sr.get("CharacterTemplate:" + id1 + ":NAME")
        self.m_description = sr.get("CharacterTemplate:" + id1 + ":DESCRIPTION")
        
        self.m_attributes.Load("CharacterTemplate:" + id1 + ":")
        
        commands = sr.get("CharacterTemplate:" + id1 + ":COMMANDS").split(" ")
        self.m_commands = []
        for i in commands:
            self.m_commands.append(i)
            
        logics = sr.get("CharacterTemplate:" + id1 + ":LOGICS").split(" ")
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

    CharacterTemplate::names::const_iterator itr = p_template.m_commands.begin();
    while( itr != p_template.m_commands.end() )
    {
        AddCommand( *itr );
        ++itr;
    }

    itr = p_template.m_logics.begin();
    while( itr != p_template.m_logics.end() )
    {
        AddLogic( *itr );
        ++itr;
    }
}            

    
