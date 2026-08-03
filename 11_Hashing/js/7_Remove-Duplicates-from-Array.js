// 7. Remove Duplicates from Array
function RemoveDuplicate(array){
    // return [...new Set(array)]

    let set = new Set();
    for(let i = 0; i < array.length; i++){
        if(set.has(array[i])){
            continue;
        }
        set.add(array[i]);
    }
    return Array.from(set);
}

const array = [1, 2, 2, 3, 3, 3, 4];
console.log(RemoveDuplicate(array));