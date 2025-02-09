import java.util.Arrays;

class Solution {
    public int[] solution(int[] num_list) {
        Arrays.sort(num_list);
        
        int[] newList = Arrays.copyOfRange(num_list, 0 ,5);
        
        return newList;
    }
}