import re
file = open ('caraid.html', 'r', encoding = 'utf-8')
text=file.read()
file.close()
l = (re.search('\<h3.*\>.+\</h3\>', text, re.DOTALL))
lemma = l.group()
lemma = re.sub('\<[^>]*\>', '', lemma)
lemma = re.sub('\s', '', lemma)
lemma = lemma.replace('\\n','')
f = (re.search('Forms:.+\</p\>\</div\>', text, re.DOTALL))
frm = f.group()
frm = re.sub('\</p\>\</div\>', '', frm)
frm = re.sub('\\s','', frm)
frm = re.sub('Forms:', '', frm)
forms = frm.split(',')
file = open('irishdict.txt', 'w', encoding = 'utf-8')
mydict = {}
for form in forms:
    mydict[form] = lemma
    file.write(form + ': ' + mydict[form] + '\n')
file.close()
