// 202 happy number
function isHappy(n) {
    let set = new Set();
    while(n != 1 && !set.has(n)){
        set.add(n);
        n = getSumOfSquares(n);
    }
    return n == 1;
};

function getSumOfSquares(n) {
    let sum = 0;
    while(n > 0){
        let digit = n % 10;
        sum += digit * digit;
        n = Math.floor(n / 10);
    }
    return sum;
}

const n = 19;
console.log(isHappy(n));