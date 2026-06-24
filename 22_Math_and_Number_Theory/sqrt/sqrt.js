function sqrt(num) {
  if (num === 0) return 0;
  if (num === 1) return 1;
  let i = 1;
  while (i * i <= num) {
    if (i * i === num) {
      return i;
    }
    i++;
  }
  return i - 1;
}

console.log(sqrt(8));


var mySqrt = function(x) {
    if (x === 0) return 0;

    let first = 1, last = x, ans = 0;

    while (first <= last) {
        let mid = Math.floor((first + last) / 2);
        if (mid <= Math.floor(x / mid)) {
            ans = mid;        
            first = mid + 1;
        } else {
            last = mid - 1;
        }
    }

    return ans;
};


console.log(mySqrt(17)); 
console.log(mySqrt(4));  
console.log(mySqrt(0));  