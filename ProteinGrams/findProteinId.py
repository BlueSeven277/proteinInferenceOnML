# find exactly what the 89 proteins are

#f = open('sigmaProteins.txt')
f = open('trueProtein.txt')
#g = open('sigma49/identification.tsv')
#h = open('identifiedProtein.txt','w')
g = open('SortedProtList4Isoform.txt')
fd = open('real48.txt','w')
list = []

for line in f:
    l = line.strip().split(" ")
    list.append(l[0])
i = 0
leng = len(list)

for line in g:
    i = i + 1
    a = line.strip().split(" ")
    for j in range(leng):
        if list[j] in a:
            fd.write(str(i) + "\n")
fd.close()




# for j in range(leng):
#     #print leng
#     k = list[j]
#     for line in g:
#         i = i + 1
#         a = line.strip().split(" ")
#         if k in a:
#             fd.write(str(i)+"\n")
#         else:continue
#     j = j+1
# fd.close()
#
# list = []
# table = {}
# for line in g:
#     l = line.strip().split("\t")
#     a, pid, c = l[1].split("|")
#     if (table.has_key(pid)):
#         table[pid] = table[pid]+1
#     else:
#         table[pid] = 1
#         list.append(pid)
#         print pid
# i = 0
# leng = len(list)
# for i in range(leng):
#     h.write(str(list[i])+" "+str(table[list[i]]) + "\n")
# h.close()