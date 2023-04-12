var TimeLimitedCache = function() {
    this.cache = {} // key: value
    this.cache_timers = {} // key: setTimeoutId
};

/** 
 * @param {number} key
 * @param {number} value
 * @param {number} time until expiration in ms
 * @return {boolean} if un-expired key already existed
 */
TimeLimitedCache.prototype.set = function(key, value, duration) {
    this.cache[key] = value
    let exist = key in this.cache_timers
    if (exist) {
        clearTimeout(this.cache_timers[key])
    }
    let id = setTimeout(() => {
        delete this.cache[key]
        delete this.cache_timers[key]
    }, duration)
    this.cache_timers[key] = id
    return exist
};

/** 
 * @param {number} key
 * @return {number} value associated with key
 */
TimeLimitedCache.prototype.get = function(key) {
    if (key in this.cache) return this.cache[key]
    return -1
};

/** 
 * @return {number} count of non-expired keys
 */
TimeLimitedCache.prototype.count = function() {
    return Object.keys(this.cache).length
};

/**
 * Your TimeLimitedCache object will be instantiated and called as such:
 * var obj = new TimeLimitedCache()
 * obj.set(1, 42, 1000); // false
 * obj.get(1) // 42
 * obj.count() // 1
 */

