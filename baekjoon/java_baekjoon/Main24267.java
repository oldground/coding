import java.util.Scanner;
public class Main24267 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        long n = sc.nextInt();
        /*
        MenOfPassion(A[], n) {
        sum <- 0;
        for i <- 1 to n - 2
            for j <- i + 1 to n - 1
                for k <- j + 1 to n
                    sum <- sum + A[i] × A[j] × A[k]; # 코드1
        return sum;
        }

        첫째 줄에 코드1 의 수행 횟수를 출력한다.
        둘째 줄에 코드1의 수행 횟수를 다항식으로 나타내었을 때, 최고차항의 차수를 출력한다. 단, 다항식으로 나타낼 수 없거나 최고차항의 차수가 3보다 크면 4를 출력한다.

        if n = 7

        시간복잡도에 대한 위의 3중 for문에 대한 다항식은 (n(n-1)(n-2))/3! 이고, 이에 대한 최고차항의 차수는 3이다.
        수행횟수는 n에 맞는 수를 대입하면 된다.

        즉, 따라서 코드는 아래와 같이 된다.*/
        System.out.println((n*(n-1)*(n-2))/6);
        System.out.println(3);
    }
}
