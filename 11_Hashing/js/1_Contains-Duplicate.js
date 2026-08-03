// ================== 1. Contains Duplicate ==================

// Input: [1,2,3,1]
// Output: true

function checkDuplicate(array) {
    const seen = new Set();

    for (let num of array) {
        if (seen.has(num)) {
            return true;
        }
        seen[num] = true;
    }
    return false;
}

const array = [1,2,3,1];
console.log(checkDuplicate(array));