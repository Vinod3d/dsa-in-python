// 5. Count Frequency of Array Elements
function countFrequencyOfArrayElements(array) {
    const frequencyMap = {};

    // create the frequency map
    for (let num of array) {
        frequencyMap[num] = (frequencyMap[num] || 0) + 1;
    }

    return frequencyMap;
}

const array = [1, 2, 3, 1, 2, 2, 3, 3, 3, 4];
console.log(countFrequencyOfArrayElements(array));