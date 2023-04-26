// https://leetcode.com/problems/two-sum/

// 1차 시도 - Brute Force
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  for (let i = 0; i < nums.length - 1; i++) {
    for (let j = i + 1; i < nums.length; j++) {
      if (nums[i] + nums[j] === target) return [i, j];
    }
  }
};

// 2차 시도 - x = value - y
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  for (let i = 0; i < nums.length - 1; i++) {
    const idx = [
      ...nums.slice(0, i),
      null,
      ...nums.slice(i + 1, nums.length),
    ].indexOf(target - nums[i]);
    if (idx >= 0) return [i, idx];
  }
};

// 3차 시도 - Hash Map
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  const obj = {};
  for (let i = 0; i < nums.length; i++) {
    if (target - nums[i] in obj) return [obj[target - nums[i]], i];
    obj[nums[i]] = i;
  }
};
