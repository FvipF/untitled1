def asort(a):
    n = len(a)
    for i in range(n-1):
        for jj in range(n-i):
            j = jj+i
            if a[j] > a[i]:
                tmp = a[i]
                a[i] = a[j]
                a[j] = tmp


n = int(input())
arr = []
for i in range(n):
    arr += [int(input())]
asort(arr)
for i in arr:
    print(i)
