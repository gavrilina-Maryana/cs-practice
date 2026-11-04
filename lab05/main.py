from logstats import parse_event, count_levels, top_errors, format_report

filename = 'events.log'

with open(filename, 'r', encoding='utf-8') as file:
    counts = count_levels(file)


total_parsed = sum(counts.values())
print(total_parsed)
print(counts.get('ERROR', 0))
print(counts.get('BROKEN', 0))

with open(filename, 'r', encoding='utf-8') as file:
    errors = top_errors(file, 3) 

report_text = format_report(counts, errors)

with open('report.txt', 'w', encoding='utf-8') as report_file:
    report_file.write(report_text)