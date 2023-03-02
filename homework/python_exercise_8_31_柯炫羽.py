import xml.etree.ElementTree as et
tree=et.parse('FarmTransData.xml')
root=tree.getroot()

i=0

for col in root[i]:
    if i<5:
        i+=1
        print('<',root[i].tag,'>',sep='')  
        for col in root[i].findall('Col3'):
            print('\t<',col.attrib['name'],'>',col.text,sep='')
        for col in root[i].findall('Col4'):
            print('\t<',col.attrib['name'],'>',col.text,sep='')
        for col in root[i].findall('Col10'):
            print('\t<',col.attrib['name'],'>',col.text,sep='')
        for col in root[i].findall('Col11'):
            print('\t<',col.attrib['name'],'>',col.text,sep='')
        print('</',root[i].tag,'>',sep='')   

import csv
with open('write.csv','w',encoding='ANSI') as f:
    fwriter=csv.writer(f)

    title=[]
    title.append(root[0][2].attrib['name'])
    title.append(root[0][3].attrib['name'])
    title.append(root[0][9].attrib['name'])
    title.append(root[0][10].attrib['name'])

    fwriter.writerow(title)


    for i in range(len(root)):
        no=root[i][2].text
        name=root[i][3].text
        price=root[i][9].text
        amount=root[i][10].text
        fwriter.writerow([no,name,price,amount])

