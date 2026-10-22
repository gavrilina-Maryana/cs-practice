# stats.py

def parse_record(line: str) -> dict:
    """Разбирает одну строку и возвращает словарь."""
    # 1. Разбиваем строку по точке с запятой
    parts = line.split(";")
    
    # 2. Проверяем, что частей ровно три
    if len(parts) != 3:
        raise ValueError(f"Ожидалось 3 поля, получено {len(parts)}: {line}")
    
    city, temp_str, date = parts
    
    # 3. Проверяем, что город и дата не пустые
    if not city.strip() or not date.strip():
        raise ValueError(f"Пустой город или дата: {line}")
    
    # 4. Проверяем, что температура — это число
    try:
        temp = float(temp_str)
    except ValueError:
        # Если float() не смог перевести строку в число, он выдаст ошибку.
        # Мы перехватываем её и выдаем свою, понятную.
        raise ValueError(f"Температура не является числом: '{temp_str}'")
        
    return {"city": city, "temperature": temp, "date": date}


def read_valid(lines: list[str]) -> list[dict]:
    """Читает список строк, пропускает пустые и битые, возвращает список словарей."""
    valid_records = []
    for line in lines:
        # Пропускаем пустые строки (или строки из одних пробелов)
        if not line.strip():
            continue
        
        # Пытаемся разобрать строку
        try:
            record = parse_record(line)
            valid_records.append(record)
        except ValueError:
            # Если строка кривая (parse_record выдал ValueError), 
            # мы просто ее пропускаем (ничего не делаем, идем к следующей).
            pass 
            
    return valid_records


def average_by_city(records: list[dict]) -> dict:
    """Считает среднюю температуру по каждому городу."""
    sums = {}
    counts = {}
    
    # Считаем сумму температур и количество записей для каждого города
    for rec in records:
        city = rec["city"]
        temp = rec["temperature"]
        
        sums[city] = sums.get(city, 0) + temp
        counts[city] = counts.get(city, 0) + 1
        
    # Вычисляем среднее и округляем
    averages = {}
    for city in sums:
        averages[city] = round(sums[city] / counts[city], 1)
        
    return averages


def warmest_city(records: list[dict]) -> str:
    """Находит город с самой высокой средней температурой. При равенстве — первый по алфавиту."""
    averages = average_by_city(records)
    
    if not averages:
        return ""
    
    # Сортируем города: сначала по температуре (по убыванию), 
    # затем (если температуры равны) по названию города (по возрастанию - алфавит).
    # В Python это делается с помощью ключа сортировки (key) и кортежа.
    # (-temp, city) означает: сортируем по -temp (то есть от большего к меньшему), 
    # а при равенстве — по city (от А до Я).
    sorted_cities = sorted(averages.keys(), key=lambda c: (-averages[c], c))
    
    return sorted_cities[0]

