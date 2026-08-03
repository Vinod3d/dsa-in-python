function wordPattern(pattern, s) {
  let hmap = new Map();
  let s1 = s.split(" ");

  if (pattern.length !== s1.length) {
    return false;
  }

  for (let i = 0; i < pattern.length; i++) {
    let char = pattern[i];
    let word = s1[i];

    if (!hmap.has(char)) {
      if (Array.from(hmap.values()).includes(word)) {
        return false;
      }
      hmap.set(char, word);
    } else if (hmap.get(char) !== word) {
      return false;
    }
  }
  return true;
}

console.log(wordPattern("abbc", "dog cat cat fish"));
