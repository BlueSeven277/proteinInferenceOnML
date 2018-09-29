from __future__ import division
import linecache
import datetime
import csv

pepAdd=[675358,399396,14682]
fd = open('realSigmaPep.txt')
peptide = []
for line in fd:
    l = line.strip()
    peptide.append(l)
print "Number of peptides before filtering:"+str(len(peptide))
np = len(peptide)
filtered = []
for j in range(0, np):
    if 167936< int(peptide[j]) < 669412 and peptide[j]not in filtered:
        filtered.append(peptide[j])

print "Number of peptides after filtering:"+str(len(filtered))

k = open('realSigmaResult.txt','w')
k.write("The total number of piptie is "+str(len(filtered))+"\n")
print datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
flag = False
candidate = [] #Candidate number can be > number of sample proteins
final = {} # must be
final2 = {}
unique_pip = []

i = 0
num =0 # total hits
pnum=0 # number of returned proteins
filtered.append("675358")
filtered.append("399396")
filtered.append("14682")
print "filtered:"+ str(len(filtered))
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
table ={}# key:peptideID  value:appear in which protein
for i in range(len(filtered)):
    j = 0
    #m = 0 # the number of unique peptides contained by a protein
    for pipHit in range(len(candidate)):
        protein = linecache.getline("FilteredProtein.txt", int(candidate[pipHit])) # get that candidate protein
        lnew = protein.strip().split(' ')
        if filtered[i] in lnew:
            contain = candidate[pipHit] #protein number
            j = j+1
            continue
    if j ==1 :
        unique_pip.append(filtered[i])
        if table.has_key(contain):
            table[contain] = table[contain]+1
            if table[contain]>2 and (final2.has_key(contain) ==False):
                final2[contain]=table[contain] # has at least two unique peptides

        else:
            table[contain] = 1
        if final.has_key(contain)==False:
            final[contain] = filtered[i]
        # peptide[filtered[i]] appeared only once in protein[contain] in all candidates
print len(final)
print "Final result must contain:"
print final

print "----- improve3.0 ------3 unique peptides:"


print len(final2)
print final2

ret_list = [item for item in candidate if item not in final2.keys()]
print "number of candidates after remove ones with 3 unique:"+str(len(ret_list))
print "unique Peptides:"+str(len(unique_pip))
unUnique = [item for item in filtered if item not in unique_pip]

#calcullate the frequency
frequency ={}
for item in filtered :
    j = 0
    frequency[item] = j
    for i in range(len(ret_list)):
        a = ret_list[i]
        protein = linecache.getline("FilteredProtein.txt", a)
        retPepList = protein.strip().split(' ')
        if item in retPepList:
            j = j+1
    frequency[item] = j
print "frequency of occurance of filtered peptides:"
print frequency

####### calculate percentage of similarity ########
itsPeps={}
fl = open('ret_sigma_list.txt','w')
# generate features
for i in range(len(candidate)):
    a = candidate[i]
    protein = linecache.getline("FilteredProtein.txt",a)
    retPepList = protein.strip().split(' ')
    pl = len(retPepList)
    j = 0
    hislist =[]
    for item in retPepList:
        if item in filtered :
            j = j+1
            hislist.append(item)
        # elif item in unique_pip:
        #     j = j+1
        #     hislist.append(item)
    three = 0
    two = 0
    more_than_eight = 0
    other =0
    one =0
    for item in hislist:

        if frequency[item]==2:
            two = two +1
        elif frequency[item]==3:
            three = three+1
        elif frequency[item]>8:
            more_than_eight = more_than_eight+1
        elif frequency[item]==1:
            one = one+1
        else:other = other+1
    fl.write(str(a)+" "+str(pl)+ " "+ str(j) +" " +str(j/pl*100) + " "+ str(one)+ " "+ str(two)+ " "+ str(three) +  " "+ str(other) +" "+ str(more_than_eight) + "\n")
fl.close()

#st = open('ret_sorted.txt','w')
top_size = 47-26
ret ={}
for line in open('ret_sigma_list.txt'):
    pID, length, number, percentage, one,two, three, other, moreThanEight= line.strip().split(' ')
    ret[int(pID)] = float(percentage)
print "Candidates sorted by percentage of similarity:"
print sorted(ret.items(),key = lambda x:x[1],reverse = True)

real =[]
for line in open('real48.txt'): #actually 47 proteins in total
    text = int(line.strip())
    real.append(text)
need_to_find = [item for item in real if item not in final2.keys()]
print "Proteins that need to be find are:" + str(len(need_to_find))
print need_to_find
tmp = [val for val in final2 if val in real]
print "intersection of [realProteins] and [final]"+str(len(tmp))
print tmp
fake =[val for val in real if val not in candidate ]
wrong = [val for val in final2 if val not in real]
print "wrong:"
print wrong
print "in [real] but not in [candidate](cannot be retrived through peptide hit):"+ str(len(fake))
print fake
print "The highest accuracy is 37/47=78.7%. or 37/43=86%"