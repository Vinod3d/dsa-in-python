// 867. Transpose Matrix
function transpose(matrix) {
    const rows = matrix.length;
    const cols = matrix[0].length;

    let transpose = Array.from(
        {length: cols},
        () => Array(rows)
    )

    for(let i = 0; i<rows; i++){
        for(let j = 0; j<cols; j++){
            transpose[j][i] = matrix[i][j]
        }
    }

    return transpose
}


console.log(transpose([[1,2,3],[4,5,6],[7,8,9]]))