'''
Created on 2012-5-30

@author: Sky
'''
from Entities.Entity import Entity, HasCharacters
from Entities.Attributes import accesslevel_Peon
class Account(Entity, HasCharacters):
    def __init__(self):
        self.m_password = "UNDEFINED"
        self.m_logintime = 0
        self.m_accesslevel = accesslevel_Peon
        self.m_allowedcharacters = 2
        self.m_banned = False
        
    def GetPassword(self):
        return self.m_password
    
    def GetLoginTime(self):
        return self.m_logintime
    
    def GetAccessLevel(self):
        return self.m_accesslevel
    
    def GetBanned(self):
        return self.m_banned
    
    def GetAllowedCharacters(self):
        return self.m_allowedcharacters
    
    def SetPass(self, p_pass):
        self.m_password = p_pass
        
    def SetLoginTime(self, p_time):
        self.m_logintime = p_time
        
    def SetAccessLevel(self, p_level):
        self.m_accesslevel = p_level
        
    def SetBanned(self, p_banned):
        self.m_banned = p_banned
        
    def SetAllowedCharacters(self, p_num):
        self.m_allowedcharacters = p_num
        
    def Load(self, sr):
        id1 = self.GetId()
        self.m_name = sr.get("Account:" + id1 + ":NAME")
        self.m_password = sr.get("Account:" + id1 + ":PASS")
        self.m_logintime = int(sr.get("Account:" + id1 + ":FIRSTLOGINTIME"))
        self.m_accesslevel = int(sr.get("Account:" + id1 + ":ACCESSLEVEL"))
        self.m_allowedcharacters = int(sr.get("Account:" + id1 + ":ALLOWEDCHARS"))
        self.m_banned = sr.get("Account:" + id1 + ":BANNED")
        if (self.m_banned == "False"):
            self.m_banned = False
        else:
            self.m_banned = True
            
        characters = sr.get("Account:" + id1 + ":CHARACTERS").split(" ")
        self.m_characters = []
        for i in characters:
            if i != "0":
                self.m_characters.append(i)
                
    def Save(self, sr):
        id1 = self.GetId()
        sr.set("Account:" + id1 + ":NAME", self.m_name)
        sr.set("Account:" + id1 + ":PASS", self.m_password)
        sr.set("Account:" + id1 + ":FIRSTLOGINTIME", str(self.m_logintime))
        sr.set("Account:" + id1 + ":ACCESSLEVEL", str(self.m_accesslevel))
        sr.set("Account:" + id1 + ":ALLOWEDCHARS", str(self.m_allowedcharacters))
        sr.set("Account:" + id1 + ":BANNED", str(self.m_banned))
        
        string = ""
        for i in self.m_characters:
            string += i + " "
        string += "0"
        sr.set("Account:" + id1 + ":CHARACTERS", string)



