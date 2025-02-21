def NVP(M):
    n = len(M)
    Series = [-1]*n
    Series[0] = 1
    def check(index):
        if Series[index] != -1:
            return Series[index]
        max_s = 1
        for i in range(index):
            if M[i] < M[index]:
                max_s = max(max_s, check(i) + 1)
        Series[index] = max_s
        return max_s
    
    max_seria = 1
    for ind in range(1, n):
        # if ind >= max_seria:
        max_seria = max(max_seria, check(ind))
    print(Series)
    return max_seria

M = [1, 1, 1, 3, 4, 1, 5]        
print(NVP(M))
