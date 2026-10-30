def parse_record(line):
    line = line.split(';')
    if len(line) != 3:
        raise ValueError
    else:
        c, t, d = line
        return c, t, d


def check_lines(lines):
    total = {}
    count = {}
    for line in lines:
        if line.strip() == "":
            continue
        
        try:
            c, t, d = parse_record(line)
            temp = float(t)
        except ValueError:
            continue
        else:
            total[c] = total.get(c, 0) + temp
            count[c] = count.get(c, 0) + 1
            
    averages = {}
    for c in total:
        averages[c] = round(total[c] / count[c], 1)
        
    return averages


def warmest_city(records):

    if not records:
        return ""
    
    cities = sorted(records.keys())
    best = cities[0]
    for c in cities:
        if records[c] > records[best]:
            best = c
    return best





