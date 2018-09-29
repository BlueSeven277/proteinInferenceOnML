f = open('sigma49/identification.tsv')
g = open('real770peptides.txt')
fd = open('realSigmaPep.txt','w')
listP = []
database = []
realPep =[]

for line in f:
    l = line.strip().split("\t")
    listP.append(l[0])
i = 0

pep = list(set(listP))
leng = len(pep)
numOfCut = 0
for line in g:
    i = i + 1
   # print i
    a,b,c,d,e,f = line.strip().split(" ")
    #database.append(f)
    for j in range(leng):
        find = False
        if pep[j] == f:
            realPep.append(e)
            find =True
        else:
            # cut sequences with K or R
            sequence = pep[j]
            k_index = sequence.find('K')
            r_index = sequence.find('R')
            if len(sequence)-2>k_index>0:
                subPre = sequence[0:k_index+1]
                subBeh = sequence[k_index+1:]
                if subPre ==f or subBeh==f:
                    #fd.write(str(e) + "\n")
                    realPep.append(e)
                    numOfCut = numOfCut+1
                    find = True
                    break
            elif len(sequence)-2>r_index>0:
                subPre = sequence[0:r_index + 1]
                subBeh = sequence[r_index+1:]
                if subPre == f or subBeh == f:
                    realPep.append(e)
                    find = True
                    numOfCut = numOfCut + 1
                    break
        if find==False and (len(sequence)-2>k_index>0 or len(sequence)-2>r_index>0): # if cut once -no match , cut twice
            sequence = pep[j]
            secondCut = 0
            secondR =0
            for i in range(len(sequence)-2):
                if sequence[i]=='K' and sequence[i+1]!='P':
                    secondCut =i
                if sequence[i]=='R' and sequence[i+1]!='P':
                    secondR =i
            if sequence[0:secondCut+1] == f or sequence[secondCut+1:]==f:
                realPep.append(e)
                find =True
                break
            elif sequence[0:secondR+1] == f or sequence[secondR+1:]==f:
                realPep.append(e)
                find =True

s = set(realPep)
print numOfCut
for b in s:
    fd.write(str(b) + "\n")


fd.close()