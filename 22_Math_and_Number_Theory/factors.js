function findFactors(n){
    let factors = [1, n];
    for(let i = 2; i*i <= n; i++){
        if(n%i == 0){
            factors.push(i);
            if(i !== n/i){
                factors.push(n/i);
            }
        }
    }
    return factors;
}

console.log(findFactors(20));

// kth factor of n
function kthFactor(n, k){
    let factors = findFactors(n);
    factors.sort((a, b) => a - b);
    return factors[k - 1];
}

console.log(kthFactor(20, 4));