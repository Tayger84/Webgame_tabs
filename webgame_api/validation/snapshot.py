import hashlib
from models.models import Snapshot
from services.snapshot_mapping import snapshot_map

def snapshot_validate_structure(parsed_snapshot: dict) -> tuple[bool, list[str]]:
    
    errors = []
    
    if not parsed_snapshot or not snapshot_map:
        errors.append("No data in the inputed Files")
        return
    
    parsed_keys = parsed_snapshot[0].keys()
    mapped_keys = snapshot_map.keys() # used for driving loop
    
    for key in mapped_keys:
        if key not in parsed_keys:
            pass
    pass

def prepare_snapshot_for_hash(parsed_json: dict, static_keys: set) -> str:
    """function prepared hash string for next processing

    Args:
        parsed_json (dict): source of data for hash
        static_keys (set): only static data si useable for the hash preparation

    Returns:
        str: hash string cleared from dynamic data and used static data only
    """
    
    result = "" 
        
    for key in sorted(static_keys):

        if key in parsed_json:
            result += f"{key}={parsed_json[key]}|"
        else: 
            result += f"{key}=None"       
            
    return result[:-1]

def compute_snapshot_hash(snapshot_string: str) -> str:
    return hashlib.sha256(snapshot_string.encode("utf-8")).hexdigest()


def snapshot_validate(
    parsed_country_json: dict,
    country_id: int,
    age_id: int,
    static_keys: set,
    existing_snapshots: list[Snapshot]
) -> bool:
    
    """
    Decide whether a snapshot is new or already stored.
        :param existing_snapshots: snapshots for ONE country in ONE age

    Returns:
        True: The hash is not in db
        False: The has has been stored in db
    """
    # prepare deterministic string
    snapshot_string = prepare_snapshot_for_hash(parsed_country_json, static_keys)
    
    # compute hash
    new_hash = compute_snapshot_hash(snapshot_string)

    # load existing hashes from DB
    existing_hashes = {
        snapshot.snapshot_hash for snapshot in existing_snapshots
    }
    
    return new_hash not in existing_hashes
