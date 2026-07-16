class MinStack {
    Stack<Integer> stack;
    Stack<Integer> temp;
    
    public MinStack() { 
        stack = new Stack<>();
        temp = new Stack<>();
    }
    
    public void push(int val) {
        stack.push(val);
        if(temp.empty() || temp.peek()>= val) {
            temp.push(val);
        }
    }
    
    public void pop() {
        int poppedVal= stack.pop();
        if(temp.peek() == poppedVal){
            temp.pop();
        }
    }
    
    public int top() {
        return stack.peek();
    }
    
    public int getMin() {
        return temp.peek();
    }
}
