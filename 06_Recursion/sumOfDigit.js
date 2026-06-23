function sumOfDigit(num){
    if(num < 10){
        return num;
    }
    return (num % 10) + sumOfDigit(Math.floor(num / 10));
}

console.log(sumOfDigit(123));