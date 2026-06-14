function setMisMatch(nums){
    let hmap = new Map();
    let len = nums.length;
    for (let num of nums) {
        hmap.set(num, (hmap.get(num) || 0) + 1);
    }
    let duplicate = -1;
    let missing = -1;
    for(let i = 0; i<= len; i++){
        if(hmap.has(i) ){
            if(hmap.get(i) == 2){
                duplicate = i;
            }
        } else{
            missing = i;
        }
    }
    return [duplicate, missing];
}


console.log(setMisMatch([1,1,3]))