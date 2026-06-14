
// If there is a tie, return the smallest one. If there is no such element, return -1.


function frequentElement(nums) {
    let hmap = new Map();
    for(let i = 0; i<nums.length; i++){
        if (nums[i] % 2 === 0) {
            hmap.set(nums[i], (hmap.get(nums[i]) || 0) + 1);
        };
    }

    let maxFreq = 0;
    let frequentElement = -1;
    
    for(let [key, value] of hmap){
        if(value > maxFreq){
            maxFreq = value;
            frequentElement = key;
        }if (value > maxFreq || (value === maxFreq && key < frequentElement)) {
            maxFreq = value;
            frequentElement = key;
        }
    }

    return frequentElement;
}

const nums = [1, 2, 2, 3, 3, 3, 4];
console.log(frequentElement(nums));