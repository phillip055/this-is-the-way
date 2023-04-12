/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    return arr.reduce((newArray, x, i) => {
        newArray.push(fn(x,i))
        return newArray
    }, [])
};

