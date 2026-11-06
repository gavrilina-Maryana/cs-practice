def parse_event(line):
    line = line.strip()

    parts = line.split(' ')

    if len(parts) >= 3:
        time, level, *message = parts

        valid_levels = {'DEBUG', 'INFO', 'WARNING', 'ERROR'}
        if level not in valid_levels:
            raise ValueError('')

        message = ' '.join(message).strip()
        return {'time': time, 'level': level, 'message': message}
    else:
        raise ValueError('')


def count_levels(lines):
    count = {}
    for line in lines:
        if not line.strip():
            continue
            
        parts = line.split(maxsplit=2)
        valid_levels = {'DEBUG', 'INFO', 'WARNING', 'ERROR'}
        
        if len(parts) >= 3 and parts[1] in valid_levels:
            event = parse_event(line)
            level = event['level']
            count[level] = count.get(level, 0) + 1
        else:
            count['BROKEN'] = count.get('BROKEN', 0) + 1
            
    return count


def top_errors(lines, n):
    errors = {}
    for line in lines:
        if not line.strip():
            continue
        parts = line.split(maxsplit=2)
        if len(parts) >= 3 and parts[1] == 'ERROR':
            msg = parts[2].strip()
            errors[msg] = errors.get(msg, 0) + 1
            
    sorted_errors = sorted(errors.items(), key=lambda x: (-x[1], x[0]))
    return [[msg, cnt] for msg, cnt in sorted_errors[:n]]


def format_report(counts, errors):
    lines = ["Отчёт по журналу", ""]

    for level in sorted(counts.keys()):
        lines.append(f"{level}: {counts[level]}")

    lines.append("")
    lines.append("Частые ошибки:")

    for msg, cnt in errors:
        lines.append(f"- {msg} — {cnt}")

    return "\n".join(lines) + "\n"