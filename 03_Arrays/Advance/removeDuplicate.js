function removeDuplicate(nums){
    let k = 1;
    for(let i = 0; i<nums.length; i++){
        
        if(nums[i] != nums[i+1]){
            nums[k] = nums[i+1];
            k++;
        }
    }
    return k;
}

let nums = [12, 12, 15, 18, 20, 20, 23, 27, 30, 30]
console.log(removeDuplicate(nums))
