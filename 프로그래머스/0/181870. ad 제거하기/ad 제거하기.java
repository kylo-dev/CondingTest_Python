import java.util.*;

class Solution {
    public String[] solution(String[] strArr) {
        List<String> answers = new ArrayList<>(Arrays.asList(strArr));
        
        answers.removeIf(ans -> ans.contains("ad"));
        
        return answers.toArray(new String[0]);
    }
}