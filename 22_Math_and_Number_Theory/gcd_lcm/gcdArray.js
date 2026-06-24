function findArrayGCD(arr) {
    let min = Math.min(...arr);
    let max = Math.max(...arr);

    function gcd(a, b) {
        if (b === 0) {
            return a;
        }
        return gcd(b, a % b);
    }

    let result = gcd(min, max);
    console.log(result);
}

console.log(findArrayGCD([42, 56, 70]));