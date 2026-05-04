import requests
from bs4 import BeautifulSoup

def parse_age():
    
    try:
        response = requests.get('https://www.webgame.cz/', timeout=5)
    except requests.RequestException:
        return None
        
    soup = BeautifulSoup(response.text, "lxml")
    theme_header = soup.find(id="theme")
    time_data = theme_header.find_all("strong")
    
    t_data = [ data.get_text(strip=True) for data in time_data ]
 
    if len(t_data) < 4:
        return None
 
    age_time_data = {
        "age": t_data[0],
        "start_age": t_data[1],
        "end_age": t_data[2],
        "rest_time": t_data[3]
    }

    return age_time_data  # age: 185 věk, start_age: ...

    