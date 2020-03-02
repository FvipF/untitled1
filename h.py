s = input()
a = s[:s.find('h')] + s[s.rfind('h') + 1:]
print(a)
