import java.util.*;

public class Main {

    public static int n;
    public static int cnt;
    /*
        퀸의 상하 겹침을 체크하기 위한 자료구조이다.
        현재 행을 인덱스로 삼고 현재 열 데이터를 값으로 넣어주면, 1차원 자료구조로 2차원 좌표 표현이 가능해진다.
        초기값은 중요하지 않음. 매 행마다 갱신할 것이며, 현재 행 전까지의 퀸에 대해서만 비교할 것이니까.
        그리고 행에 대한 충돌 처리도 할 필요가 없음. 매 행마다 하나의 퀸만 놓을 거니까.
     */ 
    public static int[] queenExistCoordinate = new int[15];

    public static void main(String[] args) throws Exception {

        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        sc.close();

        // 체스판의 왼쪽 상단 (0,0)부터 시작.
        backTracking(0);
        System.out.println(cnt);
    }

    // 백트래킹을 포함한 DFS
    public static void backTracking(int row) {

        // 모든 행을 스캔한 경우, 해당 케이스는 성공적인 케이스이므로 카운트.
        if(row == n) {
            cnt++;
            return;
        }

        for(int col = 0; col < n; col++) {

            // 위쪽 행에 위치한 퀸들과 충돌나지 않으면 재귀 탐색 진행.
            queenExistCoordinate[row] = col;
            if(checkQueens(row)) 
                backTracking(row+1);
        }
    }

    public static boolean checkQueens(int currentRow) {

        for(int row = 0; row < currentRow; row++) {

            // 퀸이 상하로 충돌하면 back.
            if(queenExistCoordinate[row] == queenExistCoordinate[currentRow])
                return false;

            // 퀸이 대각으로 충돌하면 back.
            if(Math.abs(currentRow - row) == Math.abs(queenExistCoordinate[currentRow] - queenExistCoordinate[row]))
                return false;
        }

        return true;
    }
}