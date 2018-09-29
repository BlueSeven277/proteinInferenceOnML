import cmath

__author__ = 'srx'

i = 0
window_size = 3  # window_size=real_window_size/2
f = open('cooccurrence.txt', 'w')
for line in open("SortedProtUniqueKeyListIsoformGroup.txt"):
    i = i + 1
    l = line.strip().split(' ')
    leng = len(l)
    # if (i<10):
    for index in range(leng):
        left = max(0, index - window_size + 1)
        right = min(leng, index + window_size)
        for neighbour in range(left, right):
            if (index != neighbour):
               # print '%s\t%s' % (l[index], l[neighbour])
                f.write('%s\t%s\n' % (l[index], l[neighbour]))
f.close()

# print leng
