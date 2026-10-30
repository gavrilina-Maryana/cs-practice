def parse_record(line):
    parts = line.split(';')
    if len(parts) != 3:
        raise ValueError("Invalid fields count")
    
    city, temp_str, date = parts
    
    if not city.strip() or not date.strip():
        raise ValueError("Empty city or date")
        
    try:
        temp = float(temp_str)
    except ValueError:
        raise ValueError("Temp is not a number")
        
    return {"city": city, "temperature": temp, "date": date}


def read_valid(lines):
    valid = []
    for line in lines:
        if line.strip() == "":
            continue
        try:
            record = parse_record(line)
            valid.append(record)
        except ValueError:
            continue
    return valid


def average_by_city(records):
    total = {}
    count = {}
    for rec in records:
        city = rec["city"]
        temp = rec["temperature"] 
        
        total[city] = total.get(city, 0) + temp
        count[city] = count.get(city, 0) + 1
        
    averages = {}
    for city in total:
        averages[city] = round(total[city] / count[city], 1)
    return averages


def warmest_city(records):
    if not records:
        return ""
        
    averages = average_by_city(records)

    sorted_cities = sorted(averages.keys())
    best = sorted_cities[0]
    
    for city in sorted_cities:
        if averages[city] > averages[best]:
            best = city
            
    return best




