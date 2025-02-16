"""
MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n - 1
        for j <- i + 1 to n
            sum <- sum + A[i] × A[j]; # 코드1
    return sum;
}

첫째 줄에 코드1 의 수행 횟수를 출력한다.
둘째 줄에 코드1의 수행 횟수를 다항식으로 나타내었을 때, 최고차항의 차수를 출력한다. 단, 다항식으로 나타낼 수 없거나 최고차항의 차수가 3보다 크면 4를 출력한다.

2중 for문이라 시간복잡도 상 수행 횟수를 다항식으로 나타냈을 때 최고차항의 차수는 2이다.
수행 횟수를 다항식으로 출력하려면
if n = 7, 1~6까지 
2~7, 3~7, 4~7, 5~7, 6~7, 7 이므로
6 5 4 3 2 1 수행횟수 따라서 21회 수행
즉 다항식으로 비교를 해보면 n(n-1)/2가 된다

이 다항식의 최고차수를 n^2으로 2가 되고 대략적으로 n^2인 식이 된다.
"""
n = int(input())
print(int(n*(n-1)/2))
print(2)