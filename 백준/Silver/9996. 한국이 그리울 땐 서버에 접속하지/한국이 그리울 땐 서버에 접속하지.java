import java.util.*;

public class Main {

  static int N;
  static String pattern;
  static int starIdx;
  
  public static void main(String[] args) {

    Scanner in = new Scanner(System.in);

    N = Integer.parseInt(in.nextLine());
    
    pattern = in.nextLine();
    starIdx = pattern.indexOf("*");

    String start = pattern.substring(0, starIdx);
    String end = pattern.substring(starIdx + 1);

    for (int i = 0; i < N; i++) {
      String file = in.nextLine();

      if (file.length() >= pattern.length() - 1 &&
        file.startsWith(start) && file.endsWith(end)) {
        System.out.println("DA");
        }
      else {
        System.out.println("NE");
      }
    }
    in.close();
    
  }
}