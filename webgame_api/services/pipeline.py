from dataclasses import dataclass
from typing import Any

from parsers.age import parse_age
from parsers.overview import parse_alliance_overview
from parsers.snapshot import parse_alliance_table

from validation.overview import overview_diff_validace, overview_validate_structure
from validation.snapshot import prepare_snapshot_for_hash, compute_snapshot_hash, snapshot_validate, snapshot_validate_structure
from validation.user import user_validate

from models import models
from age_services import get_or_create_age

@dataclass
class PipelineResult:
    ok: bool
    errors: list[str]
    snapshot_hash: str | None = None

def sync_pipeline(user_id, alliance_id, db, overview_html = None, snapshot_html = None) -> PipelineResult:
    
    # 0) something must be transmited
    if not overview_html and not snapshot_html:
        return PipelineResult(ok=False, errors=["No input HTML provided(overview_html/snaphost_html)."])
    
    parsed_overview = None
    parsed_snapshot = None
    overview_errors = None
    snapshost_errors = None
    
    # 1) Parsed input data from stored html, one of inputs is necessary for proceeding 
    if overview_html:
        parsed_overview = parse_alliance_overview(overview_html) # overview of alliance
        overview_errors = overview_validate_structure(parsed_overview)
        
        
    if snapshot_html:
        parsed_snapshot = parse_alliance_table(snapshot_html) # one of snapshot of the overview alliance
        snapshost_errors = snapshot_validate_structure(parsed_snapshot)
        
    # 2) Age - gets number of AGE for storing in database
    parsed_age = parse_age()
    if not parsed_age:
        return PipelineResult(ok=False, errors=["Failed to parse age data."])
    
    current_age = get_or_create_age(parsed_age, db) 
    
    return PipelineResult(ok=True, errors=[])
    
    
   
   
if __name__ == "__main__":
    
    pass
        
    
# def run(user_id, alliance_id, overview_html = None, snapshot_html = None):
    
    

#     parsed_overview = None
#     parsed_snapshot = None
#     parsed_age = None

#     # 1) Parse
#     if overview_html:
#         parsed_overview = parse_alliance_overview(overview_html) 
        
#     if snapshot_html:
#         parsed_snapshot = parse_alliance_table(snapshot_html) 
        
#     # 2) AGE



    
    
