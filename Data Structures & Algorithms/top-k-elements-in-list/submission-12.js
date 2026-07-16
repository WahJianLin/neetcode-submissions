class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        const map = new Map();
        const ret = [];
        for(let i =0;i<nums.length; i++){
            if(map.has(nums[i])) {
                const value = map.get(nums[i])+1;
                map.set(nums[i],value);
            } else {
                map.set(nums[i], 1);
            }
        }
        const sortedMap = new Map([...map.entries()].sort((a, b) => b[1] - a[1]));

        for (let [key, value] of sortedMap) {
            ret.push(key);
            if(ret.length=== k){
                break;
            }
        }

        return ret;
    }
}
