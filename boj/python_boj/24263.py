"""
MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n
        sum <- sum + A[i]; # 코드1
    return sum;
}

첫째 줄에 코드1 의 수행 횟수를 출력한다.
둘째 줄에 코드1의 수행 횟수를 다항식으로 나타내었을 때, 최고차항의 차수를 출력한다. 단, 다항식으로 나타낼 수 없거나 최고차항의 차수가 3보다 크면 4를 출력한다.

함수를 보면 for문의 시간복잡도는 입력이 뭐든간에 for문이 한번만 있으면 입력이 뭐든 간에 O(n) = n 이므로
최고차항은 1이다.

즉 7을 넣으면 7번을 돌고 최고차항의 차수는 1이다.
따라서 입력이 n이면 수행 횟수는 for 문에 의하여 n이고 수행횟수를 다항식으로 나타내었을 때의 최고차항의 차수는
O(n) = n이므로 시간복잡도의 최고차항의 차수는 1이다.

즉 코드는 아래와 같이 된다.
"""
n = input()
print(n)
print(1)