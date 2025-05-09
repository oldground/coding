# BOJ Gold

## 14502. 연구소 -> 골드 4

### BFS, 브루트포스 사용

이야.. 확실히 실버보단 골드가 어렵긴 하다. 한가지 알고리즘만을 생각하여 적용하는 것이 아닌 복합적으로 적용을 하게 됨.

문제를 해결하기 위해 생각한 것은, 벽을 3개를 세우고, 그 다음 바이러스를 점염시키고 안전지대를 카운트하는 것임.

그래서 함수를 3개를 만들어서 실행, 벽을 세우는 wall(), 바이러스를 점염시키는 bfs(), 안전지대를 카운트하는 find_max()

#### wall()

해당 함수는 벽을 3개를 세우는 경우의 수를 모두 찾는 함수임. 벽을 세울 수 있는 조건은 빈칸(0)이어야 했음.

그래서 모든 위치를 순회하며 빈칸이면 wall의 개수를 count하는 cnt변수를 증가시키고 해당 위치를 벽(1)로 바꿔줌.

그 후 재귀를 통해 wall()을 호출

원상 복구를 위해 cnt변수를 감소시키고, 다시 빈칸(0)으로 만들어줌.

이러한 방식으로 재귀를 통해 벽을 세우게 되면 cnt가 3이 될 때가 있는데, 이 때 벽을 3개 모두 세운 상태이므로 bfs()를 return하여 바이러스를 점염시키도록 함.

#### bfs()

먼저 기존의 지도는 벽을 세울 떄 사용하기 때문에, 사용을 안하고, 벽을 세워진 상태의 지도를 cpy_map으로 복사를 하여 사용.

점염을 시키는 방식은 복사한 지도를 순회하며 바이러스(2)를 찾음. 이때 바이러스이고, 방문하지 않았을 경우에만 점염을 시작.

그 이후는 bfs의 방식을 따라 지도의 범위 내이고, 빈칸(0)인 곳을 바이러스(2)로 변경하면서 진행.

바이러스 점염이 완료된 이후에는 find_max()를 호출

#### find_max()

해당 함수를 통해 복사된 지도의 빈칸(0)을 count를 하고, 최대값과 비교를 하여 업데이트를 진행

#### 결론

문제를 파악하고, 해결하기 위해 방식을 정리를 해둠으로써 코드를 작성하기 편리했던 것 같음.

방식을 세우고, 코드를 잘 작성하지 못하여 다른 사람의 문제 풀이를 참고한 점이 아쉬움.

그렇지만 골드의 문제 파악능력 향상에는 도움이 됨

**소요시간 : 2시간**
---
## 15686. 치킨 배달 -> 골드 5

### DFS 사용

처음에는 14502번의 영감을 받아 BFS로 구현을 하였음. 하지만 해당 방식으로 구현 시 시간초과가 나는 부분이 발생함.

14502번에 비해 범위가 크기 때문일 것이라고 생각.

그래서 다른 방식으로 접근, 치킨집과 집의 좌표만 필요하기 때문에, 입력받을 때 치킨집벡터에 치킨집 좌표를 추가하고, 집벡터에 집 좌표를 추가를 함.

그리고 치킨집벡터를 이용해서 최대 개수 만큼의 index를 생존벡터에 index값을 추가하는 식으로 진행.

그 후 최대 개수만큼 되면 최소거리 계산하기 진행

풀고나서 풀이를 하니 되게 간단하게 보임. 특히 접근을 초반에 익숙한 BFS로 접근을 해버려서 시간 초과가 나고, DFS로 변경을 하니 풀이를 할 수 있었음

**소요시간 : 1시간 30분** => 접근을 잘못하여 코드를 한번 뒤엎음
---
## 14891. 톱니바퀴 -> 골드 5

### deque을 사용한 구현

딱 보자마자 앞과 끝의 삽입과 제거가 자유로운 방식을 써야한다고 생각

그 때 떠오른 것이 **deque** 근데 이 deque를 vector로 담을 수 있나 찾아봤더니 됨

그래서 vector로 5개의 크기를 선언하고 deque를 만들었음

그 deque에 각 기어의 극을 입력하고 기어마다 회전방향을 정해줘야 함. 

회전방향은 하나가 돌면 연속적으로 모든 톱니가 돌 수도 있는 가능성도 있고, 하나만 돌 수도 있는 것이기 때문에 회전방향을 정하는 함수를 만들어서 방향을 정해줌

회전 방향을 정하는 조건은 기어의 번호인 1 ~ 4일 경우와 회전 방향을 정했는 지 여부이다. 이는 check배열로 판단을 할 수 있음.

회전 방향을 판단하는 방식은 재귀를 이용햇고, 왼쪽과 오른쪽을 나눠서 구현함

왼쪽의 경우는 현재의 톱니가 회전을 안하면 왼쪽 톱니도 회전을 안하고, 현재 톱니가 회전을 하는데 같은 극이면 회전을 안하고, 현재 톱니가 회전을 하고 극이 다르면 왼쪽 톱니는 현재 톱니의 반대 방향으로 회전한다.

오른쪽의 경우는 현재의 톱이가 회전을 안하면 오른쪽 톱니도 회전을 안하고, 현재 톱니가 회전을 하는데 같은 극이면 회전을 안하고, 현재 톱니가 회전을 하고 극이 다르면 오른쪽 톱니느 현재 톱니의 반대 방향으로 회전한다.

이 때 같은 극을 판단하는 법은 현재 톱니의 6번 인덱스와 왼쪽 톱니의 2번 인덱스가 맞닿아 있고, 현재 톱니의 2번 인덱스와 오른쪽 톱니의 6번 인덱스가 맞닿아 있다.

이 2가지를 접근하여 극성 판단을 하면 된다.

회전 방향을 판단한 후에는 deque의 성질을 이용해서 시계방향으로 회전하면 제일 뒤가 제일 앞으로 오도록 제일 뒤의 값을 제일 앞에 삽입하고, 제일 뒷 값은 pop을 해주면 된다.

반대로 반시계방향으로 회전하면 제일 앞 값이 제일 뒤로 가도록 제일 앞의 값을 제일 뒤에 삽입하고, 제일 앞 값은 pop을 해주면 된다.

결과값은 각 톱니의 12시의 극성을 보고 점수를 판단을 하는 것인데, 1번 N 0 , S 1=2^0 / 2번 N 0 , S 2=2^1 / 3번 N 0 , S 4=2^2 / 4번 N 0 , S 8=2^3 와 같은 점수표를 가지게 된다.

이를 이용하여 각 인덱스를 접근하며 i = 1부터 i = 4까지 접근을 하기에 gear[i].front() * pow(2, i - 1)과 같은 형태의 계산 값의 합을 구해주면 된다.

deque를 사용한다는 것을 바로 판단을 하면 생각보다 구현하기에는 어렵지 않은 문제였음.

**소요시간 : 40분** => deque를 사용함을 알고, 규칙을 찾으면 쉽게 구현 가능
---