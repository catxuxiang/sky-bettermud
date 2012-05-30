'''
Created on 2012-5-30

@author: Sky
'''
from Entities.Entity import Entity
class LogicEntity(Entity):
    def AddLogic(self, p_logic):
        try:
            self.m_logic.Add(p_logic, self.m_id)
            return True
        except Exception:
            pass
        return False
    
    def AddExistingLogic(self, p_logic):
        try:
            self.m_logic.AddExisting(p_logic)
            return True
        except Exception:
            pass
        return False

    def DelLogic(self, p_logic):
        try:
            self.ClearLogicHooks(p_logic)
            
            self.m_logic.Del(p_logic)
            return True
        except Exception:
            pass
        return False
    
    def GetLogic(self, p_logic):
        return self.m_logic.Get(p_logic)
    
    def HasLogic(self, p_logic):
        try:
            return self.m_logic.Has(p_logic)
        except Exception:
            pass
        return False
    
    def DoAction(self, p_action):
        return self.m_logic.DoAction(p_action)
    
    def DoAction(self, p_act, p_data1 = 0, p_data2 = 0, p_data3 = 0, p_data4 = 0, p_data = ""):
        return self.m_logic.DoAction(Action(p_act, p_data1, p_data2, p_data3, p_data4, p_data))

