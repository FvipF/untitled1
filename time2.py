n = int(input())
a = (n // 3600) % 24
b = n // 60 % 60 // 10
c = n // 60 % 60 % 10
d = n % 60 // 10
e = n % 10
print(a, ":", b, c, ":", d, e,)
