const convert = (array) => {
  const numRows = array.length;
  const numCol = array[0].length;
  const result = new Array([numCol][numRows]);
  for (let col = 0; col < numCol; col++) {
    result[col] = [];
    for (let row = 0; row < numRows; row++) {
      console.log(array[row][col]);
      result[col][row] = array[row][col];
    }
  }
  return result;
};

const res = convert([
  [1, 2, 3],
  [4, 5, 6],
]);

console.log(res);
