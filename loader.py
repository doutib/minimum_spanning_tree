import numpy as np
import heapq as h

def load_data_2(name):
    G=load_data(name)
    n=G.shape[0]
    L=[]
    N=[]
    for i in range(n):
        N.append([])
    for i in range(n):
        for j in range(n):
            if G.item((i,j))>0 and G.item((i,j))<np.inf:
                L.append((G.item((i,j)),i,j))
                N[i].append(j)
                N[j].append(i)
            else:
                G.itemset((i,j),np.inf)
    h.heapify(L)
    Gp=symetrize(G,n)
    return G,L,Gp,N,n


def load_data(name):
    f=open(name,'r')
    l=[]
    l=[line.split(' ') for line in f]
    del(l[0])
    del(l[len(l)-1])
    L=[parse(line) for line in l]
    G=np.array(L)
    n=G.shape[0]
    for i in range(n):
        for j in range(n):
            if G.item((i,j))==0:
                G.itemset((i,j),np.inf)
    return G

def parse(l):
    e=[]
    for i in range(len(l)-1):
        e.append(float(l[i]))
    w=l[len(l)-1]
    e.append(float(w[0:len(w)-1]))
    return e

def symetrize(G,n):
    Gp=np.array(G)
    for i in range(n):
        for j in range(i+1,n):
            Gp.itemset((i,j),Gp.item(j,i))
    return Gp
