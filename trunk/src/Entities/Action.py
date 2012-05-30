'''
Created on 2012-5-30

@author: Sky
'''
ENTITYTYPE_CHARACTER = 0
ENTITYTYPE_ITEM = 1
ENTITYTYPE_ROOM = 2
ENTITYTYPE_PORTAL = 3
ENTITYTYPE_REGION = 4

class Action:
    def __init__(self, p_action, p_data1 = 0, p_data2 = 0, p_data3 = 0, p_data4 = 0, p_data = ""):
        self.actiontype = p_action
        self.data1 = p_data1
        self.data2 = p_data2
        self.data3 = p_data3
        self.data4 = p_data4
        self.stringdata = p_data
        
class TimedAction:
    def __init__(self, time, act, p_data1 = 0, p_data2 = 0, p_data3 = 0, p_data4 = 0, p_data = ""):
        self.valid = True
        self.executiontime = time
        if type(act) != str:
            self.actionevent = act
        else:
            self.actionevent = Action(act, p_data1, p_data2, p_data3, p_data4, p_data)
        self.valid = True
        
    def Hook(self):
        if self.actionevent.actiontype == "attemptsay" || actionevent.actiontype == "command" || actionevent.actiontype == "attemptenterportal" || actionevent.actiontype == "attempttransport" || actionevent.actiontype == "transport" || actionevent.actiontype == "destroycharacter":
            
    {
        character( actionevent.data1 ).AddHook( this );
    }
    else if( actionevent.actiontype == "attemptgetitem" ||
             actionevent.actiontype == "attemptdropitem" )
    {
        character( actionevent.data1 ).AddHook( this );
        item( actionevent.data2 ).AddHook( this );
    }
    else if( actionevent.actiontype == "attemptgiveitem" )
    {
        character( actionevent.data1 ).AddHook( this );
        character( actionevent.data2 ).AddHook( this );
        item( actionevent.data3 ).AddHook( this );
    }
    else if( actionevent.actiontype == "destroyitem" )
    {
        item( actionevent.data1 ).AddHook( this );
    }
    else if( actionevent.actiontype == "messagelogic" ||
             actionevent.actiontype == "dellogic" ||
             actionevent.actiontype == "do" ||
             actionevent.actiontype == "modifyattribute" )
    {
        switch( actionevent.data1 )
        {
        case CHARACTER:
            character( actionevent.data2 ).AddHook( this );
            break;
        case ITEM:
            item( actionevent.data2 ).AddHook( this );
            break;
        case ROOM:
            room( actionevent.data2 ).AddHook( this );
            break;
        case PORTAL:
            portal( actionevent.data2 ).AddHook( this );
            break;
        case REGION:
            region( actionevent.data2 ).AddHook( this );
            break;
        }
    }
}

void TimedAction::Unhook()
{
    valid = false;
    if( actionevent.actiontype == "attemptsay" ||
        actionevent.actiontype == "command" ||
        actionevent.actiontype == "attemptenterportal" ||
        actionevent.actiontype == "attempttransport" ||
        actionevent.actiontype == "transport" ||
        actionevent.actiontype == "destroycharacter" )
    {
        character( actionevent.data1 ).DelHook( this );
    }
    else if( actionevent.actiontype == "attemptgetitem" ||
             actionevent.actiontype == "attemptdropitem" )
    {
        character( actionevent.data1 ).DelHook( this );
        item( actionevent.data2 ).DelHook( this );
    }
    else if( actionevent.actiontype == "attemptgiveitem" )
    {
        character( actionevent.data1 ).DelHook( this );
        character( actionevent.data2 ).DelHook( this );
        item( actionevent.data3 ).DelHook( this );
    }
    else if( actionevent.actiontype == "destroyitem" )
    {
        item( actionevent.data1 ).DelHook( this );
    }
    else if( actionevent.actiontype == "messagelogic" ||
             actionevent.actiontype == "dellogic" ||
             actionevent.actiontype == "do" ||
             actionevent.actiontype == "modifyattribute" )
    {
        switch( actionevent.data1 )
        {
        case CHARACTER:
            character( actionevent.data2 ).DelHook( this );
            break;
        case ITEM:
            item( actionevent.data2 ).DelHook( this );
            break;
        case ROOM:
            room( actionevent.data2 ).DelHook( this );
            break;
        case PORTAL:
            portal( actionevent.data2 ).DelHook( this );
            break;
        case REGION:
            region( actionevent.data2 ).DelHook( this );
            break;
        }
    }
}

void TimedAction::Save( std::ofstream& p_stream )
{
    if( !valid )
        return;

    p_stream << "[TIMER]\n";
    p_stream << "    [TIME]                  ";
    BasicLib::insert( p_stream, executiontime );
    p_stream << "\n    [NAME]                  " << actionevent.actiontype << "\n";
    p_stream << "    [DATA1]                 " << actionevent.data1 << "\n";
    p_stream << "    [DATA2]                 " << actionevent.data2 << "\n";
    p_stream << "    [DATA3]                 " << actionevent.data3 << "\n";
    p_stream << "    [DATA4]                 " << actionevent.data4 << "\n";

    // set the string data to "0", so that SOMETHING is written out to disk.
    // writing nothing would be a disaster, because the load function assumes
    // that something is there (whitespace... blah!).
    // note that this is acceptible because if the parameter is "", then
    // it is assumed to be unused anyway, so saving and loading a "0" will
    // make it ignored
    if( actionevent.stringdata == "" )
        actionevent.stringdata = "0";
    p_stream << "    [STRING]                " << actionevent.stringdata << "\n";
    p_stream << "[/TIMER]\n";
}

void TimedAction::Load( std::ifstream& p_stream )
{
    std::string temp;
    p_stream >> temp >> temp;       // "[TIMER]" and "[TIME]"
    BasicLib::extract( p_stream, executiontime );
    p_stream >> temp >> std::ws;
    std::getline( p_stream, actionevent.actiontype );
    p_stream >> temp >> actionevent.data1;
    p_stream >> temp >> actionevent.data2;
    p_stream >> temp >> actionevent.data3;
    p_stream >> temp >> actionevent.data4;
    p_stream >> temp >> std::ws;
    std::getline( p_stream, actionevent.stringdata );
    p_stream >> temp;
}
