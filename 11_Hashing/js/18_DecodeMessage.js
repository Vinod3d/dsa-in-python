function decodeMessage(mapping, message) {
    let result = "";
    
    for (let ch of message) {

            if (mapping[ch] !== undefined) {
                result += mapping[ch];
            } else {
                result += ch;
            }
        }
        
        return result;
}



const mapping = {
    'a': 'y',
    'b': 'h',
    'c': 'e',
    'd': 'n',
    'e': 'g',
    'f': 'j',
    'g': 'q',
    'h': 'n',
    'i': 'a',
    'j': 'd',
    'k': 'r',
    'l': 'o',
    'm': 'w',
    'n': 'z',
    'o': 'x',
    'p': 'i',
    'q': 'b',
    'r': 'c',
    's': 'k',
    't': 'u',
    'u': 'v',
    'v': 't',
    'w': 's',
    'x': 'l',
    'y': 'p',
    'z': 'm'
};

const message = "ysq v q z nz";
console.log(decodeMessage(mapping, message));