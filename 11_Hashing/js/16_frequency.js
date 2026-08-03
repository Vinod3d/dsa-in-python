// Find the frequency of elements in an integer array
function frequency(arr){
    let hmap = new Map();
    for(let i = 0; i<arr.length; i++){
        hmap.set(arr[i], (hmap.get(arr[i]) || 0) + 1);
    }


    
    let result = [];
    for (let [key, value] of hmap) {
        result.push(`${key} ${value}`);
    }
    
    return result.join('\n');
}

const nums = [1, 2, 2, 3, 3, 3, 4];
console.log(frequency(nums));