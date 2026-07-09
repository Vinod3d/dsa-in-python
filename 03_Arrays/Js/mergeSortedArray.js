function mergeSortedArray(arr1, arr2) {
    let temp = new Array(arr1.length + arr2.length);
    let i = 0;
    let j = 0;
    let k = 0;
    while (i < arr1.length && j < arr2.length) {
        if (arr1[i] <= arr2[j]) {
            temp[k] = arr1[i];
            i++;
        } else {
            temp[k] = arr2[j];
            j++;
        }
        k++;
    }
    while(i< arr1.length){
        temp[k] = arr1[i];
        i++;
        k++;
    }
    while(j< arr2.length){
        temp[k] = arr2[j];
        j++;
        k++;
    }
    return temp;
}

arr1 = [1,2,3,0,0,0];
arr2 = [2,5,6];
console.log(mergeSortedArray(arr1, arr2))