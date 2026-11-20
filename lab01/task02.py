h, v = map(float, input("Введите ширину и высоту прямоугольника:").split())

s = h*v
p = 2 * (h+v)

print(f"Площадь = {s:.1f}")
print(f"Периметр = {p:.1f}")