class Solution {
    public boolean isAnagram(String s, String t) {
        // two options convert strings to letter array and then do a .sort
        char[] sArr = s.toCharArray();
        char[] tArr = t.toCharArray();
        Arrays.sort(sArr);
        Arrays.sort(tArr);
        return Arrays.equals(sArr, tArr);
    }
}
