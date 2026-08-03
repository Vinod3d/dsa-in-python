// 2. Character Frequency Counter

function characterFrequencyCounter(string) {
    const frequencyMap = {};

      // create the frequency map
    for (let char of string) {
        frequencyMap[char] = (frequencyMap[char] || 0) + 1;
    }

    return frequencyMap;
}

const string = "hello";
console.log(characterFrequencyCounter(string));