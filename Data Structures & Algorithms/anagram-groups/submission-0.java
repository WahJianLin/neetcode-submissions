class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> sortedStrings = new HashMap<>();
        for(int i = 0; i < strs.length; i++) {
            char[] sortedChar = strs[i].toCharArray();
            Arrays.sort(sortedChar);
            String charToString = new String(sortedChar);
            if(sortedStrings.containsKey(charToString)) {
                List<String> matchingList = sortedStrings.get(charToString);
                matchingList.add(strs[i]);
                sortedStrings.put(charToString, matchingList);
            } else {
                List<String> list = new ArrayList<String>();
                list.add(strs[i]);
                sortedStrings.put(charToString, list);
            }
        }
        return new ArrayList(sortedStrings.values());
    }
}
