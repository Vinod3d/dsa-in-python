// 4. Valid Anagram

function validAnagram(string1, string2) {
    if (string1.length !== string2.length) {
        return false;
    }

    const frequencyMap = {};

    // create the frequency map
    for (let char of string1) {
        frequencyMap[char] = (frequencyMap[char] || 0) + 1;
    }

    // check the frequency map
    for (let char of string2) {
        if (!frequencyMap[char]) {
            return false;
        }
        frequencyMap[char]--;
    }

    return true;
}

const string1 = "anagram";
const string2 = "nagaram";
console.log(validAnagram(string1, string2));
