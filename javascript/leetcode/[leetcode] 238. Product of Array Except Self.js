// https://leetcode.com/problems/product-of-array-except-self/
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function (nums) {
  const product = nums.reduce((a, c) => {
    return c === 0 ? a : a * c;
  }, 1);
  if (nums.includes(0)) {
    return nums.filter((x) => x === 0).length === 1
      ? nums.map((x) => (x === 0 ? product : 0))
      : nums.fill(0);
  } else {
    return nums.map((x) => product / x);
  }
};
