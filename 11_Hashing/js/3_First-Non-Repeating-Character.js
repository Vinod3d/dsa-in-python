// 3. First Non-Repeating Character

function firstNonRepeatingCharacter(string) {
    const frequencyMap = {};

    // create the frequency map
    for (let char of string) {
        frequencyMap[char] = (frequencyMap[char] || 0) + 1;
    }

    // find the first non-repeating character
    for (let char of string) {
        if (frequencyMap[char] === 1) {
            return char;
        }
    }

    return null;
}

const string = "leetcode";
console.log(firstNonRepeatingCharacter(string));