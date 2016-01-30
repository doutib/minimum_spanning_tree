import numpy as np
from heapq import heappush,heappop,heapify
import heapq as h
import time as t


def prim(Gp,N,n):
    R=np.zeros([n,n])
    nodes=range(n)
    Vt=[False for i in range(n)]
    Vt_N=[]
    u=nodes.pop(0)
    Q=[]
    Vt_N.append(u)
    Vt[u]=True
    for v in N[u]:
        heappush(Q,(Gp.item((u,v)),u,v))
    k=1
    while k<n:
        w,u,v=heappop(Q)
        if Vt[v]==False:
            Vt_N.append(v)
            Vt[v]=True
            nodes.remove(v)
            for a in Vt_N:
                for m in N[a]:
                    if not Vt[m]:
                        heappush(Q,(Gp.item((a,m)),a,m))
            R.itemset((u,v),w)
            k=k+1
    return R

def print_prim(Gp,N,n,adresse):
    R=np.zeros([n,n])
    nodes=range(n)
    Vt=[False for i in range(n)]
    Vt_N=[]
    u=nodes.pop(0)
    Q=[]
    Vt_N.append(u)
    Vt[u]=True
    for v in N[u]:
        heappush(Q,(Gp.item((u,v)),u,v))
    f=open('prim_'+adresse+'.txt','w')
    k=1
    while k<n:
        w,u,v=heappop(Q)
        if v in Vt_N:
            continue
        Vt_N.append(v)
        Vt[v]=True
        nodes.remove(v)
        for a in Vt_N:
            for m in N[v]:
                if Vt[m]==False:
                    heappush(Q,(Gp.item((a,m)),a,m))
        if u>v:
            R.itemset((u,v),w)
        else:
             R.itemset((v,u),w)
        f.write(str(k)+'\n')
        for i in range(n):
            for j in range(n):
                f.write(str(int(R.item((i,j))))+' ')
            f.write('\n')
        k=k+1
    return R
        
            


