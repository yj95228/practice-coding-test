// https://leetcode.com/problems/palindromic-substrings/submissions/
/**
 * @param {string} s
 * @return {number}
 */
var countSubstrings = function(s) {
    let strArray = [];
    for(let i = 0; i < s.length; i++){
        for(let j = s.length; i < j; j--){
            str = s.slice(i,j)
            for(let k = 0; k < str.length; k++){
                if(str[k] !== str[str.length-1-k]) break;
                if(k === str.length-1) strArray.push(str);
            }
            // if(str === str.split('').reverse().join('')) strArray.push(str)
        }
    }
    return strArray.length
};
