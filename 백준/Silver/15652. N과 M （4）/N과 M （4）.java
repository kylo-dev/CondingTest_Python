import java.util.*;

public class Main {

  static int N, M;
  static List<Integer> ans = new ArrayList<>();
  
  public static void main(String[] args) {

    Scanner in = new Scanner(System.in);
    N = in.nextInt();
    M = in.nextInt();
    in.close();
    
    back();
  }

  static void back() {

    if (ans.size() == M) {
      for (int num : ans) {
        System.out.print(num + " ");
      }
      System.out.println();
      return;
    }

    for (int i = 1; i <= N; i++) {
      if (ans.isEmpty() || i >= ans.get(ans.size() - 1)) {
        ans.add(i);
        back();
        ans.remove(ans.size() - 1);
      }
    }
  }

}