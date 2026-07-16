class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums) {
        const map = new Map();
        let longest = 0;
        for(let i = 0; i<nums.length; i++){
            let val = nums[i];
            let targetLongest = 1;
            if(map.has(val-1)){
                targetLongest = map.get(val-1)+1;
                map.set(val,targetLongest);
            } else{
                map.set(val, 1);
                if(longest==0) {
                    longest = 1;
                }
            }
            while(map.has(++val)){
                targetLongest++;
                map.set(val,targetLongest);
            }
            if(targetLongest>longest){
                longest = targetLongest;
            }
        }
        
        return longest;
    }
}
