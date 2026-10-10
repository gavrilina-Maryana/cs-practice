x, op, y = input("Введите два числа и операцию между ними: ").split()
x = int(x)
y = int(y)

if op == "+":
    print(x + y)
elif op == "-":
    print(x - y)
elif op == "*":
    print(x * y)
elif op == "/":
    if y != 0:
        print(x / y)
    else:
        print("Ошибка: деление на ноль")