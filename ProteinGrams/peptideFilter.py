f = open('FilteredProtein.txt', 'w')
i = 0
for line in open("SortedProtUniqueKeyListIsoformGroup.txt"):
    i = i+1
    l = line.strip().split(' ')
    leng = len(l)
    for j in range(0,leng):
        if 167936< int(l[j]) < 669412 :
            f.write(l[j]+ " ")
    f.write("\n")
f.close()