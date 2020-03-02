def IsAscending(A):
    for i in range(1, len(A)):
        while int(A[i]) < int(A[i + 1]):
            return ("YES")
        return ("NO")


spisok = input().split()
print(IsAscending(spisok))
