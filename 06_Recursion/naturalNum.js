// print natural number from 1 to N

function naturalNum(n) {
    if(n==0){
        return;
    }
    console.log(n);
    return naturalNum(n-1);
}

naturalNum(5);


// print natural number from N to 1


function printNumbers(n) {
   if (n === 0) {
    return;
  }
  
  process.stdout.write(`${n} `)
  return printNumbers(n - 1)
}

printNumbers(5);

