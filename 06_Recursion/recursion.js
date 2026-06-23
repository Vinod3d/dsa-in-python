let prompt = require("prompt-sync")();

let n = Number(prompt("Enter the number:")); 

function hello(n){
    if(n==0){
        return;
    }
    console.log("Hello");
    return hello(n-1);
}

hello(n);