from webgame_api.models.models import Country, db

def apply_overview_changes(changes, alliance_name, user_id):
    
    """
    Apply overview differences into the database.
    """
    
    # a new country
    for parsed in changes["new"]:
        new_country = Country(
            number = parsed["number"],
            name = parsed["country_name"],
            player = parsed["player_name"],
            alliance = parsed["alliance"],
            regime = parsed["regime_full"],
            user_id = user_id
        )
    
    # update an existing country
    for parsed in changes["update"]:
        pass
    
    # removed countries
    for parsed in changes["removed"]:
        pass
    
    # commit
    db.session.commit()