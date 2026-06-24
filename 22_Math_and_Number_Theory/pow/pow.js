function myPow(n, p) {
    function countPower(base, exp) {
        if (exp === 0) return 1;

        let half = countPower(base, Math.floor(exp / 2));
        if (exp % 2 === 0) {
            return half * half;
        } else {
            return base * half * half;
        }
    }
    let absExponent = Math.abs(p);
    let result = countPower(n, absExponent);

    if (p < 0) {
        return 1 / result;
    }

    return result;
}


console.log(myPow(2, 10));
console.log(myPow(2, -3));
console.log(myPow(5, 3));