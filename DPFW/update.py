import numpy as np
import io
from scipy import sparse

def update(n,i,k,v,lambda1,T,t,L,Yi,Di):
    if t==0:
        Yi=np.zeros(n)
        Ai=np.zeros(n)
    else:
        Ai=Omega(Yi-Di)
    ui=(Ai*v)/lambda1
    Yitemp=np.dot((1-1/T),Yi)-np.dot(k/T,ui*np.transpose(v))
    if L/np.linalg.norm(Omega(Yitemp),ord=2)<1:
        YA=np.dot(L/np.linalg.norm(Omega(Yitemp),ord=2),Yitemp).
    else:
        YA=Yitemp
    Ai=Omega(YA-Yi)
    AN=np.transpose(Ai)*Ai
    return YA,AN