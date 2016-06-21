f = open('table1.csv', 'r', encoding = 'utf-8')
f1 = open('finaltable.csv', 'w', encoding = 'utf-8')
decades = {}
for line in f.readlines():
    l = line.split(';')
    try:
        c = int(l[5])
        dec = ((int(l[5]) % 100) // 10)*10
        if dec in decades:
            decades[dec] +=int(l[22])
        else:
            decades[dec] = int(l[22])
        if decades[dec] <= 15000000:
            f1.write(line)
        else:
            continue
    except:
        continue
f1.close()
f.close()
