// 9. Longest Consecutive Sequence
function longestConsecutive(array) {
    const seen = new Set(array);
    let longestStreak = 0;

    for (let num of array) {
        // Check if 'num' is the start of a sequence
        if (!seen.has(num - 1)) {
            let currentNum = num;
            let currentStreak = 1;

            // Count the length of the sequence starting from 'num'
            while (seen.has(currentNum + 1)) {
                currentNum += 1;
                currentStreak += 1;
            }

            // Update the longest streak found so far
            longestStreak = Math.max(longestStreak, currentStreak);
        }
    }

    return longestStreak;
}

const array = [100, 4, 200, 1, 3, 2];
console.log(longestConsecutive(array)); // Output: 4