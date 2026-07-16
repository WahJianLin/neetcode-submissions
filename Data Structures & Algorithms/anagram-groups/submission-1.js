class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        const sortedMap = new Map();
        for (let i = 0; i< strs.length; i++){
            const sortedStr = strs[i].split('').sort().join('');
            if(sortedMap.has(sortedStr)) {
                const value = sortedMap.get(sortedStr);
                value.push([strs[i]]);
                sortedMap.set(sortedStr, value);
            } else {
                sortedMap.set(sortedStr, [strs[i]]);
            }
        }
        return [...sortedMap.values()];
    }
}
