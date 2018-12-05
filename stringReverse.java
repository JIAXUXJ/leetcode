class Solution {
    public String reverseString(String s) {
        StringBuilder newString=new StringBuilder();
        int length=s.length();
        
        for(int i=0;i<length;i++){
            newString.append(s.charAt(length-1-i));
        }        
        return newString.toString();
    }
}