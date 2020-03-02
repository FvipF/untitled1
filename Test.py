a = list(map(int, input().split()))
b = []
for now in a:
    if now % 2 == 0:
        b.append(now)
print(*b)
