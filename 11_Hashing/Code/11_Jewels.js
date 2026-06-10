// 771. Jewels and Stones

function numJewelsInStones(jewels, stones) {
    let jewelSet = new Set(jewels);
    let count = 0;
    for(let stone of stones){
        if(jewelSet.has(stone)){
           count++;
        }
    }

    return count;
}

const jewels = "aA";
const stones = "aAAbbbb";
console.log(numJewelsInStones(jewels, stones));