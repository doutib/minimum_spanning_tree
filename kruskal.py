import numpy as np
import time
import heapq as h

def kruskal(C,n):
    R=np.zeros([n,n])
    D={}
    for i in range(n):
        D[i]=i
    c=0
    while c<n-1:
        p=D[C[0][1]]
        ch=D[C[0][2]]
        while not p==D[p]:
            p=D[p]
        while not ch==D[ch]:
            ch=D[ch]
        if p==ch:
            h.heappop(C)
        else:
            e=h.heappop(C)
            R.itemset((e[1],e[2]),e[0])
            D[ch]=p
            c=c+1
    return R

def print_kruskal(C,n,adresse):
    R=np.zeros([n,n])
    D={}
    for i in range(n):
        D[i]=i
    c=0
    f=open("kruskal_"+adresse+".txt",'w')
    f.write(str(0)+'\n')
    for a in range(n):
        for b in range(n):
            f.write(str(int(R.item((a,b))))+' ')
        f.write('\n')
    k=0
    while c<n-1:
        p=D[C[0][1]]
        ch=D[C[0][2]]
        while not p==D[p]:
            p=D[p]
        while not ch==D[ch]:
            ch=D[ch]
        if p==ch:
            h.heappop(C)
        else:
            e=h.heappop(C)
            R.itemset((e[1],e[2]),e[0])
            D[ch]=p
            c=c+1
            k=k+1
            f.write(str(k)+'\n')
            for a in range(n):
                for b in range(n):
                    f.write(str(int(R.item((a,b))))+' ')
                f.write('\n')
    f.close()
    return R
