for i in range(10, 100):

    i1 = i

    pr = 1

    while i1 > 0:

        pr = pr * (i1 % 10)

        i1 = i1 // 10

    if i == pr*2:

        print(i)
