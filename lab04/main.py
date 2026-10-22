# main.py
import sys
from stats import read_valid, average_by_city, warmest_city

def main():
    # Читаем весь ввод из консоли до конца (Ctrl+D в Linux/Mac или Ctrl+Z в Windows)
    input_data = sys.stdin.read()
    
    # Разбиваем текст на строки
    lines = input_data.splitlines()
    
    # 1. Получаем список правильных записей (словарей)
    valid_records = read_valid(lines)
    
    # 2. Считаем статистику
    total_valid = len(valid_records)
    total_skipped = len(lines) - total_valid
    
    # 3. Выводим 1-ю и 2-ю строки отчета (количество разобранных и пропущенных)
    print(total_valid)
    print(total_skipped)
    
    # 4. Ищем самый теплый город
    if total_valid > 0:
        best_city = warmest_city(valid_records)
        averages = average_by_city(valid_records)
        
        # Выводим 3-ю строку отчета (средняя температура лучшего города)
        # Формат "{:.1f}".format(...) гарантирует ОДИН знак после запятой (например, 30.0)
        print(f"{averages[best_city]:.1f}")
    else:
        # Если валидных записей не было вообще, выводим заглушку или 0.0
        print(0.0)

if __name__ == "__main__":
    main()