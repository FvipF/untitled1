import math

x = float(input())
b = (x - int(x))*10
if b < 5:
    print(math.floor(x))
else:
    print(math.ceil(x))
