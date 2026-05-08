from bs4 import BeautifulSoup


def parse_alliance_table(html_content: str) -> tuple[dict[str], list[str]]:
    """
    Mining data about countries and storing them as snapshot
    
    Return: snapshot of countries as dict
    """
    parsed_keys = []
    soup = BeautifulSoup(html_content, 'lxml')
    
    # find the header for check correct page 
    header = soup.find(['h1', 'h2', 'h3'], string=lambda t: t and "Detaily zemí aliance" in t) # find first "Detaily zemí aliance" in tag regadless on other characters
    if not header:
        return None
    
    # find first table after header "Detaily zemí aliance"
    table = header.find_next("table")
    rows = table.find_all("tr")
    
    # how many countries and storaged td in cells
    cells = rows[0].find_all("td")
    num_countries = len(cells) - 1
    
    # create format for country list(dict{})
    countries = [ {} for _ in range(num_countries) ]
    
    # fill rows in the cell in dictionary
    for row in rows:
        cells = [ c.get_text(strip=True) for c in row.find_all("td") ]
        
        if not cells:
            return None
        
        # header of the property of every country       
        metric_name = cells[0]
        parsed_keys.append(metric_name) # parsed keys for validation snapshot structure
        
        # fill countries via metric_name and cells values
        for i in range(1, len(cells)):
            countries[i-1][metric_name] = cells[i] # duplicity matric_name - in this case the value is stored again in the same key
        
            
    return countries, parsed_keys # dictionary of the snapshot and every keys


