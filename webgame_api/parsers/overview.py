import re
from bs4 import BeautifulSoup
# import upload

def parse_alliance_overview(html_content) -> list[dict]:
    soup = BeautifulSoup(html_content, "lxml")
    
    # find the header for check correct page
    header = soup.find('h2', string=lambda t: t and "Alianční bonusy" in t)
    if not header:
        return None
     
    regimes_dict = {
        "Demo": "Demokracie",
        "Rep": "Republika",
        "Dikt": "Diktatura",
        "Fund": "Fundamentalismus",
        "Kom": "Komunismus",
        "Feud": "Feudalismus",
        "Utop": "Utopie",
        "Robo": "Robokracie",
        "Anar": "Anarchie",
        "Tech": "Technokracie"
    }
    
    # get a aliance name header and its name
    alliance_name_header = soup.find("h1")
    alliance_name = alliance_name_header.get_text(strip=True)
    
    # get correct ali table without <th> headers
    table = alliance_name_header.find_next("table")
    rows = [ tr for tr in table.find_all("tr") if tr.find("a") ] # <tr><td><a>
    
    result = {}
    
    for row in rows:
                
        links = [ 
                 a for a in row.find_all("a")
                 if not a.find("img") # links without img inside
                 ] 
        if len(links) <2:
            continue
        
        # get names and number of country and player
        country_text = links[0].get_text(strip=True)
        player_name = links[1].get_text(strip=True).lstrip("- ")

        # extract number from contry_text (#xxx)
        number_match = re.search(r"\(#(\d+)\)", country_text)
        if not number_match:
            continue
        country_number = int(number_match.group(1))
        
        # extract name from country_text xxx(#xxx)
        country_name = country_text.split("(")[0].strip()
        
        # clean cells for the correct regime extraction
        clean_cells = [
            td for td in row.find_all("td")
            if not td.find(["img", "sup", "span"])
        ] 
        
        regime_short = None
        
        for td in clean_cells:
            text = td.get_text(strip=True).capitalize()
            if text in regimes_dict:
                regime_short = text
                break
            
        regime = regimes_dict.get(regime_short, None)
        
        if regime is None:
            print(f"[WARN] Zřízení nenalezeno: země '{country_name}', číslo {country_number}, hodnota='{regime_short}")
        
        result[country_number] = {
            "alliance": alliance_name,
            "country_name": country_name,
            "player_name": player_name,
            "regime_short": regime_short,
            "regime_full": regime
        }

    return result

