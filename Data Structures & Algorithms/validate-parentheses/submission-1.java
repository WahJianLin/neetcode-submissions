class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        for(int i=0; i<s.length(); i++){
            char targetChar = s.charAt(i);
            if(targetChar == '('
                ||targetChar == '{'
                ||targetChar == '['){
                    stack.push(targetChar);
            } else {
            // can swap to a switch case statement
                if(stack.size()==0){
                    return false;
                }
                char poppedChar = stack.pop();
                if(targetChar == ')') {
                    if(poppedChar != '(') {
                        return false;
                    }
                } else if(targetChar == '}') {
                    if(poppedChar != '{') {
                        return false;
                    }
                } else {
                    if(poppedChar != '[') {
                        return false;
                    }
                }
            }
        }
        if(stack.size()>0){
            return false;
        }
        return true;
    }
}
