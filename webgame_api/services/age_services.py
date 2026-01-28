from models import Age
from datetime import datetime
import re

def get_or_create_age(parsed_age: dict, db) -> Age:
    """
    Returns active Age object for current parsed age.
    Create new Age if not exists.
    """
    age_number = parsed_age["age"]
    
    age = Age.query.filter_by(age_number=age_number).first()
    
    if age:
        return age
    
    # deactivate old ages
    Age.query.filter_by(is_active=True).update({"is_active": False})
    
    age = Age(
        age_number = parsed_age["age"],
        start_age = parsed_age["start_age"],
        end_age = parsed_age["end_age"],
        remain_time = parsed_age.get("rest_time"),
        is_active = True
    )
    
    db.session.add(age)
    db.session.commit()
    
    return age

def resolve_age(parsed_age_string: str) -> Age | None:
    """ Checking the AGE if it is correct and active in db or its a new one or disactive 
        return Objet | None
    """
    
    age_text = parsed_age_string.strip()
    
    if not re.search(r"\d", age_text):
        return None # no age, just another form of game
    
    age = Age.query.filter_by(age_number=age_text).first()
    
    if age and age.is_active:
        return age
    
    return None


