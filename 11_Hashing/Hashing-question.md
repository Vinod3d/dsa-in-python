## 1 Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
// Two Sum 1
```js
function twoSum(nums, target) {
    let map = new Map();

    for (let i = 0; i < nums.length; i++) {
        const complement = target - nums[i];  
        if (map.has(complement)) {
            return [map.get(complement), i];
        }
        map.set(nums[i], i);
    }
}

const nums = [2, 7, 11, 15];
const target = 9;
console.log(twoSum(nums, target));
```

## 2. Given two arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.
// Intersection of Two Arrays

```js
function intersection(nums1, nums2) {
    let set1 = new Set(nums1);
    let set2 = new Set(nums2);
    let intersection = [];
    for (let num of set1) {
        if (set2.has(num)) {
            intersection.push(num);
        }
    }
    return intersection;
}

const nums1 = [1, 2, 2, 1];
const nums2 = [2, 2];
console.log(intersection(nums1, nums2));
```


## 3. Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
// Intersection of Two Arrays II
```js
function intersection(nums1, nums2) {
      
}

const nums1 = [1, 2, 2, 1];
const nums2 = [2, 2];
console.log(intersection(nums1, nums2));
```
