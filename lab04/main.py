import sys
from stats import parse_record, read_valid, average_by_city, warmest_city

def main():
    lines = sys.stdin.read().splitlines()
    
    valid_records = read_valid(lines)

    non_empty_lines = [line for line in lines if line.strip() != ""]
    errors_count = len(non_empty_lines) - len(valid_records)

    print(len(valid_records))

    print(errors_count)

    if valid_records:
        best = warmest_city(valid_records)
        averages = average_by_city(valid_records)
        print(f"{averages[best]:.1f}")
    else:
        print("0.0")

if __name__ == "__main__":
    main()