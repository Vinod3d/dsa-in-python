function sumOfUnique(nums) {
    let hmap = new Map();
    for (let i = 0; i < nums.length; i++) {
        hmap.set(nums[i], (hmap.get(nums[i]) || 0) + 1);
    }

    let sum = 0;
    for (let [key, value] of hmap) {
        if (value === 1) {
            sum += key;
        }
    }

    return sum;
}

const nums = [1, 2, 3, 4, 5];
console.log(sumOfUnique(nums));