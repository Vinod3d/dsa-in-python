// you are given an array of strings names, and an array of integers heights
// where names[i] is the name of the i-th person and heights[i] is the height of the i-th person
// return the array of names sorted in descending order of heights


function sortPeople(names, heights) {
    const map = new Map();
    for (let i = 0; i < names.length; i++) {
        map.set(heights[i], names[i]);
    }
    
    // Sort heights in descending order
    heights.sort((a, b) => b - a);
    
    // Map sorted heights to names using the hash map
    return heights.map(height => map.get(height));
}

const names = ["Alice", "Bob", "Charlie"];
const heights = [165, 175, 185];
console.log(sortPeople(names, heights));
