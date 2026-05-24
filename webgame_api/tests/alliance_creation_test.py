import ast
from pathlib import Path

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
    alliance_countries_numbers = []
    
    for country in json_data:
        country_number = int(country["Číslo"])
        alliance_countries_numbers.append(country_number)

    return alliance_countries_numbers


# Test alliance creation based on country numbers

TEST_DIR = Path(__file__).resolve().parent
file_path = TEST_DIR / "upload" / "overview_data.txt"

with file_path.open("r", encoding="utf-8") as f:
    
    file_data = f.read()
    
data = ast.literal_eval(file_data)

list_of_countries = get_country_numbers_from_overview(data)
print(list_of_countries)
