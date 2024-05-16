/**
 * @param {string} val
 * @return {Object}
 */
var expect = function(val) {
  var assertion = {
    toBe: function(a) {
      if (val === a) {
        return true;
      }
      throw new Error("Not Equal");
    },
    notToBe: function(a) {
      if (val !== a) {
        return true;
      }
      throw new Error("Equal");
    },
  };

  return assertion;
};

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */