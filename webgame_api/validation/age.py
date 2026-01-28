import re

def validate_age(parsed_age: dict) -> bool:
    """Validate the parsed AGE represents a real game AGE

    Args:
        parsed_age (dict): parsed data of the AGE from the https://www.webgame.cz

    Returns:
        True -> valid age ( e. g. 185. věk )
        False -> invalid age (e.g. Mezihra / Invalid data)
    """
    if not parsed_age:
        return None
    
    age_text = parsed_age.get("age")
    
    if not isinstance(age_text, str): # the age must be str
        return False
    
    # valid age contains at least  one digit
    return bool(re.search(r"\d+", age_text))
    