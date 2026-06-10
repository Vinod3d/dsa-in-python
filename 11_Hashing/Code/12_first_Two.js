function first_Two(s) {
    // for(let i =1; i<s.length; i++){
    //     if(s[i-1] == s[i]){
    //         return s[i]
    //     }
    // }

    let set = new Set();
    for(let i = 0; i < s.length; i++){
        if(set.has(s[i])){
            return s[i]
        }
        set.add(s[i])
    }
};

const s = "abccbaacz";
console.log(first_Two(s));
