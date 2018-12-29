import numpy as np
import math
import scipy.io as scio
import numpy as np
import io
import matplotlib.pyplot as plt
import random
def Synthetic():
   # u=np.zeros((500000,1),np.dtype='float16')
    u = np.random.random((5000, 1))
    v = np.random.random((40, 1))
    YYY = np.dot(u, np.transpose(v))
    return YYY


def rmse(target,prediction):
    error = []
    (m,n)=np.shape(target)
    for i in range(m):
        for j in range(n):
            error.append(target[i][j] - prediction[i][j])



    squaredError = []
    absError = []
    for val in error:
        squaredError.append(val * val)
        absError.append(abs(val))
    #print len(squaredError)

    rm=np.sqrt(sum(squaredError) / len(squaredError))
   # print sum(squaredError)
    return np.sqrt(sum(squaredError) / len(squaredError))


def Omegamatrix(Xx,samplenum):

    (m,n)=np.shape(Xx)
    X=np.zeros((m,n))
    for i in range(m):
        loc=np.random.randint(0,n,size=samplenum)
        for j in loc:
            X[i][j]=1
    Result=X*Xx
    return Result


def processU(mmatrixU,saveU):
    documentU=[]
    for line in mmatrixU:
        linenew=line[:saveU]
        documentU.append(linenew)
    return documentU

def processV(mmatrixV,saveV):
    documentV=mmatrixV[:saveV]
    return documentV







datainput1=Synthetic()
#datainput2=dataprocess(datainput1)
#L = maxnorm(datainput)
#L=math.pow(n,1.0/4)
T = 4
#belta = 1
datainput=Omegamatrix(datainput1,7)
#L = maxnorm(datainput)
k = np.linalg.matrix_rank(datainput1)
#print L
#k=30000
#(m, n) = np.shape(data['input'])
(m,n)=np.shape(datainput1)
Yt=np.zeros((m,n))
for i in range(T):
    wt = Yt - datainput
    U,S,V = np.linalg.svd(wt)

  #
    uu=processU(U,1)
    vv=processV(V,1)
    #print vv
    st = np.dot(uu,vv)
  #  st=np.dot(uu,vv)

    Yt = (1-1.0/T)*Yt-float(k)/T*st

print(rmse(Yt,datainput1))