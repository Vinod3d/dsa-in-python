// JavaScript code here
function mergeArrays(arr1, m, arr2, n) {
    let i = m-1;
    let j = n-1;
    let k = m+n-1;

    while (i >= 0 && j >= 0) {
        if(arr1[i]>=arr2[j]){
            arr1[k] = arr1[i];
            i--;
        }else{
            arr1[k] = arr2[j];
            j--;
        }
        k--;
    }

    while (i >= 0) {
        arr1[k--] = arr1[i--];
    }
    while (j >= 0) {
        arr1[k--] = arr2[j--];
    }

    return arr1;
}

arr1 = [1,2,3,0,0,0];
arr2 = [2,5,6];
console.log(mergeArrays(arr1,3, arr2,3))