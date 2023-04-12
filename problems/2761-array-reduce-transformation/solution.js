/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init = 0) {
    if (nums.length == 0) {
        return init
    }
    firstElement = nums.shift()
    return reduce(nums, fn, fn(init, firstElement))
};

