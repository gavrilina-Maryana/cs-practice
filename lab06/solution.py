paths = ["docs/report.PDF", "notes.txt", "docs/img/logo.png", "Makefile"]
# {"pdf": 1, "txt": 1, "png": 1, "": 1}
# deepest_path(paths)         # "docs/img/logo.png"

# human_size(900)             # "900 Б"
# human_size(1536)            # "1.5 КБ"
# human_size(5 * 1024 * 1024) # "5.0 МБ"
def count_by_extension(paths):
    extensions = {}
    for path in paths:
        if '.' in path:
            extension = path.split('.')[-1].lower()
        else:
            extension = ''
        extensions[extension]= extensions.get(extension, 0) + 1
       
    return extensions
print(count_by_extension(paths)) 

def deepest_path(paths):
    if not paths:
        return ""
    max_depth = -1
    best_path = ""

    for path in sorted(paths):
        depth = path.count('/')
        if depth > max_depth:
            max_depth = depth
            best_path = path

    return best_path

def human_size(n_bytes):
    if n_bytes < 1024:
        return f"{n_bytes} Б"
    elif n_bytes < 1024 * 1024:
        return f"{n_bytes / 1024:.1f} КБ"
    elif n_bytes < 1024 * 1024 * 1024:
        return f"{n_bytes / (1024 * 1024):.1f} МБ"
    elif n_bytes < 1024 * 1024 * 1024 * 1024:
        return f"{n_bytes / (1024 * 1024 * 1024):.1f} ГБ"
    else:
        return f"{n_bytes / (1024 * 1024 * 1024 * 1024):.1f} ТБ"

if __name__ == '__main__':
    test_paths = ["docs/report.PDF", "notes.txt", "docs/img/logo.png", "Makefile"]
    
    print("1. Расширения:", count_by_extension(test_paths))
    print("2. Самый глубокий путь:", deepest_path(test_paths))
    print("3. Размер 900:", human_size(900))
    print("4. Размер 1536:", human_size(1536))
    print("5. Размер 5 МБ:", human_size(5 * 1024 * 1024))