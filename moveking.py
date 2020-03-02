horizontal1 = int(input())
vertically1 = int(input())
horizontal2 = int(input())
vertically2 = int(input())
if horizontal2 == horizontal1 + 1 or horizontal2 == horizontal1 - 1 or horizontal2 == horizontal1:
    f = True
else:
    f = False
if vertically2 == vertically1 + 1 or vertically2 == vertically1 - 1 or vertically2 == vertically1:
    f = True
else:
    f = False
if f:
    print("YES")
else:
    print("NO")
