"""
MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n
        for j <- 1 to n
            sum <- sum + A[i] × A[j]; # 코드1
    return sum;
}


첫째 줄에 코드1 의 수행 횟수를 출력한다.
둘째 줄에 코드1의 수행 횟수를 다항식으로 나타내었을 때, 최고차항의 차수를 출력한다. 단, 다항식으로 나타낼 수 없거나 최고차항의 차수가 3보다 크면 4를 출력한다.

시간복잡도에 관한 문제이고, 2중 for문으로 구성이 되어있다.
즉 2중 for문의 시간복잡도는 n^2이고 따라서 최고차항의 차수는 2이다.
수행횟수는 n까지 2중 for문 이므로 n = 7이면 n^2 = 7^2 = 49이다.

따라서 결과를 출력하는 코드는 아래와 같다.
"""
n = int(input())
print(n**2)
print(2)