N, M = map(int, input().split())
baguni = [0] * (N + 1)

for _ in range(M) :
    i, j, k = map(int, input().split())
    for n in range(i, j + 1) :
        baguni[n] = k
    
for i in range(1, N + 1) :
    print(baguni[i], end = " ")