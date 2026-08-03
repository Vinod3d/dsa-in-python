// 3.28: Candies Distribution
// You are given a collection of candies, where each candy is represented by an integer indicating its type.
// You are also given an integer k, representing the number of distinct candy types each child must receive.

// Each child must receive exactly k distinct candies.
// A candy can be given to only one child and cannot be reused.

// Your task is to determine the maximum number of children that can receive such a distribution.

// The distribution must satisfy both conditions:

// Every child receives exactly k distinct candy types.

// No candy is shared between children.

// If it is not possible to distribute candies under these rules, return 0.


function CandiesDistribute(n, k, candies) {
    let hmap = new Map();
    for (let i = 0; i < candies.length; i++) {
        hmap.set(candies[i], (hmap.get(candies[i]) || 0) + 1);
    }

    let count = 0;
    while (hmap.size >= k) {
        let keys = [...hmap.keys()].slice(0, k);

        for (let key of keys) {
            hmap.set(key, hmap.get(key) - 1);

            if (hmap.get(key) === 0) {
                hmap.delete(key);
            }
        }
        count++;
    }
    return count;
}

console.log(CandiesDistribute(7, 3, [1, 1, 2, 2, 3, 3, 4]));
