class Solution {
    public int[] twoSum(int[] nums, int target) {
        int [] ret = new int[] {-1,-1};
        int[] original = Arrays.copyOf(nums, nums.length);
        //plan sort array, have pointer on left and right on the sorted array. Find the value
        Arrays.sort(nums);
        int l=0; 
        int r=nums.length-1;
        Integer leftVal = null;
        Integer rightVal = null;
        while(r>l){
            int sum = nums[l] + nums[r]; 
            if(sum == target){
                leftVal= nums[l];
                rightVal=nums[r];
                l=0;
                r=nums.length-1;
                break;
            } else if (sum > target){
                r--;
            } else {
                l++;
            }
        }

        for(int i =0; i<nums.length;i++){
            int val = original[i];
            if(leftVal == val || rightVal == val){
                // System.out.println(""+val +leftVal+rightVal);
                if(ret[0] == -1 ){
                    ret[0] = i;
                } else {
                    ret[1] = i;
                    break;
                }
            }
        }

        return ret;
    }
}
