
__author__ = 'srx'
#final size:1032879
#id,key-value  can solve problem of order!!!!

nSize = 3
gramTable = {}
i = 0
#f = open('3grams.txt', 'w')
fd = open('2gramsFiltered.txt', 'w')
for line in open("FilteredProtein.txt"):
    i = i+1
    l = line.strip().split(' ')
    leng = len(l)
    if leng <3:
        continue
    for j in range(0,leng-1):
        # problem: cannot use a set as a key
        key = str(l[j])+' '+str(l[j+1])
        if(gramTable.has_key(key)==False):
            sequenceNumList = [i]
            gramTable[key]=sequenceNumList
        else:
            sequenceNumList = gramTable[key]
            sequenceNumList.append(i)
            gramTable[key]=sequenceNumList

print i
j = 0
#g=open('cooccurTable.txt','w')
for key in gramTable:
    fd.write(key+':'+ str(gramTable[key])+'\n')
    j = j+1
fd.close()
print j



