a = int(input())
b = int(input())
c = int(input())
if (a % 2 == 0 and b % 2 != 0) or (a % 2 != 0 and b % 2 == 0):
    print("YES")
else:
    print("NO")
