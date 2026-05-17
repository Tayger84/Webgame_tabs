from parsers.snapshot import parse_alliance_table
from services.snapshot_mapping import SNAPSHOT_MAP


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


with open("upload/NTRLTY_aliance_detaily.html", "r") as snapshot:
    
    html = snapshot.read()
       
parsed_snapshot, snapshot_parsed_keys = parse_alliance_table(html) # one of snapshot of the overview alliance
        
snapshot_expected_keys = set(SNAPSHOT_MAP.keys()) # get keys for structure check of the snapshost
print(parsed_snapshot)
     
is_valid, snapshost_structure_errors = snapshot_validate_structure(set(snapshot_parsed_keys), snapshot_expected_keys)
        
print(snapshost_structure_errors)

