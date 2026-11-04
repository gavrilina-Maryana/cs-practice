from logstats import parse_event, count_levels, top_errors

with open('events.log' , 'r' , encoding='utf-8') as file:
    for line in file:
        print(parse_event(line))

counts = count_levels(lines)

total_parsed = sum(counts.values())
print(total_parsed)

print()