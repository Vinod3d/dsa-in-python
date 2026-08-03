// 10. Group Anagrams
function groupAnagrams(strs) {
    const map = new Map();

    for (let word of strs) {

        // Create sorted key
        let sortedWord = word
            .split('')
            .sort()
            .join('');

        if (!map.has(sortedWord)) {
            map.set(sortedWord, []);
        }

        map.get(sortedWord).push(word);
    }
    return Array.from(map.values());
}

const strs = ["eat","tea","tan","ate","nat","bat"];
console.log(groupAnagrams(strs));

