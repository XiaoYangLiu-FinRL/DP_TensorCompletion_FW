import io
import numpy as np
import scipy.io as scio
import math


def Omegamatrix(Xx):
    (m,n)=np.shape(Xx)
    X=np.zeros((m,n))
    for i in range(m):
        for j in range(n):
            if  Xx[i][j]!=None:
                X[i][j]=Xx[i][j]
            else:
                X[i][j]=0
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


def maxnorm(YY):
    (m,n)=np.shape(YY);

    maxx=0
    for i in range(m):
        temp=np.linalg.norm(YY[i,:],ord=2)
        if maxx<temp:
            maxx=temp
    return maxx

def getZ(tu,S):
    (nn,)=np.shape(S)
    Z=np.zeros((nn, nn))
    stemp=0
    for i in range(int(nn)):
        for j in range(nn):
            if i==j and S[i]>tu:
                Z[i][j]=S[i]-tu
            else:
                Z[i][j]=0
    return Z
           
        

dataFile = 'data/movielens.mat'
data = scio.loadmat(dataFile)
datainput=data['input']
k = 2 * np.linalg.matrix_rank(datainput)
#print k
eplison=[0.1,1.0,2.0,5.0]
delta=math.pow(10,(-6))

L = maxnorm(datainput)

print L
T = 20
belta = 10
(m, n) = np.shape(data['input'])
DI=[]
#print datainput
for eplisoni in eplison:
    namda=0.005
    sigma=math.pow(L,2)*math.sqrt(64*T*np.log10(1/delta))/eplisoni
    Yinital=np.zeros((m,n))
    Ytt=np.zeros((m,n))
    for t in range(T):
        if t==0:
            Yt=Yinital
        else:
                
            Yt=(1/(1+namda))*(Yt-namda*Omegamatrix(datainput))
            #print Yt
            Wt=np.dot(np.transpose(Yt),Yt)+ np.random.normal(0, sigma)
            lamdasqrt, vv = np.linalg.eig(Wt)

            lamda=np.sqrt(np.real(np.abs(lamdasqrt)))
            #print Wt
           # print np.diag(lamda)
            lamdainves=[]
            for lamdai in lamda:
                if lamdai!=0:
                   lamdainves.append(1/lamdai)
                else:
                    lamdainves.append(0)
            u=np.dot(np.dot(Yt, vv),np.diag(lamdainves))
           # print sum(lamda)
            tua=(sum(lamda)-k)/n
            #print tua

            if sum(lamda)>k:
                Z=getZ(tua, lamda)
            else:
                Z=np.diag(lamda)
            print Z
            Yt=np.dot(np.dot(u,Z),np.transpose(vv))
       # print Yt
    DI.append(rmse(Yt,datainput))
    print DI
            
            
        

        
    
