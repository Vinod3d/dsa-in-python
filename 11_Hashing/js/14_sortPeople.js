function sortPeople(names, heights) {
    let hmap = new Map();
    for(let i = 0; i<heights.length; i++){
        hmap.set(heights[i], names[i]);
    }
    
    heights.sort((a, b) => b - a);
    
    let result = [];
    for(let i = 0; i<heights.length; i++){
        result.push(hmap.get(heights[i]));
    }
    
    return result;
}


const names = ["Mary","John","Emma"];
const heights = [180,165,170];

console.log(sortPeople(names, heights));
