def parse_record(line: str) -> dict:
    fields = line.split(';')
    if len(fields) != 3:
        raise ValueError(f"Неверное количество полей: {len(fields)}. Ожидается 3.")
    city, temp_str, date = fields
    if not city or not date:
        raise ValueError("Город и дата не могут быть пустыми.")
    try:
        temperature = float(temp_str)
    except ValueError:
        raise ValueError(f"Температура '{temp_str}' не является числом.")
    return {'city': city, 'temperature': temperature, 'date': date}

def read_valid(lines: list[str]) -> list[dict]:
    valid_records =
    for line in lines:
        if line.strip():  # Пропускаем пустые строки
            try:
                record = parse_record(line)
                valid_records.append(record)
            except ValueError as e:
                print(f"Пропущена строка: {line} — {e}")
    return valid_records 

def average_by_city(records: list[dict]) -> dict:
    totals = {}
    count = {}
    for record in records:
        city = record['city']
        totals[city] = totals.get(city, 0) + record['temperature']
        count[city] = count.get(city, 0) + 1
    return {city: total / count for city, total in totals.items()}

def warmest_city(records: list[dict]) -> str:
    warmest = None
    max_avg = None
    for record in records:
        avg = record['temperature'] / count[record['city']]  # Учитываем, что count[record['city']])
        if warmest is None or avg > max_avg or (avg == max_avg and record['city'] < warmest):
            warmest = record['city']
            max_avg = avg
    return warmest
