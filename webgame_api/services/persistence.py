from webgame_api.models.models import Country, db

def apply_overview_changes(changes, alliance_name):
    
    """
    changes = {
        "new": [...],
        "updated": [...],
        "removed": [...]        
    }
    
    parsed = {
    "alliance": "...",
    "country_name": "...",
    "player_name": "...",
    "regime_short": "...",
    "regime_full": "..."
}
    """
    
    # a new country
    for parsed in changes["new"]:
        pass
    
    # update an existing country
    for parsed in changes["update"]:
        pass
    
    # removed countries
    for parsed in changes["removed"]:
        pass
    
    # commit
    db.session.commit()