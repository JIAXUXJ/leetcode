class Solution {
    public int lengthOfLongestSubstring(String s) {
        int freq[256] = {0};
        int l = 0, r = -1; //滑动窗口为s[l...r]
        int res = 0;
        while(l < s.size()){
            if(r + 1 < s.size() && freq[s[r+1]] == 0){
                r++;
                freq[s[r]]++;
            }else {   //r已经到头 || freq[s[r+1]] == 1
                freq[s[l]]--;
                l++;
            }
            res = max(res, r-l+1);
        }
        return res;
    }
}