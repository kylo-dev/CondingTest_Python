class Solution {
    public int solution(int a, int b) {
        int first = Integer.parseInt(String.valueOf(a) + String.valueOf(b));
        int second = Integer.parseInt(String.valueOf(b) + String.valueOf(a));
        
        if (first > second) {
            return first;
        } else {
            return second;
        }
    }
}