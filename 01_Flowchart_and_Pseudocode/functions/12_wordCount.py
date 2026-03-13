def wordCount(txt):
    WC = {}
    for word in txt.split():
        if word in WC:
            WC[word] = WC[word] + 1
        else:
            WC[word] = 1
    return WC

text = "Python is very easy to learn Python"

print(wordCount(text))