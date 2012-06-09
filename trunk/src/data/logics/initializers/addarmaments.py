from accessors.CharacterAccessor import character, charactertemplate
from accessors.ItemAccessor import item, itemtemplate
from accessors.GameAccessor import GameWrap

def init():
    mud = GameWrap()

    # add arms to every item
    mud.BeginItem()
    while mud.IsValidItem():
        item = item( mud.CurrentItem() )
        template = itemtemplate( item.TemplateID() )
        if not item.HasAttribute( "arms" ):
            item.AddAttribute( "arms", template.GetAttribute( "arms" ) )
        mud.NextItem()

    # add defaultweapon and weapon to every character
    mud.BeginCharacter()
    while mud.IsValidCharacter():
        character = character( mud.CurrentCharacter() )
        template = charactertemplate( character.TemplateID() )
        if not character.HasAttribute( "defaultweapon" ):
            character.AddAttribute( "defaultweapon", template.GetAttribute( "defaultweapon" ) )
        if not character.HasAttribute( "weapon" ):
            character.AddAttribute( "weapon", template.GetAttribute( "weapon" ) )
        mud.NextCharacter()