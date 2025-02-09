class Solution {
    public int solution(String myString, String pat) {
        
        String[] arr = myString.split("");
        
        for (int i = 0; i < arr.length; i++) {
            if (arr[i].equals("B")) {
                arr[i] = "A";
            } else if (arr[i].equals("A")) {
                arr[i] = "B";
            }
        }
        
        String newStr = String.join("", arr);
        
        return newStr.contains(pat) ? 1 : 0;
    }
}