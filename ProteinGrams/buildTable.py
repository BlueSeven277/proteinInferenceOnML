
__author__ = 'srx'
# calculate neighbours
f = open('cooccurrence.txt')
j = 0
table ={}
for line in f:
    key, value = line.strip().split('\t')
    if (table.has_key(key)==False):
        valuesList = {value:1}
        table[key] = valuesList
    elif (table[key].has_key(value)):
        valuesList = table[key]
        valuesList[value]=valuesList[value]+1
        table[key]=valuesList
    else:
        valuesList = table[key]
        valuesList[value]=1

g=open('cooccurTable.txt','w')
for key in table:
    g.write(key+':'+ str(table[key])+'\n')
    j = j+1
g.close()
print j