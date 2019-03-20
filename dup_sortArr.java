// class Solution {
//     public int removeDuplicates(int[] nums) {
//         int len = nums.length;
//         int prev;
//         int res = 0;
//         if(len > 0){
//             prev = nums[0];
//             res++;
//         }else{
//             return res;
//         }
//         for(int i = 1; i < len; i++){
            
//             if(nums[i] != prev){
//                 res++;
//             }
//             prev = nums[i];
//         }
        
//         return res;
//     }
// }

class Solution {
    public int removeDuplicates(int[] nums) {
        int n = nums.length;
        int res = 1;
        for(int i = 1; i<n; i++){
            if(nums[i] != nums[i-1]) nums[res++] = nums[i];
        }
        return res;
    }
}