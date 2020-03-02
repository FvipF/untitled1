def lagr(n):
    t = []
    for a in range(n, -1, -1):
        for b in range(n, -1, -1):
            for c in range(n, -1, -1):
                for d in range(n, -1, -1):
                    if a ** 2 + b ** 2 + c ** 2 + d ** 2 == n:
                        t = t + [a, b, c, d]
                        s = [x for x in t if x != 0]
                        return s


n = int(input())
print(*lagr(n), end='')
