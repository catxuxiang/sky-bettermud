'''
Created on 2012-5-30

@author: Sky
'''
class LogicCollection:
    def Get(self, p_name):
        return self.m_collection.Get(p_name)
    
    def AddExisting(self, l):
        self.m_collection.Add(l.GetName(), l)
        
    def Add(self, p_name, p_id):
        l = LogicDB.generate( p_name, p_id );
    AddExisting( l );
}

void LogicCollection::Del( const std::string& p_name )
{
    Logic* l = m_collection.Get( p_name );
    delete l;
    m_collection.Del( p_name );
}

bool LogicCollection::Has( const std::string& p_name )
{
    return m_collection.Has( p_name );
}

int LogicCollection::Attribute( 
    const std::string& p_module, 
    const std::string& p_attr )
{
    return m_collection.Get( p_module )->Attribute( p_attr );
}

int LogicCollection::DoAction( const Action& p_action ) 
{
    for( iterator itr = m_collection.begin(); itr != m_collection.end(); ++itr )
    {
        int i = (itr->second)->DoAction( p_action );
        if( i != 0 )
            return i;
    }
    return 0;
}


void LogicCollection::Load( std::istream& p_stream, entityid p_id )
{
    std::string temp;
    p_stream >> temp;       // chew up the "[LOGICS]"
    p_stream >> temp;       // load in the first logic name

    // loop while there are logic modules available
    while( temp != "[/LOGICS]" )
    {
        Add( temp, p_id );
        Logic* c = Get( temp );
        c->Load( p_stream );
        p_stream >> temp;       // try reading next logic name
    }
}

void LogicCollection::Save( std::ostream& p_stream )
{
    p_stream << "[LOGICS]\n";
    iterator itr = begin();
    while( itr != end() )
    {
        // make sure you can save the logic module first
        if( itr->second->CanSave() )
        {
            p_stream << itr->second->Name() << "\n";
            itr->second->Save( p_stream );
        }
        ++itr;
    }
    p_stream << "[/LOGICS]\n";
}



LogicCollection& LogicCollection::operator=( const LogicCollection& p_right )
{
    if( m_collection.size() )
        throw Exception( "ERROR: COPYING OVER LOGIC COLLECTION IS NOT ALLOWED!" );

    LogicCollection& l = const_cast<LogicCollection&>( p_right );
    m_collection = l.m_collection;
    l.m_collection.Clear();

    return *this;
}

LogicCollection::LogicCollection( const LogicCollection& p_right )
{
    LogicCollection& l = const_cast<LogicCollection&>( p_right );
    m_collection = l.m_collection;
    l.m_collection.Clear();
}
