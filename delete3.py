s = input()
for x in range(len(s)):
    if x % 3 != 0:
        print(s[x], end='')
