from parsers.overview import parse_alliance_overview
#from validation.overview import overview_validate_structure

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
        return errors
        
    if not( 1 <= len(parsed_overview) <= 10 ):
        errors.append("Invalid number of countries in the file")
            
    for country, country_keys in parsed_overview.items():

        if not isinstance(country_keys, dict):
            errors.append("Incorrect country format")
        for key in mandatory_keys:
            if key not in country_keys:
                errors.append(f'Country: {country}. Missing mandatory key: {key}')
        
    return not errors, errors

def get_country_numbers_from_overview(json_data: dict) -> list[int]:
    """
    List of country numbers extraction of the loaded alliance data

    Args:
        json_data (dict): parsed data from overview parser function

    Returns:
        list[int]: list of unordered numbers
    """
    
    return list(json_data.keys())

with open("upload/NTRLTY_aliance.html", "r") as snapshot:
    
    html = snapshot.read()
    
parsed_overview = parse_alliance_overview(html)

is_valid, errors = overview_validate_structure(parsed_overview)

countries = get_country_numbers_from_overview(parsed_overview)
print(countries)
