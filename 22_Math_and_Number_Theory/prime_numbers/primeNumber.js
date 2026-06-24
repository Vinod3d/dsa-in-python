// prime number using sieve Erathostarness


function primeNumber(n){
    let prime = new Array(n + 1).fill(true);
    for(let i = 2; i<= Math.sqrt(n); i++){
        if(prime[i]){
            for(let j = i*i; j<=n; j+=i){
                prime[j] = false;
            }
        }
    }

    let ans = [];
    for(let i = 2; i<=n; i++){
        if(prime[i]) ans.push(i);
    }
    return ans;
}

console.log(primeNumber(25))