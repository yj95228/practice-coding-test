// https://leetcode.com/problems/maximum-product-subarray/
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxProduct = function (nums) {
  let result = nums[0];
  let globalMax = nums[0];
  let globalMin = nums[0];

  for (let i = 1; i < nums.length; i++) {
    let localMax = Math.max(globalMax * nums[i], nums[i], globalMin * nums[i]);
    let localMin = Math.min(globalMax * nums[i], nums[i], globalMin * nums[i]);

    globalMax = Math.max(localMax, localMin);
    globalMin = Math.min(localMax, localMin);

    result = Math.max(result, globalMax);
  }

  return result;
};
