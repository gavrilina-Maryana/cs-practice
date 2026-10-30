# main.py
import sys
from stats import read_valid, average_by_city, warmest_city

def main():
    input_data = sys.stdin.read()
    
    lines = input_data.splitlines()

    valid_records = read_valid(lines)
    
    total_valid = len(valid_records)
    total_skipped = len(lines) - total_valid
    
    print(total_valid)
    print(total_skipped)
    
    if total_valid > 0:
        best_city = warmest_city(valid_records)
        averages = average_by_city(valid_records)
    
        print(f"{averages[best_city]:.1f}")
    else:
        print(0.0)

if __name__ == "__main__":
    main()