N, M = map(int, input().split())
baguni = []
for i in range(N + 1) :
    baguni.append(i)
for _ in range(M) :
    i, j = map(int, input().split())
    baguni[i], baguni[j] = baguni[j], baguni[i]
for i in range(1, N + 1) :
    print(baguni[i], end = " ")