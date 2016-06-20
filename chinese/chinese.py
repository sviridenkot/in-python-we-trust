import re
import string
from lxml import etree
from bs4 import BeautifulSoup

def create_dict(file):
    f = open(file, 'r', encoding = 'utf-8')
    d = {}
    for line in f:
        line = line.strip()
        if line[0] == '#':
            continue
        else:
            l = line.split('/')
            word = l[0]
            transcr = re.search('\[(.*?)\]', word)
            sem = re.search ('\]\s/(.+)', line)
            word = word[:word.index('[')]
            w = word.split()
            new = w[1]
            transcr = transcr.group(1)
            sem = sem.group(1)
            d1 = {}
            d1['transcr'] = transcr
            d1['sem'] = sem
            d[new] = d1
    f.close()
    return(d)

def delete_punct(file):
    punct = string.punctuation
    f = open(file, 'r', encoding = 'utf-8') 
    soup = BeautifulSoup(f, "lxml")
    sent = soup.find_all("se")  
    sentences = []
    for s in sent:
        sentences.append(s.get_text().strip(punct))
    f.close()
    return(sentences)

def create_xml(d, sents):    
    punct = string.punctuation
    l = []  
    html = etree.Element("html")
    head = etree.SubElement(html, "head")
    body = etree.SubElement(html, "body")
    for sent in sents:
        sent = sent.strip(punct)
        se = etree.SubElement(body, "se")
        maxlen = len(sent)
        while maxlen > 0:
            cur = sent[0:maxlen]
            if cur in d:
                l.append((cur, d[cur]))
                w = etree.SubElement(se, "w")
                ana = etree.SubElement(w, "ana", lex = cur, transcr = d[cur]['transcr'], sem = d[cur]['sem'])
                ana.tail = cur
                sent = sent[maxlen:]
                maxlen = len(sent)
                continue
            else:
                maxlen -= 1
    with open("stal_processed.xml", "w", encoding = "utf-8") as f:
        f.write(etree.tostring(html, encoding = "utf-8", xml_declaration = True, pretty_print = True).decode("utf-8"))
        

chinaDict = create_dict('cedict_ts.u8')
sent = delete_punct('stal.xml')
create_xml(chinaDict, sent)

