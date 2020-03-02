start = 1
end = -1


def IsPointInSquare(x, y):
    return (x <= start and x >= end) and (y >= end and y <= start)


x = float(input())
y = float(input())
if IsPointInSquare(x, y):
    print('YES')
else:
    print('NO')
