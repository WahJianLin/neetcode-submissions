class Solution {
    /*

    */
    public boolean checkInclusion(String s1, String s2) {
        final int targetLen = s1.length();
        for (int i = 0;i<s2.length(); i++){
            if(s1.contains(s2.charAt(i)+"")){
            StringBuilder originalString = new StringBuilder(s1);
            StringBuilder matchString = new StringBuilder();
                int j = i;
                while(j<s2.length()){
                    String charStr=s2.charAt(j)+"";
                    int checkIndex = originalString.indexOf(charStr);
                    if(checkIndex==-1){
                        break;
                    } else {
                        originalString.deleteCharAt(checkIndex);
                        matchString.append(charStr);
                    }
                    if(matchString.length()==targetLen){
                        return true;
                    }
                    j++;
                }
            }
        }
        return false;
    }
}
