def underlineSpliter(s):
    return s.split("_")
    
# YS     WAX    YC
def humpSpliter(s):
    start = 0
    l = []
    for idx, c in enumerate(s):
        if c.isupper():
            l.append(s[start:idx])
            start = idx
    l.append(s[start:])
    return l

def numericSpliter(s):
    start = 0
    l = []
    digitFlag = False
    for idx, c in enumerate(s):
        if c.isdigit():
            if digitFlag == False:
                l.append(s[start:idx])
                start = idx
                digitFlag = True
        else:
            if digitFlag == True:
                l.append(s[start:idx])
                start = idx
                digitFlag = False
    l.append(s[start:])
    return l
    
def mergeCap(l):
    new = []
    cap_word = ""
    for i in range(len(l)):
        if l[i].isupper() and len(l[i]) == 1:
            cap_word += l[i]
        else:
            if cap_word:
                new.append(cap_word)
            new.append(l[i])
            cap_word = ""
    return new


def split(s):
    underlineTokens = underlineSpliter(s)
    humpTokens = []
    numericTokens = []
    for token in underlineTokens:
        humpTokens.extend(humpSpliter(token))
    for token in humpTokens:
        numericTokens.extend(numericSpliter(token))
    l = [i for i in numericTokens if i]
    return mergeCap(l)

if __name__ == "__main__":
    import os#, nltk
    import sys
    path = sys.argv[1]
    f = open(path + "variable_name.txt")
    l = f.read().splitlines()
    f.close()
    name_tokens = {}
    # des_tokens = {}
    for varname in l:
        varname = varname.strip()
    #    vardes = i[1] if len(i)>1 else ""
        name_tokens[varname] = split(varname)
    #    des_tokens[varname] = nltk.word_tokenize(vardes)

    w = open(path + "name_tokens_v2.txt","w")
    for varname in name_tokens:
        w.write(str(varname))
        for name in name_tokens[varname]:
            w.write("\t" + name) 
        w.write("\n")
    w.close()
    #w = open("des_tokens.txt","w")
    #for varname in des_tokens:
    #    w.write(str(varname)+"\t"+str(des_tokens[varname])+"\n")

