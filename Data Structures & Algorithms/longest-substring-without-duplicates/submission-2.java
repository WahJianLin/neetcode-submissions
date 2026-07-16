class Solution {
    /*
        iterate through string
        if string builder does not contain target char. Add it to string builder
        if it does contain target string. Record largest length and then trigger 
        a while loop to remove the first character until there is no over lap
        then addin new character
    */
    public int lengthOfLongestSubstring(String s) {
        StringBuilder sb = new StringBuilder();
        int maxLen = 0;

        for(int i=0; i<s.length();i++){
            char target = s.charAt(i);
            if(sb.indexOf(""+target)==-1){
                sb.append(target);
            }else {
                maxLen = Math.max(maxLen, sb.length());
                while(sb.indexOf(""+target)!=-1){
                    sb.deleteCharAt(0);
                }
                sb.append(target);
            }
        }
        return maxLen = Math.max(maxLen, sb.length());
    }
}
