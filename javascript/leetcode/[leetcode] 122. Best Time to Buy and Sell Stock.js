// https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

// 1차 시도 - Brute Force
/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function (prices) {
  let answer = 0;
  for (let i = 0; i < prices.length - 1; i++) {
    for (let j = i + 1; j < prices.length; j++) {
      if (prices[j] - prices[i] > answer) answer = prices[j] - prices[i];
    }
  }
  return answer;
};

// 2차 시도 - 투 포인터
/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function (prices) {
  let left = 0; // Buy
  let right = 1; // sell
  let answer = 0;
  while (right < prices.length) {
    if (prices[left] < prices[right]) {
      answer = Math.max(answer, prices[right] - prices[left]);
    } else {
      left = right;
    }
    right++;
  }
  return answer;
};
