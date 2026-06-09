// find number frequency using map

let arr = [1, 2, 3, 2, 1, 3, 4, 5, 1, 1];

let map = new Map();

for (let i = 0; i < arr.length; i++) {
    let num = arr[i];
    map.set(num, (map.get(num) || 0) + 1);
}

console.log(map);