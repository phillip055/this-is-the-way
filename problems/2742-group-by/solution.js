/**
 * @param {Function} fn
 * @return {Array}
 */
Array.prototype.groupBy = function(fn) {
    return this.reduce((acc, x, i) => {
        let res = fn(x, i)
        if (!(res in acc)) acc[res] = []
        acc[res].push(x)
        return acc
    }, {})
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */

