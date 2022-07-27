// https://leetcode.com/problems/longest-palindromic-substring/submissions/
/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function(s) {
    let strArray = [s[0]];
    for(let i = 0; i < s.length; i++){
        for(let j = s.length; i < j && Math.abs(i-j) > Math.max(...strArray.map(s => s.length)); j--){
            str = s.slice(i,j)
            for(let k = 0; k < str.length; k++){
                if(str[k] !== str[str.length-1-k]) break;
                if(k === str.length-1) strArray.push(str);
            }
            // if(str === str.split('').reverse().join('')) strArray.push(str)
        }
    }
    return strArray.sort((a,b) => {
        if(a.length < b.length) return 1
        if(a.length > b.length) return -1
        return 0
    })[0]
};
