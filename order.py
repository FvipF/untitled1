a = int(input())
b = int(input())
c = int(input())
if a > b:
    a, b = b, a
elif b > c:
    b, c = c, b
print(a, b, c)
