def create_line(list):
    line = ''
    for l in list:
        line = line + str(l) + ';'
    return line


f = open('table.csv', 'r', encoding = 'utf-8')
f1 = open('table1.csv', 'w', encoding = 'utf-8')
for line in f.readlines():
    l = line.split(';')
    if l[22] == 'words\n':
        f1.write(line)
        continue
    try:
        w = int(l[22])
        y = int(l[5])
        s = str(l[6])
        if w <= 70000:
            f1.write(line)
        elif w <= 100000:
            l1 = l
            l2 = l
            l1[22] = w // 2
            f1.write(create_line(l1)+'\n')
            l2[22] = w - l1[22]
            f1.write(create_line(l2)+'\n')
        else:
            l1 = l
            l2 = l
            l3 = l
            l1[22] = w // 3
            f1.write(create_line(l1)+'\n')
            l2[22] = w // 3
            f1.write(create_line(l2)+'\n')
            l3[22] = w - l1[22] - l2[22]
            f1.write(create_line(l3)+'\n')
    except:
        continue
f.close()
f1.close()

