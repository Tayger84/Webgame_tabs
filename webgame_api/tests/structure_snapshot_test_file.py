from parsers.snapshot import parse_alliance_table
from services.snapshot_mapping import SNAPSHOT_MAP
from pathlib import Path


def snapshot_validate_structure(parsed_keys: set[str], expected_keys: set[str]) -> tuple[bool, list[str]]:
    
    errors = []
    if not parsed_keys:
        errors.append(f"No parsed keys for comparing")
        return False, errors
    if not expected_keys:
        errors.append(f"No expected keys for comparing")
        return False, errors
    
    missing_keys = expected_keys - parsed_keys
    extra_keys = parsed_keys - expected_keys
    
    if missing_keys:
        errors.append(f"Missing keys in parsed data: {sorted(missing_keys)}")

    if extra_keys:
        errors.append(f"Extra keys in parsed data: {sorted(extra_keys)}")        
        
    return not errors, errors

#### Tested in sructure_snapshot_test_file ####
# def get_country_numbers_from_snapshot(json_data: list) -> list[int]:
#     """
#     List of country numbers extraction of the loaded alliance snapshot data

#     Args:
#         json_data (list): list of dictionaries. Every dict is a one country

#     Returns:
#         list[int]: list of unordered numbers
#     """
#     alliance_countries_numbers = []
    
#     for country in json_data:
#         country_number = int(country["Číslo"])
#         alliance_countries_numbers.append(country_number)

#     return alliance_countries_numbers

#### ####

TEST_DIR = Path(__file__).resolve().parent
file_dir = TEST_DIR / "upload" / "NTRLTY_aliance_detaily.html"

with file_dir.open("r", encoding="utf-8") as snapshot:
    
    html = snapshot.read()
       
parsed_snapshot, snapshot_parsed_keys = parse_alliance_table(html) # one of snapshot of the overview alliance
        
snapshot_expected_keys = set(SNAPSHOT_MAP.keys()) # get keys for structure check of the snapshost
# print(parsed_snapshot)
     
is_valid, snapshost_structure_errors = snapshot_validate_structure(set(snapshot_parsed_keys), snapshot_expected_keys)

list_countries = get_country_numbers_from_snapshot(parsed_snapshot)

print(list_countries)
# print(snapshost_structure_errors)

