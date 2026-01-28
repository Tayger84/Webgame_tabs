def user_validate(
    parsed_overview: dict,
    current_user: dict
) -> bool:
    """
    Check if the user has at least one country in parsed alliance overview
    """
       
    players_in_alliance = { parsed["player"] for parsed in parsed_overview.values() } # set of players in parsed alliance
    
    return current_user["player"] in players_in_alliance #  user's country is present in the overview