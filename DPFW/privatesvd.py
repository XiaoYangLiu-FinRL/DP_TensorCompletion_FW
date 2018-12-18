import io
import numpy as np
import scipy.io as scio
import math
import pyunlocbox

def Omegamatrix(Xx):
    (m,n)=np.shape(Xx)
    for i in range(m):
        for j in range(n):
            if Xx[i][j]>0 and Xx[i][j]!=None:
                Xx[i][j]=Xx[i][j]
            else:
                Xx[i][j]=0
    return Xx[i][j]

def maxnorm(YY):
    (m,n)=np.shape(YY);

    maxx=0
    for i in range(m):
        temp=np.linalg.norm(YY[i,:],ord=2)
        if maxx<temp:
            maxx=temp
    return maxx

def Omega(X):
    for i in range(len(X)):
        if X[i]>0 and X[i]!=None:
            X[i]=X[i]
        else:
            X[i]=0
    return X


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


dataFile = 'data/movielens.mat'
data = scio.loadmat(dataFile)
datainput=data['input']
delta=math.pow(10,-6)
eplison=[0.1,0.5,1.0,5.0]

L = maxnorm(datainput)
belta = 10


k = 2 * np.linalg.matrix_rank(data)
k=400
(m, n) = np.shape(data['input'])
di=[]

#for iii in range(m):
   # sunm=sum(datainput[iii,:])/len(datainput[iii,:])
 #   datainput[iii, :]=datainput[iii,:]-sunm

for eplisoni in eplison:

#eplisoni=0.1
    Y=np.zeros((m,n))
    W=np.zeros((n,n))
    #print(math.log(1/delta))
    sigma=math.pow(L,2)*math.sqrt(64*np.log10(1/delta))/eplisoni
    for i in range(m):
      # print datainput[i, :]
       f = pyunlocbox.functions.proj_b2()
       ff=f.prox(datainput[i,:],)
       print ff
       wi=np.dot(np.transpose(ff),ff)
       W=W+wi
    W=W+np.random.normal(0, sigma)

    W1=np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            W1[i][j] =W[i][j]+ np.random.normal(0, sigma)

    lamdasqrt, vv = np.linalg.eig(W1)
    for i in range(m):
        Yi=np.dot(np.dot(Omega(datainput[i,:]),vv),np.transpose(vv))
        Y[i,:]=Yi
    print Y
    di.append(rmse(Y,datainput))
    print di
               

    
                                        
        
