[문제 링크](https://www.acmicpc.net/problem/9663)

# 문제 정보
N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

### 입력

- 첫째 줄에 N이 주어진다. (1 ≤ N < 15)

### 출력

- 첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.

### 예제 입력

```
8
```

### 예제 출력

```
92
```

# 풀이

> 백트래킹: 해를 찾는 도중 해가 아니어서 막히면, 되돌아가서 다시 해를 찾아가는 기법

N-Queen 문제는 백트래킹의 가장 대표적인 문제이다. 기본적으로는 완전탐색을 기반으로 돌아간다. 문제 조건에서도 n이 15 미만이기 때문에 볼륨이 크지 않다는 것을 알 수 있다. 

완전탐색을 할 때는 성능을 높이기 위해 반복문을 돌리는 것이 일반적이지만, 백트래킹을 사용하려면 이전 상태로 돌아갈 수 있어야 하므로 반드시 재귀 방법으로 해결해야 한다. 각 row마다 퀸 하나를 놓아가면서 해당 좌표에 퀸을 놓으면 다른 위쪽 row에 대한 퀸들과 영역이 겹치는지 매번 비교해나간다. 만약 위쪽의 다른 퀸과 영역이 겹친다면, 이전 상태로 되돌아온다. 그렇게 최종적으로 가장 마지막 row까지 퀸을 놓는데 성공하면, 그것은 모든 퀸이 서로를 공격하지 않는 하나의 경우이다. 이 행동을 모든 경우에 대해 반복하면 최종적으로 조건을 만족하는 모든 경우의 수를 계산할 수 있다.

하지만 백트래킹과는 별개로 퀸의 영역 비교에 대한 구현까지 해줘야 한다. 기본적으로 row에 대해 순차 탐색을 진행하기 때문에, 우리는 동일한 row에 대해 중복 여부를 비교할 필요는 없다. 각 row 당 퀸 하나씩만 놓을 거니까. 다만 column의 경우에는 매 row마다 순차탐색을 하면서 이미 점유된 column인지 비교해야 한다. 그렇기에 column의 점유 상태를 관리하는 리스트(혹은 배열) 하나를 사용해준다. 각 인덱스는 column의 좌표를 의미하며, 각 인덱스마다 true 혹은 false의 값을 저장시킨다. 디폴트는 false로 한다. 만약 퀸이 자리를 점유하고 있다면, 해당 column에 해당하는 인덱스의 값을 true로 변경한다. 

하지만 대각선이 진짜 문제다. row를 순차탐색하기에 아래 row를 고려하지 않고 위에 세 방향으로 가지치기 해나가며 재귀탐색을 하면 되지 않을까 생각할 수 있고, 실제 구현도 가능은 하다. 그러나 좌표계의 특징을 이용하면 이 방식보다 효율적으로 구현이 가능하다. 퀸은 대각으로는 y=x축과 y=-x축으로 이동할 수 있다. y=x축의 경우에는 좌표계의 시작이 좌측 상단에서 시작한다는 특징에 의해, y=x축을 따라 column이 1 증가할 때마다 row가 1 감소한다. 그래서 y=x 축에서 row와 column의 합은 항상 일정하다. 이 y=x축이 보드판 위에서 여러 개 존재하는데(n이 2 이상이면), 각 축마다 그 합은 일정하다는 특징을 활용하면 각 축마다의 자리 점유를 표현할 수 있다. 그러므로 각 y=x 축마다의 합을 인덱스로 표현하는 리스트(혹은 배열)를 사용해주면, 각 퀸의 y=x 방향으로의 자리 점유를 표현할 수 있다. y=-x도 큰 개념은 동일하다. 다만 row와 column의 관계가 살짝 다른 점만 짚으면 된다. y=-x축 위에서는 column이 1 증가하면 row도 1 증가한다. 그래서 각 y=-x 축마다 row와 column의 차는 항상 일정하다. 이 특성을 활용하여 각 y=-x축 방향의 자리 점유 또한 표현할 수 있다. 다만 y=-x 같은 경우에는 두 값의 차가 음수가 될 수 있다는 점을 고려하여 인덱스 매핑을 해줘야 한다.

위처럼 퀸이 자리를 점유하는 방향을 모두 구현하면, 이제 매 좌표마다 자리 점유 리스트 3개를 매번 뒤져서 전부 false일 때 해당 좌표에 퀸을 놓고 다음 row로 재귀 탐색을 하면 된다.

참고로 [이 블로그](https://blog.encrypted.gg/945)에서 백트래킹에 대한 개념과 예제 문제를 충실히 다루고 있기에, 백트래킹에 대한 추가 훈련을 진행하고 싶다면 이 블로그를 참고하라.

```python
def sol(row):
    global cnt

    # 행 끝까지 재귀에 성공한 경우, 해당 탐색은 성공적인 경우이므로 카운트하고 재귀 종료
    if row == n:
        cnt += 1
        return
    
    for col in range(n):
        # 만약 현재 좌표에 퀸을 배치했을 때 십자 영역과 대각선 영역 모두 포함해서 다른 퀸과 걸치지 않는 경우
        if not usedCross[col] and not usedLinearIncreaseDirection[row + col] and not usedLinearDecreaseDirection[(n-1) + row - col]:
            # 새로운 퀸을 배치하고자, 이 퀸에 대한 십자와 대각선 영역 표시
            usedCross[col] = True
            usedLinearIncreaseDirection[row + col] = True
            usedLinearDecreaseDirection[(n-1) + row - col] = True
            # 재귀 탐색 진행
            sol(row+1)
            # 재귀 끝난 경우 현재 좌표에 둔 퀸을 빼면서 다음 col에서의 퀸 재귀 탐색 준비
            usedCross[col] = False
            usedLinearIncreaseDirection[row+col] = False
            usedLinearDecreaseDirection[(n-1) + row - col] = False
        else:
            # 다른 퀸과 겹치면 이전으로 돌아가기
            return


n = int(input())
board = [[0] * n for _ in range(n) ]
# 같은 row와 같은 col에 퀸이 존재하면 안된다.
usedCross = [False] * n  # row 기준으로 각 row마다 하나의 퀸을 놓으면서 순차 반복을 돌리면 column 점유 여부만 고려하면 된다. 따라서 2차원 좌표 문제를 선형 리스트로도 문제 풀 수 있음.
# 보드판에서 y=x 방향으로 이동하면 (row - i, col + i) 좌표 형식으로 움직인다. i값 범위는 0부터 row가 0이 될 때까지.
usedLinearIncreaseDirection = [False] * (2*(n-1) + 1)  # n*n 보드 기준 y=x 방향 'row + col'의 범위는 0 ~ 2(n-1).
# 보드판에서 y=-x 방향으로 이동하면 (row + i, col + i) 좌표 형식으로 움직인다. i값 범위는 0 ~ n-1.
usedLinearDecreaseDirection = [False] * (2*(n-1) + 1)  # n*n 보드 기준 y=-x 방향 'row - col'의 범위는 -(n-1) ~ (n-1).

cnt = 0
sol(0)
print(cnt)
```
참고로 Python말고 **PyPy를 사용했을 경우 메모리 소비량이 크게 증가하지만 연산 속도는 크게 감소하는 trade-off 효과를 볼 수 있다.** 만약 메모리는 넘쳐나는데 시간이 부족한 경우 PyPy로 채점해보자.


```java
import java.util.*;

public class MainClass {
	
	// 기본 자료형 boolean은 전부 false로 초기화 되어 있다.
	// Boolean Wrapper class를 쓰는 경우 Arrays.fil(배열명, false) 함수를 사용하여 false를 채워넣어주자.
	public static boolean[] usedCross = new boolean[15];
	public static boolean[] usedLinearIncreaseDirection = new boolean[2*(15-1) + 1];
	public static boolean[] usedLinearDecreaseDirection = new boolean[2*(15-1) + 1];
	public static int cnt = 0;
	public static int n = 0;
	
	public static void main(String[] args) throws Exception {
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		sc.close();

		backTracking(0);
		System.out.println(cnt);
	}
	
	public static void backTracking(int row) {
		
		if (row == n) {
			cnt++;
			return;
		}
		
		for (int col=0; col < n; col++) {
			if(usedCross[col] == false && usedLinearIncreaseDirection[row + col] == false && usedLinearDecreaseDirection[(n-1) + row - col] == false) {
				usedCross[col] = true;
				usedLinearIncreaseDirection[row + col] = true;
				usedLinearDecreaseDirection[(n-1) + row - col] = true;
				backTracking(row + 1);
				usedCross[col] = false;
				usedLinearIncreaseDirection[row + col] = false;
				usedLinearDecreaseDirection[(n-1) + row - col] = false;
			} else {
                return;
            }
		}
	}
}
```