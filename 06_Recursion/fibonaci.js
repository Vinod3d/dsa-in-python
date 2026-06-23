
// fibonachi series useing recursion
function fiboSeries(n){
    let fiboseries = [0, 1, ];
    function fibo(n){
        if(n==0){
            return 0;
        }
        
        if(n==1){
            return 1;
        }

        return fibo(n-1) + fibo(n-2);
    }
    for(let i=2; i<n; i++){
        fiboseries.push(fibo(i));
    }
    return fiboseries;
}

console.log(fiboSeries(10));


// finbonachi Series using normal way
function fibonachiSeries(n){
    let fiboseries = [0, 1];
    for(let i=2; i<n; i++){
        fiboseries.push(fiboseries[i-1] + fiboseries[i-2]);
    }
    return fiboseries;
}

console.log(fibonachiSeries(10));