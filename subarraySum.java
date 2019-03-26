class Solution {
    public int subarraySum(int[] nums, int k) {
        int res = 0;
        if(nums == null || nums.length == 0) return res;
        for(int i = 0; i < nums.length; i++){
            int temp = k;
            for(int j = i; j >= 0; j--){
                temp = temp - nums[j];
                if(temp == 0) res++;
            }
        }
        return res;
    }
}