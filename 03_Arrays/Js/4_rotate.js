function rotate(matrix){
    let rows = matrix.length;
    let cols = matrix[0].length;
    let ans = Array.from({length:cols},()=>Array(rows))

    for(let i = 0; i<rows; i++){
        for(let j = 0; j<cols; j++){
            ans[j][rows-1-i] = matrix[i][j]
        }
    }
    
    for(let i = 0; i<rows; i++){
        for(let j = 0; j<cols; j++){
            matrix[i][j] = ans[i][j]
        }
    }
    
}   

console.log(
    rotate([
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ])
);