var nextGreaterElements = function (nums) {
  // let map = new Map();
  let stack = [];
  let res = new Array(nums.length).fill(-1);
  for (let i = 0; i < nums.length * 2; i++) {
    while (
      stack.length &&
      nums[i % nums.length] > nums[stack[stack.length - 1]]
    ) {
      let index = stack.pop();
      res[index] = nums[i % nums.length];
    }
    stack.push(i % nums.length);
  }

  return res;
};