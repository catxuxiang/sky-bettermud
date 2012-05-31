'''
Created on 2012-5-31

@author: Sky
'''
from Db.Databases import MapDatabase
from BasicLib.Redis import sr
from Entities.Region import Region
from Db.RoomDatabase import RoomDB
from Db.PortalDatabase import PortalDB
from Db.CharacterDatabase import CharacterDB
from Db.ItemDB import ItemDB

class RegionDatabase(MapDatabase):
    def LoadAll(self):
        folder = "regions"
        for i in sr.llen(folder):
            key = sr.lindex(folder, i)
            self.LoadRegion(key)
            
    def LoadRegion(self, p_name):
        id1 = "0"
        for i in sr.hkeys("regions"):
            if sr.hget("regions", i) == p_name:
                id1 = i
                break
        if id1 == "0":
            raise Exception("Invalid Region Names!")
        
        dir1 = "regions:" + p_name
        regionfilename = dir1 + ":region"
        reg = Region()
        reg.SetId(id1)
        self.LoadEntity(reg, regionfilename)
        reg.SetDiskname(p_name) 
            
        reg.m_rooms = RoomDB.LoadDb(dir1 + ":rooms")
        reg.m_portals = PortalDB.LoadDb(dir1 + ":portals")
        reg.m_characters = CharacterDB.LoadDb(dir1 + ":characters")
        reg.m_items = ItemDB.LoadDb(dir1 + ":items")
        
    def SaveRegion(self, p_id):
        reg = self.Get(p_id)
        sr.hset("regions", p_id, reg.GetDiskname())
        workingdir = "regions:" + reg.GetDiskname()
        regionfilename = workingdir + ":region"
        self.SaveEntity(self, reg, regionfilename)
            
        RoomDB.SaveDb(workingdir + ":rooms", reg.m_rooms)
        PortalDB.SaveDb(workingdir + ":portals", reg.m_portals)
        CharacterDB.SaveDb(workingdir + ":characters", reg.m_characters)
        ItemDB.SaveDb(workingdir + ":items", reg.m_items)  
        
    def SaveAll(self):
        for i in self.m_container.values():
            if i.GetId() != "0":
                self.SaveRegion(i.GetId())
                
RegionDB = RegionDatabase()
