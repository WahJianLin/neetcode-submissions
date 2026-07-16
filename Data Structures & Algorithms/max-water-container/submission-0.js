class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    maxArea(heights) {
        let l = 0;
        let r = heights.length-1;
        let maxArea = 0 ;
        while(l<r) {
            const height = Math.min(heights[l], heights[r]);
            const area = height * (r-l);
            maxArea = Math.max(area, maxArea);
            if (heights[r]>heights[l]) {
                l++;
            } else {
                r--;
            }
        }
        return maxArea;
    }
}
