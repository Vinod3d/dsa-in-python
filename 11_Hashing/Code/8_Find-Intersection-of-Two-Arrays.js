// 8. Find Intersection of Two Arrays
function findIntersection(array1, array2) {
    const intersection = [];
    const seen = new Set();

    for (let i = 0; i < array1.length; i++) {
        seen.add(array1[i]);
    }

    for (let i = 0; i < array2.length; i++) {
        if (seen.has(array2[i])) {
            intersection.push(array2[i]);
            seen.delete(array2[i]);
        }
    }

    return intersection;
}

const array1 = [1, 2, 3, 4];
const array2 = [3, 4, 5, 6];    
console.log(findIntersection(array1, array2));