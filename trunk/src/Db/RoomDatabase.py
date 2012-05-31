'''
Created on 2012-5-31

@author: Sky
'''
from Db.Databases import MapDatabase
from BasicLib.Redis import sr
from Entities.Room import Room

class RoomDatabase(MapDatabase):
    def SaveDb(self, folder, p_rooms):
        sr.ltrim(folder, 2, 1)
        for i in p_rooms:
            sr.rpush(folder, i.GetId())
            self.SaveEntity(i, folder)
            
    def LoadDb(self, folder):
        rooms = []
        for i in range(0, sr.llen(folder)):
            id1 = sr.lindex(folder, i)
            data = Room()
            data.SetId(id1)
            self.LoadEntity(data, folder)
            rooms.append(data)
        return rooms

RoomDB = RoomDatabase()
