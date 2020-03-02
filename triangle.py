a = int(input())
b = int(input())
c = int(input())
x = ((a ** 2) - (b ** 2) - (c ** 2))/(- 2 * b * c)
y = ((b ** 2) - (a ** 2) - (c ** 2))/(- 2 * a * c)
z = ((c ** 2) - (a ** 2) - (b ** 2))/(- 2 * b * a)
if x or y or z == 0:
    print("rectangular")
elif x and y and z > 0:
    print("acute")
elif x or y or z < 0:
    print("obtuse")
elif (a + b) <= c:
    print("impossible")
elif (a + c) <= b:
    print("impossible")
elif (c + b) <= a:
    print("impossible")
