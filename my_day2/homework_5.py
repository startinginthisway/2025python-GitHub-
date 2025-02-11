# 2024年12月25日
i = 1
while (i <= 9):
    j = 1
    while (j <= i):
        print("%d x %d = %2d   " % (i, j, j * i),end = " ")
        j += 1
    print("\t")
    i += 1
