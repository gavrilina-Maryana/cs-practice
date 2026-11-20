x = int(input('Введите продолжительность в секундах: '))

h = x // 3600 
sec = x % 3600 
m = sec // 60 
s = sec % 60 

if x<0:
    print("введите другое число")
else:    
    print(f'Часы = {h}')
    print(f'Минуты = {m}')
    print(f'Секунды = {s}')