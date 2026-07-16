class Solution {
    public int evalRPN(String[] tokens) {
        /*
            create stack
            push numbers into stack (only max of 2 numbers in stack)
            Once an operation is detected pop out numbers and do the math. The first value popped value is the secondary value in operation
            Push result back into stack
            repeat steps 2-4
            once for loop is complete peek at top of stack and that should be the end result

            Assuming tokens always end in an operation. 
            Assuming tokens has an alertnating order ofnumbers and operations. Except the first 2 values are numbers
        */
        Stack<String> nums = new Stack<>();
        for(int i = 0; i<tokens.length;i++){
            String target = tokens[i];
            if (!target.matches("[-+*/]")) {
                nums.push(target);
            } else {
                int num2 = Integer.parseInt(nums.pop());
                int num1 = Integer.parseInt(nums.pop());
                int result = calc(num1, num2, target);
                nums.push(""+result);
            }
        System.out.println(nums);
        }
        
        return Integer.parseInt(nums.peek());
    }
    
    private int calc(int num1, int num2, String operation){
        switch(operation) {
            case "+":
                return num1 + num2;
            case "-":
                return num1 - num2;
            case "*":
                return num1 * num2;
            case "/":
                return num1 / num2;
            default:
            break;
        }
        return 0;
    }
}
