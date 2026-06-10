
var checkIfPangram = function(sentence) {
    let set = new Set();
    for(let i=0; i<sentence.length;i++){
        let ch = sentence.charAt(i);
        set.add(ch);
    }
    return set.size == 26;
};