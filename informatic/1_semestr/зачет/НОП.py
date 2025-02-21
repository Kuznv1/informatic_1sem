def lcs(X, Y):
    m = len(X)
    n = len(Y)
    memo = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]
   
    def lcs_rec(i, j):
        if i == 0 or j == 0:
            return 0
        if memo[i][j] != -1:
            return memo[i][j]
        if X[i - 1] == Y[j - 1]:
            memo[i][j] = 1 + lcs_rec(i - 1, j - 1)
        else:
            memo[i][j] = max(lcs_rec(i - 1, j), lcs_rec(i, j - 1))
        return memo[i][j]

    return lcs_rec(m, n)

X = "aabc"
Y = "GXbXAcB"
print(lcs(X, Y))