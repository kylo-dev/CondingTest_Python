import java.util.*;
import java.util.stream.Collector;

public class Main {

  static int N, M;
  static List<Integer> arr = new ArrayList<>();
  static List<Integer> ans = new ArrayList<>();
  
  public static void main(String[] args) {

    Scanner in = new Scanner(System.in);
    N = in.nextInt();
    M = in.nextInt();

    for (int i = 0; i < N; i++) {
      arr.add(in.nextInt());
    }
    Collections.sort(arr);

    back(0);

  }

  static void back(int start) {
    if (ans.size() == M) {
      for (int a: ans) {
        System.out.print(a + " ");
      }
      System.out.println();
      return;
    }

    for (int i = 0; i < N; i++) {
      if (ans.contains(arr.get(i))) {
        continue;
      }

      ans.add(arr.get(i));
      back(start + 1);
      ans.remove(ans.size() - 1);
    }
  }

}