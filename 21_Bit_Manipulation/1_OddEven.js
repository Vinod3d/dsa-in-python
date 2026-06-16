function OddEven(n){
    return (n&1)? "Odd" : "Even"; 
}

console.log(OddEven(10))

function isPowerOfTwo(n) {

    if((n & (n-1)) === 0) {
        return true;
    }
    else {
        return false;
    }
}

console.log(isPowerOfTwo(10))