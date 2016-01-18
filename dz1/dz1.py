def translit(mystr):
    conversion = {
        'ა' : 'ɑ',
        'ბ' : 'b',
        'გ' : 'g',
        'დ' : 'd',
        'ე' : 'ɛ',
        'ვ' : 'v',
        'ზ' : 'z',
        'ჱ' : 'ɛj',
        'თ' : 'tʰ',
        'ი' : 'ɪ',
        'კ' : 'kʼ',
        'ლ' : 'l',
        'მ' : 'm',
        'ნ' : 'n',
        'ჲ' : 'j',
        'ო' : 'ɔ',
        'პ' : 'pʼ',
        'ჟ' : 'ʒ',
        'რ' : 'r',
        'ს' : 's',
        'ტ' : 'tʼ',
        'ჳ' : 'wi',
        'უ' : 'u',
        'ფ' : 'pʰ',
        'ქ' : 'kʰ',
        'ღ' : 'ɣ',
        'ყ' : 'qʼ',
        'შ' : 'ʃ',
        'ჩ' : 'tʃ',
        'ც' : 'ts',
        'ძ' : 'dz',
        'წ' : 'tsʼ',
        'ჭ' : 'tʃʼ',
        'ხ' : 'x',
        'ჴ' : 'q',
        'ჯ' : 'dʒ',
        'ჰ' : 'h',
        'ჵ' : 'hɔɛ'
            }
    newstr = ''
    for c in mystr:
        newstr+=(conversion.setdefault(c, c))
    return newstr

f = open('gruz.txt', mode = 'r', encoding = 'utf-8')
gruz = f.read()
f.close()
f = open('ipa.txt', 'w', encoding='utf-8')
for c in gruz:
    f.write(translit(c))
f.close()
