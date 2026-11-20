x = int(input( "Введите четырехзначное число: "))

x1 = x // 1000
b12 = x // 100
x2 = b12 % 10
b34 = x % 100
x3 = b34 // 10
x4 = x % 10

if x%10==0:
    print("попробуйте другое число")
elif 1000<=x<=9999:
    print(x1)
    print(x2)
    print(x3)
    print(x4)
    print(x1+x2+x3+x4)
    print(x4*1000+x3*100+x2*10+x1)
elif x<=999 or x>=10000:
    print("попробуйте другое число")




