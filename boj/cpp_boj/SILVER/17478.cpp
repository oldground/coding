// 17478. 재귀함수가 뭔가요? -> 실버 5

#include <bits/stdc++.h>

using namespace std;

int n;
string s1 = "어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.";
string s2 = "\"재귀함수가 뭔가요?\"";
string s3_1 = "\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.";
string s3_2 = "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.";
string s3_3 = "그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"";
string s4 = "\"재귀함수는 자기 자신을 호출하는 함수라네\"";
string s5 = "라고 답변하였지.";
string s6 = "____";

void chatbot(int depth) {
  for (int i = 0; i < depth; i++) cout << s6;
  cout << s2 << '\n';
  if (depth==n) {
    for (int i = 0; i < depth; i++) cout << s6;
    cout << s4 << '\n';  
  }
  else {
    for (int i = 0; i < depth; i++) cout << s6;
    cout << s3_1 << '\n';
    for (int i = 0; i < depth; i++) cout << s6;
    cout << s3_2 << '\n';
    for (int i = 0; i < depth; i++) cout << s6;
    cout << s3_3 << '\n';
    chatbot(depth+1);
  }
  for (int i = 0; i < depth; i++) cout << s6;
  cout << s5 << '\n';
}

void func1(void) {
  cin >> n;
  cout << s1 << '\n';
  chatbot(0);
}

int main(void)
{
  ios::sync_with_stdio(0);
  cin.tie(0);
  func1();
  return 0;
}