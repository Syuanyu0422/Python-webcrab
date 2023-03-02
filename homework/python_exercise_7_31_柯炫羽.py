import csv
infn='input.csv'
outfn='output.csv'

with open(infn,'r',encoding='UTF-8') as infile:
    inreader=csv.reader(infile)
    listinput=list(inreader)

with open(outfn,'w',newline='',encoding='ANSI') as outfile:
    outwriter=csv.writer(outfile,delimiter='\t')
    for row in listinput:
        outwriter.writerow(row)
    outwriter.writerow('----------')
    for row in listinput:
        outwriter.writerow(row)
    outwriter.writerow(['花茶',15])
    outwriter.writerow(['蜜茶',10])