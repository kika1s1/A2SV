/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    let value = init
    let cnt = value
    return {
        increment :()=>{
            cnt +=1
            return cnt
        },
        decrement :()=>{
            cnt -=1
            return cnt
        },
        reset :()=>{
            cnt = value
            return value
        }
    }
    
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */