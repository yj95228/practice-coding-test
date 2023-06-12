// https://leetcode.com/problems/climbing-stairs/
/**
 * @param {number} n
 * @return {number}
 */

var climbStairs = function (n) {
  const array = [0, 1, 2];
  if (n <= 2) return array[n];
  for (let i = 3; i <= n; i++) {
    array[i] = array[i - 2] + array[i - 1];
  }
  return array[n];
};
