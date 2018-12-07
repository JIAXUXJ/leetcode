import java.util.HashMap;
class Solution {
    public int romanToInt(String s) {
        HashMap<Character, Integer> romanChar = new HashMap<Character, Integer>();
        romanChar.put('I', 1);
        romanChar.put('V', 5);
        romanChar.put('X', 10);
        romanChar.put('L', 50);
        romanChar.put('C', 100);
        romanChar.put('D', 500);
        romanChar.put('M', 1000);
        int last = 0;
        int res = 0;
        for(int i = (s.length() - 1); i >= 0; i--){
            if(romanChar.get(s.charAt(i)) < last && i < s.length() - 1){
                res -= romanChar.get(s.charAt(i));
            }else{
                res += romanChar.get(s.charAt(i));
            }
            last = romanChar.get(s.charAt(i));
        }
        return res;
    }
}