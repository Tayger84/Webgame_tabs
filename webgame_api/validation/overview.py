from models import Country, Age

def overview_validate_structure(
    parsed_overview: dict
) -> tuple[bool, list[str]]:
    """
    Validation of the parsed_overview

    True: No errors observed, None
    False: Found error/s, list[errors in string type]
    """
    errors = []
    mandatory_keys = { "alliance", "country_name", "player_name", "regime_short", "regime_full" }
    
    if not parsed_overview:
        errors.append("No data in the inputed File")
        
    if not( 1 <= len(parsed_overview) <= 10 ):
        errors.append("Invalid number of countries in the file")
    
        
    for country in parsed_overview.values():
        if not isinstance(country, dict):
            errors.append("Incorrect country format")
        for key in mandatory_keys:
            if key not in country:
                errors.append(f'Missing mandatory key: {key}')
        
    return not errors, errors
    

def overview_diff_validace(
    parsed_overview: dict,
    db_overview: list[Country], # filtred to one Alliance

) -> dict:
    """
    Check and comparing potencial differencies in the overviews
    
    return: dictionary, keyes: "new", "updated", "remowed"
    """
    changes = {
        "new": [],
        "updated": [],
        "removed": []        
    }

    db_map = { c.number: c for c in db_overview } # create a similar map as parsed_overview is 

    for number, parsed in parsed_overview.items(): # number, { country object }
        if number not in db_map: # check if the number is in the database
            changes["new"].append(parsed)
        else:
            db_country = db_map[number]
            
            if db_country.player != parsed["player_name"] or db_country.regime != parsed["regime_full"] or db_country.name != parsed["country_name"]:
                changes["updated"].append(parsed) # append if there was a change in the parsed data comparing with db data
            
    parsed_overview_keys = parsed_overview.keys() # map all country numbers in the input
    
    for number in db_map.keys():
        # check if the country in db is still in new parsed file
        if number not in parsed_overview_keys:
            changes["removed"].append(db_map[number])
            
    return changes
