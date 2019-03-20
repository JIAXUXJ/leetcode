/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    var len = nums.length;
    var res = 0;
    if(len == 0){
        return res;
    }
    for(var i = 0; i < len; i++){
        if(nums[i] != nums[i-1]){
            nums[res++] = nums[i]
        }
    }
    return res;
};