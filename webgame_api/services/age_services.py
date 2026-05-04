from models import Age
from datetime import datetime
import re

def build_new_age(parsed_age: dict) -> Age:
    
    return Age(
        age_number=parsed_age["age"],
        start_age=parsed_age["start_age"],
        end_age=parsed_age["end_age"],
        remain_time=parsed_age.get("rest_time"),
        is_active=True
    )

def get_or_create_age(parsed_age: dict, db) -> Age:
    """
    Returns active Age object for current parsed age.

    Create a new Age when: 
    - no Active Age exists,
    - the same Age was restarted,
    - new Age has started.
    """
    active_age = Age.query.filter_by(is_active=True).first() # první aktivní věk, pokud existuje
    
    if not active_age:
        
        new_age = build_new_age(parsed_age)
        db.session.add(new_age)
        db.session.commit()
        return new_age
        
    if active_age.age_number == parsed_age["age"]:
        same_content = (active_age.start_age == parsed_age["start_age"] and active_age.end_age == parsed_age["end_age"])
        
        if same_content:
            return active_age
        else:
            # same age label, but different content -> reset detected
            active_age.is_active = False
            new_age = build_new_age(parsed_age)
            db.session.add(new_age)
            db.session.commit()
            return new_age
        
    
    # different age label -> new Age
    Age.query.filter_by(is_active=True).update({"is_active": False})
    new_age = build_new_age(parsed_age)
    db.session.add(new_age)
    db.session.commit()  
    return new_age
 
