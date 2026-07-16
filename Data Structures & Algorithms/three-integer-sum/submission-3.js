class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    //-4,-1,-1,0,1,2
    threeSum(nums) {
        const ret = [];
        nums.sort(function(a,b) {return a-b});
        console.log(nums)
        for(let i = 0; i<nums.length;i++){
            if(i!=0){
                while(nums[i]==nums[i-1]){
                    i++;
                }
            }
            let l = i+1;
            let r = nums.length-1;
            while(l<nums.length-1) {
                if(nums[i]+nums[l]+nums[r]==0){
                    ret.push([nums[i],nums[l],nums[r]]);
                    l++;
                    while(nums[l]==nums[l-1]){
                        l++;
                    }
                    r = nums.length-1;
                    continue;
                }
                r--;
                if(l>=r){
                    l++;
                    r = nums.length-1;
                }
            }
        }
        return ret;
    }
}
