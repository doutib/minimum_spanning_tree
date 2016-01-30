from prim import prim,print_prim
from kruskal import kruskal,print_kruskal
from loader import *
import time
import numpy as np

def run(do_print):
    tk=0
    tp=0
    for i in range(100):
        G,C,Gp,N,n=load_data_2('testing_graph_'+str(i)+'.txt')
        start=time.time()
        if do_print:
            print_kruskal(C,n,str(i))
        else:
            kruskal(C,n)
        tk=tk+time.time()-start
        n=G.shape[0]
        start=time.time()
        if do_print:
            print_prim(Gp,N,n,str(i))
        else:
            prim(Gp,N,n)
        tp=tp+time.time()-start
    tp=tp/100.0
    tk=tk/100.0
    print tp
    print tk
    f=open('runtime.txt','w')
    f.write('Prim: '+str(tp)+' seconds\nKruskal: '+str(tk)+' seconds')
    f.close()
    return

run(False)



