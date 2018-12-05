class Solution {
    public String reverseString(String s) {
        // StringBuilder newString=new StringBuilder();
        int length = s.length();
        char [] newS = s.toCharArray();
        
        for(int i = 0; i < length / 2; i++){
            // newString.append(s.charAt(length-1-i));
            char cur = newS[i];
            newS[i] = newS[length - 1 - i];
            newS[length - 1 - i] = cur;
        }        
        String res = new String(newS);
        return res;
    }
}