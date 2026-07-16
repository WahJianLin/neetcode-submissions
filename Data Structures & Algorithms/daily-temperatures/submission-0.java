class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        Stack<int[]> stack = new Stack<>();
        int[] ret = new int[temperatures.length];
        for(int i = 0; i<temperatures.length; i++){
            int [] input = new int[]{i,temperatures[i]};
            if(stack.size() == 0) {
                stack.push(input);
            } else {
                while(stack.size()>0){
                    int[] top = stack.peek();
                    
                    if(top[1]<input[1]){
                        ret[top[0]]=input[0]-top[0];
                        stack.pop();
                    } else {
                        break;
                    }
                }
                stack.push(input);
            }
        }
        return ret;
    }
}
