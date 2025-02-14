import java.util.*;

public class Main {

  static int N, L, R;
  static int[][] graph;
  static int[] dx = {-1, 1, 0, 0};
  static int[] dy = {0, 0, -1, 1};
  
  public static void main(String[] args) {

    Scanner in = new Scanner(System.in);
    N = in.nextInt();
    L = in.nextInt();
    R = in.nextInt();

    graph = new int[N][N];
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < N; j++) {
        graph[i][j] = in.nextInt();
      }
    }
    in.close();

    int result = 0;

    while (true) {
      boolean[][] visited = new boolean[N][N];
      boolean moved = false;

      for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
          if (!visited[i][j]) {
            if (bfs(i, j, visited)) {
              moved = true;
            }
          }
        }
      }

      if (!moved) {
        break;
      }
      result++;
    }

  System.out.println(result);
  }

  static boolean bfs(int i, int j, boolean[][] visited) {
    Queue<int[]> que = new LinkedList<>();
    List<int[]> union = new ArrayList<>();
    que.add(new int[]{i, j});
    visited[i][j] = true;
    int total = graph[i][j];
    union.add(new int[]{i,j});

    while (!que.isEmpty()) {
      int[] current = que.poll();
      int x = current[0];
      int y = current[1];

      for (int k = 0; k < 4; k++) {
        int nx = x + dx[k];
        int ny = y + dy[k];

        if (0 <= nx && nx < N && 0 <= ny && ny < N && !visited[nx][ny]) {
          int diff = Math.abs(graph[x][y] - graph[nx][ny]);

          if (L <= diff && diff <= R) {
            que.add(new int[]{nx, ny});
            visited[nx][ny] = true;
            total += graph[nx][ny];
            union.add(new int[]{nx, ny});
          }
        }
      }
    }

    if (union.size() == 1) {
      return false;
    }

    int newPopulation = total / union.size();
    for (int[] pos : union) {
      graph[pos[0]][pos[1]] = newPopulation;
    }
    return true;
    
  }

}