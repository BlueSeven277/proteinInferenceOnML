f = open('RealMascotData_89_All.txt')
g = open('real770peptides.txt')
fd = open('real770.txt','w')
list = []

for line in f:
    l = line.strip().split(" ")
    list.append(l[0])
i = 0
leng = len(list)

for line in g:
    i = i + 1
    a,b,c,d,e,f = line.strip().split(" ")
    for j in range(leng):
        if list[j] == f:
            fd.write(str(e) + "\n")
fd.close()