function findlongest(word) {
  let result = "";
  let maxlength = "";
//   word = word.toLowerCase()
  for (let i of word) { // aabbcc
    if (!result.includes(i)) {
      result += i;
      if (result.length > maxlength.length || !maxlength) {
        maxlength = result;
      }
    } else {
      result = i;
    }
  }
  console.log(maxlength, maxlength.length);
}

findlongest("xycabdefxyg");
findlongest("bbbbbb");
findlongest("pwwkew");
findlongest("");
findlongest("a");
findlongest("abcdefg");


