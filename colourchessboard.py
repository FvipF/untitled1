horizontal1 = int(input())
vertically1 = int(input())
horizontal2 = int(input())
vertically2 = int(input())
if (horizontal1 + horizontal2 + vertically1 + vertically2) % 2 == 0:
    print("YES")
else:
    print("NO")
