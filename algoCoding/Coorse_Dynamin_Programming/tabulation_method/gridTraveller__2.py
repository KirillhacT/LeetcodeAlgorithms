def GridTraveller(m, n):
    table = [[0]*(n+1) for i in range(m+1)]
    table[1][1] = 1
    # print(table)
    for i in range(m + 1):
        for j in range(n + 1):
            current = table[i][j]
            if j + 1 <= n:
                table[i][j + 1] += current
            if i + 1 <= m:
                table[i + 1][j] += current
    for i in table:
        print(i, end="\n")
    return table[m][n]

    # table = [[0] * n for _ in range(m)]
    # for i in range(m):
    #     for j in range(n):
    #         if i == 0 or j == 0:
    #             table[i][j] = 1
    #             continue
    #         table[i][j] = table[i-1][j] + table[i][j-1]
    # return table[m-1][n-1]




print(GridTraveller(3, 3))