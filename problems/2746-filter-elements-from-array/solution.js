/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    return arr.reduce((newArray, x, i) => {
        if (fn(x,i)) {
            newArray.push(x)
        }
        return newArray
    }, [])
};

