function flipHorizontalMatrix(image) {
    let row = image.length;
    let col = image[0].length;

    for (let i = 0; i < row; i++) {

        for (let j = 0; j < Math.ceil(col / 2); j++) {

            let temp = image[i][j];

            image[i][j] = image[i][col - 1 - j] ^ 1;
            image[i][col - 1 - j] = temp ^ 1;
        }
    }

    return image;
}

console.log(
    flipHorizontalMatrix([
        [1,1,0],
        [1,0,1],
        [0,0,0]
    ])
);