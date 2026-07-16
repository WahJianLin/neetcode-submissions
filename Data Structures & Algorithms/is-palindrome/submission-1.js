class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        const lowerStr=s.toLowerCase();
        const normalStr = lowerStr.replaceAll(/[^a-z0-9]/g,'');
        const revStr = normalStr.split('').reverse().join('');
        console.log(normalStr);
        return normalStr===revStr;
    }
}
