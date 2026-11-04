def parse_event(line):
    line = line.split(' ')

    if len(line) >= 3:
        time, level, *message = line
        message = ' '.join(message).strip()
        return {'time':time, 'level': level, 'message': message}
    else:
        raise ValueError('')


def count_levels(lines):
    count = {}
    valid_levels = {'DEBUG', 'INFO', 'WARNING', 'ERROR'}

    for line in lines:
        parts = line.split(maxsplit=2)

        if len(parts) >= 3 and parts[1] in valid_levels:
            event = parse_event(line)
            level = event['level']

            count[levels] = count.get(level, 0) + 1
        else:
            count['BROKEN'] = count.get('BROKEN', 0) + 1

    return count

def top_errors(lines, n):
    errors = {}
    for line in lines:
        parts = line.split(maxsplit=2)

        if len(parts) >= 3 and parts[1] == 'ERROR':
            msg = parts[2].strip()
            errors[msg] = errors.get(msg, 0) + 1

        sorted_errors = sorted(errors.items(), key=lambda item: (-item[1], item[0]))

        return [[msg, count] for msg, count in sorted_errors[:n]]

    