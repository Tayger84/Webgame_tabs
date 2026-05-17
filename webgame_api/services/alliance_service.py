

def get_country_numbers_from_overview(json_data: dict) -> list[int]:
    """
    List of country numbers extraction of the loaded alliance data

    Args:
        json_data (dict): parsed data from overview parser function

    Returns:
        list[int]: list of unordered numbers
    """
    return list(json_data.keys())

def get_country_numbers_from_snapshot(json_data: list) -> list[int]:
    """
    List of country numbers extraction of the loaded alliance snapshot data

    Args:
        json_data (list): list of dictionaries. Every dict is a one country

    Returns:
        list[int]: list of unordered numbers
    """
    pass

def get_county_numbers_from_web() -> list[int]:
    pass