import random
import linecache
import datetime
#a = random.randint(0,10000)
#f = open("SortedProtUniqueKeyListIsoformGroup.txt")
g = open('random10.txt','w')
h = open('random10pips.txt','w')

l = []
peptide = []
####### sampe 10 proteins and cut them into peptides########
for i in range(0,100):
    a =random.randint(0,10000)
    protein = linecache.getline("SortedProtUniqueKeyListIsoformGroup.txt",a)
    newpip = protein.strip().split(' ')
    peptide.extend(newpip)
    l.append(protein)
    #h.write(str(newpip))
    g.write(str(a)+":"+protein)
g.close()

h.write(str(peptide))
h.close()

####### filter peptides for some cannot be detected ########
####### candidate size can be 100+ times larger if there is no filter ########
print "Number of peptides before filtering:"+str(len(peptide))
np = len(peptide)
filtered = []
for j in range(0, np):
    if 167936< int(peptide[j]) < 669412 and peptide[j]not in filtered:
        filtered.append(peptide[j])

print "Number of peptides after filtering:"+str(len(filtered))



####### search for candidate proteins ########
i=0
num =0 # total hits
pnum=0 # number of returned proteins
k = open('random10result.txt','w')
k.write("The total number of piptie is "+str(len(filtered))+"\n")
print datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
flag = False
candidate = [] #Candidate number can be >10
final = {} # must be 10
for line in open("FilteredProtein.txt"):
    sigleHit = 0  #number of hit in one single protein
    i = i + 1
    li = line.strip().split(' ')
    for j in range(len(filtered)):
        if filtered[j] in li:
            flag = True
            k.write("protein "+ str(i) +" contains:" +str(filtered[j])+ "\n")
            num = num+1
            sigleHit = sigleHit+1
    if flag==True: # if hit
        pnum = pnum+1
        candidate.append(i)
        flag = False
    # if sigleHit==1:
    #     final.append(i)

k.write("Total hit: "+str(num))
k.close()
print "Total hit: "+str(num)
print datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print "Number of protein candidates: "+str(pnum)
# print "Final result must contain:"
# print final


###### improve #########
print "----- improve2.0 ------"
#70% of the searched peptides appears only once
for i in range(len(filtered)):
    j = 0
    for pipHit in range(len(candidate)):
        protein = linecache.getline("FilteredProtein.txt", int(candidate[pipHit])) # get that candidate protein
        lnew = protein.strip().split(' ')
        if filtered[i] in lnew:
            contain = candidate[pipHit] #protein number
            j = j+1
            continue
    if j ==1 and final.has_key(contain)==False:
        final[contain] = filtered[i]
        # peptide[filtered[i]] appeared only once in protein[contain] in all candidates
print len(final)
print "Final result must contain:"
print final
