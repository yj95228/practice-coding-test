// https://leetcode.com/problems/maximum-subarray/
// Dynamic Programming
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function (nums) {
  let max = nums[0];
  for (let i = 1; i < nums.length; i++) {
    nums[i] = Math.max(0, nums[i - 1]) + nums[i];
    max = Math.max(max, nums[i]);
  }
  return max;
};
