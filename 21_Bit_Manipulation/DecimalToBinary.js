
function decimalToBinary(){
    let prompt = require("prompt-sync")();
    let num = prompt("Enter the decimal number: ");
    if(num === 0){
        return "0"
    }
    let ans = ""
    while(num > 0){
        let bin = num % 2;
        ans = bin + ans;
        num = Math.floor(num / 2);
    }
    return ans;
}

console.log(decimalToBinary());
