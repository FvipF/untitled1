def power(a, n):
    if n == 0:
        return 1
    elif n == 1:
        return a
    elif n % 2 != 0:
        return a * power(a, n - 1)
    elif n % 2 == 0:
        return power(a * a, n / 2)


a = float(input())
n = int(input())
print(power(a, n))
