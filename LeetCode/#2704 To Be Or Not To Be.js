/**
 * @param {string} val1
 * @return {Object}
 */
var expect = function(val1) {
    function toBe(val2) {
       if (val1 === val2) {
           return true
       } else {
           throw new Error('Not Equal')
       }
    }

    function notToBe(val2){
        if (val1 !== val2) {
            return true
        } else {
            throw new Error('Equal')
        }
    }

    return {
        toBe, notToBe
    }
};

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */
