'''
Created on 2012-5-31

@author: Sky
'''
from Db.Databases import MapDatabase
from Entities.Account import Account
from BasicLib.Redis import sr

class AccountDatabase(MapDatabase):
    def Create(self, g_game, p_name, p_pass):
        id1 = self.FindOpenId()
        
        a = Account()
        a.SetId(id1)
        MapDatabase.Create(self, a)
        a.SetName(p_name)
        a.SetPass(p_pass)
        a.SetLoginTime(g_game.GetTime())
        return id1
    
    def Load(self):
        for i in sr.llen("accounts"):
            id1 = sr.lindex("accounts", i)
            a = Account()
            a.SetId(id1)
            self.LoadEntity(a, "accounts")
            
    def Save(self):
        sr.ltrim("accounts", 2, 1)
        for i in self.m_container.values():
            sr.rpush("accounts", i.GetId())
            self.SaveEntity(i, "accounts")  
            
    def AcceptibleName(self, p_name):
        inv = " \"'~!@#$%^&*+/\\[]{}<>()=.,?;:"
        for i in range(0, len(inv)):
            if p_name.find(inv[i]) != -1:
                return False
            
        if len(p_name) > 16 or len(p_name) < 3:
            return False
        
        if not ((p_name[0] >= "A" and p_name[0]<="Z") or (p_name[0] >= "a" and p_name[0] <= "z")):
            return False
        
        if p_name == "new":
            return False
        
        return True

AccountDB = AccountDatabase()
