class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {
        const leftSideArr = [];
        const rightSideArr = [];
        const ret = [];
        for( let i = 0; i<nums.length; i++) {
            const target = nums.length-i-1;
            if(i==0){
                leftSideArr.push(nums[i]);

                rightSideArr.push(nums[target]);
            } else {
                const leftCalc = leftSideArr[i-1]*nums[i];
                const rightCalc = rightSideArr[i-1]*nums[target];
                leftSideArr.push(leftCalc);
                rightSideArr.push(rightCalc);
            }
        }
        rightSideArr.reverse();

        for( let j = 0; j<nums.length; j++) {
            if(j==0) {
                ret.push(rightSideArr[j+1]);
            } else if (j==nums.length-1) {
                ret.push(leftSideArr[j-1]);
            } else {
                ret.push(rightSideArr[j+1]*leftSideArr[j-1]);
            }
        }
        return ret;
    }
}
