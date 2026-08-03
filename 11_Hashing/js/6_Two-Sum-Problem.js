// 6. Two Sum Problem

function twoSum(array, target) {
    const numMap = new Map();

    for (let i = 0; i < array.length; i++) {
        const complement = target - array[i];

        if (numMap.has(complement)) {
            return [numMap.get(complement), i];
        }

        numMap.set(array[i], i);
    }

    return null;
}

const array = [2, 7, 11, 15];
const target = 9;
console.log(twoSum(array, target));

// dry run
// i = 0, array[0] = 2
// complement = 9 - 2 = 7
// numMap.has(7) = false
// numMap.set(2, 0)

// i = 1, array[1] = 7
// complement = 9 - 7 = 2
// numMap.has(2) = true
// return [numMap.get(2), 1] = [0, 1]

