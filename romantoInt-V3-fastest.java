import java.util.HashMap;
class Solution {
    // use switch in this method
    private static int getIntFromRoman(char roman){
		int a = 0;
		switch (roman) {
		case 'I':
			a= 1;
			break;
		case 'V':
			a= 5;
			break;
		case 'X':
			a= 10;
			break;
		case 'L':
			a= 50;
			break;
		case 'C':
			a= 100;
			break;
		case 'D':
			a= 500;
			break;
		case 'M':
			a= 1000;
			break;
		default:
			break;
		}
		return a;
	}
//     private HashMap<Character, Integer> romanChar = new HashMap<Character, Integer>();
//         {
//             romanChar.put('I', 1);
//             romanChar.put('V', 5);
//             romanChar.put('X', 10);
//             romanChar.put('L', 50);
//             romanChar.put('C', 100);
//             romanChar.put('D', 500);
//             romanChar.put('M', 1000);
//         }
    public int romanToInt(String s){
        
        // int last = 0;
        // int res = 0;
        // for(int i = (s.length() - 1); i >= 0; i--){
        //     if(romanChar.get(s.charAt(i)) < last && i < s.length() - 1){
        //         res -= romanChar.get(s.charAt(i));
        //     }else{
        //         res += romanChar.get(s.charAt(i));
        //     }
        //     last = romanChar.get(s.charAt(i));
        // }
        // return res;
        
        int stack = 0;
		int last = 0;
        
		for(int i = (s.length() - 1); i >= 0; i--){
            
			int curInt = getIntFromRoman(s.charAt(i));
            
			if(curInt < last && i < s.length() - 1){
				stack -= curInt;
			}else{
                stack += curInt;
            }
            
			last = curInt;
            
		}
		return stack;
    }
	
}