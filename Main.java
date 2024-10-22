import java.util.*;

public class Main
{

    public static int[][] graph = new int[100][100];

	public static void main(String[] args) {
		
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.nextLine();

        for(int i = 0; i < n; i++) {
            Integer[] tempArr = Arrays.stream(sc.nextLine().split(" ")).map(Integer::parseInt).toArray(Integer[]::new);
            for(int j = 0; j < n; j++)
                graph[i][j] = tempArr[j];
        }               
        sc.close();


        for(int k = 0; k < n; k++)
            for(int i = 0; i < n; i++)
                for(int j = 0; j < n; j++)
                    if(graph[i][k] + graph[k][j] == 2)
                        graph[i][j] = 1;

        for(int i = 0; i < n; i++)
            System.out.println(String.join(" ", Arrays.stream(graph[i]).mapToObj(String::valueOf).limit(n).toArray(String[]::new) ));
	}
}