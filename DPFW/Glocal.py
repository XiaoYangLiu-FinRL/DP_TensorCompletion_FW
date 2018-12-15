
import math
import scipy.io as scio
import numpy as np
import io
import matplotlib.pyplot as plt

def Omega(X):
    for i in range(len(X)):
        if X[i]>0 and X[i]!=None:
            X[i]=X[i]
        else:
            X[i]=0
    return X


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

def update(n,i,k,v,lambda1,T,t,L,Yi,Di):
    if t==0:
        Yi=np.zeros(n)
        Ai=np.zeros(n)
    else:
        Ai=Omega(Yi-Di)
    #print np.shape(v)
    ui=np.multiply(Ai,v)*[1/lambda1]
    Yitemp=Yi*[(1-1/T)],-ui*np.transpose(v)*[k/T]
    YA= np.zeros(n)
   # print(Yitemp)
   # print(Omega(Yitemp))
    #print(L/np.linalg.norm(Omega(Yitemp),ord=2))
    if np.linalg.norm(Omega(Yitem),ord=2)!=0:
        if L/np.linalg.norm(Omega(Yitemp),ord=2)<1 :
            YA=Yitemp*[L/np.linalg.norm(Omega(Yitemp),ord=2)]
        else:
            YA=Yitemp
    Ai=Omega(YA-Yi)

    AN=np.transpose(Ai)*Ai
    return YA,AN


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

def rmsee(target,prediction):
    error = []
    (m,n)=np.shape(target)
    for i in range(m):
        error.append(target[i,:] - prediction[i,:])



    squaredError = []
    absError = []
    for val in error:
        squaredError.append(val * val)
        absError.append(abs(val))
    #print len(squaredError)
    rm=np.sqrt(sum(squaredError) / len(squaredError))
   # print sum(squaredError)
    return min(np.sqrt(sum(squaredError) / len(squaredError)))




dataFile = 'data/movielens.mat'
data = scio.loadmat(dataFile)
datainput=data['input']
delta=math.pow(10,-6)
eplison=[0.1,0.5,1.0,2.0,5.0]

L = maxnorm(datainput)
T = 20
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

    #print(math.log(1/delta))
    sigma=math.pow(L,2)*math.sqrt(32*T*np.log10(1/delta))/eplisoni
    v=np.zeros(n)
    lamda=0
    Y=np.zeros((m,n))
    W1=np.zeros((n,n))
    Yi=np.zeros(n)
    Yitem=np.zeros(n)
    #print(n)
    for t in range(T):
        W=np.zeros((n,n))
        lambda1=int(lamda)+int(math.sqrt(sigma*math.log(n/belta))*math.pow(n,1/4))
        for i in range(m):
            Di=datainput[i]
            [YYi,AN]=update(n,i,k,v,lambda1,T,t,L,Yi,Di)
            Yi=YYi
            Y[i,:]=YYi
            W=W+AN
        #print(np.size(W))
        for i in range(n):
            for j in range(n):
                W1[i][j] =W[i][j]+ np.random.normal(0, sigma)

        lamdasqrt, vv = np.linalg.eig(W1)
   # print(np.real(math.fabs(sorted(lamdasqrt)[1])))
        lamda=math.sqrt(int(np.real(math.fabs(sorted(lamdasqrt)[1]))))
    #print lamda
        v=vv[:,1]

    di.append(rmsee(Y,datainput))
    print di
plt.plot(epsilon, di, '-r^', 'MarkerEdgeColor','b','MarkerFaceColor','b', 'MarkerSize', 10);
plt.xlabel('Epsilon');
plt.ylabel('RMSE');
plt.grid(color='black',linewidth='0.3',linestyle='--')
plt.show()








