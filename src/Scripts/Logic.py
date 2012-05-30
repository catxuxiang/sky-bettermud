'''
Created on 2012-5-30

@author: Sky
'''
SCRIPTRELOADMODE_LEAVEEXISTING = 0
SCRIPTRELOADMODE_RELOADFUNCTIONS = 1

class Script:
    def Load(self, sr, prefix):
        
         
    {
        // default to empty data loading, by chewing up the [DATA] and
        // [/DATA] tags.
        std::string temp;
        p_stream >> temp >> temp;
    };

    virtual void Save( std::ostream& p_stream ) 
    {
        // default to empty data saving
        p_stream << "[DATA]\n[/DATA]\n";
    };

    virtual std::string Name() = 0;
    virtual ~Script() {};
};  // end class Script
