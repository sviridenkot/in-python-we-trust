def translit(str):
    f = open('amhar.tsv', 'r', encoding = 'utf-8')
    cons = []
    vow = []
    amhar = {}
    c = 0
    for l in f.readlines():
        v = 0
        line = l.split()
        for char in line:
            if c == 0 and v != 0:
                vow.append(char)
            if c != 0 and v == 0:
                cons.append(char)
            if c != 0 and v != 0:
                amhar[char] = cons[c-1] + vow[v-2]                
            v += 1
        c += 1
    f.close()
    newstring = []
    for ch in str:
        newstring.append(amhar.setdefault(ch, ch))
    return ''.join(newstring)

f = open('amhartxt.txt', 'r', encoding = 'utf-8')
amhar = f.read()
f.close()
f = open('amhartrans.txt', 'w', encoding='utf-8')
for c in amhar:
    f.write(translit(c))
f.close()
