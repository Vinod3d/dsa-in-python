function BinaryToDecimal(){
    let prompt = require("prompt-sync")();
    let bin = prompt("Enter the binary number: ");
    
    if(bin === 0){
        return "0";
    }

    let dec = 0;
    let power = 0;
    
    while(bin > 0){
        let lastBit = bin % 10;
        dec = dec + lastBit * (2 ** power);
        power++;
        bin = Math.floor(bin / 10);
    }
    return dec;
}

console.log(BinaryToDecimal());
