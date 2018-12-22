
import math
import scipy.io as scio
import numpy as np
import io
import matplotlib.pyplot as plt
import random
def Synthetic():
   # u=np.zeros((500000,1),np.dtype='float16')
    u = np.random.random((500000, 1))
    v = np.random.random((400, 1))
    YYY = np.dot(u, np.transpose(v))
    return YYY

def Omega(X):
    for i in range(len(X)):
        if  X[i]!=None:
            X[i]=X[i]
        else:
            X[i]=0
    return X

def dataprocess(X):
    (m, n) = np.shape(X)
    for i in range(m):
        mean=sum(X[i,:])/len(X[i:,])
        X[i,:]=X[i,:]-mean
    return X

def Omegamatrix(Xx,samplenum):
    (m,n)=np.shape(Xx)
    X=np.zeros((m,n))
    # = np.zeros(n)
    for i in range(m):
        loc=np.random.randint(0,n,size=samplenum)
        for j in loc:
            X[i][j]=1
    Result=X*Xx
    return Result

def maxnorm(YY):
    (m,n)=np.shape(YY);

    maxx=0
    for i in range(m):
        temp=np.linalg.norm(YY[i,:],ord=2)
        if maxx<temp:
            maxx=temp
    return math.sqrt(maxx)

def update(n,k,v,lambda1,T,t,L,Yi,Di):
    YA = np.zeros(n)
    AN=np.zeros((n,n))
    if t==0:
        Yiii=np.zeros(n)
    else:
        Yiii=Yi
        #print Yii
    #print Y
    Ai=Omega(Yiii-Di)
    #print Ai
    ui=(1.0/lambda1)*np.multiply(Ai,v)
    #print np.dot(ui,np.transpose(v))
    Yite=(1.0-1.0/T)*Yiii-float(k)/T*np.dot(ui,np.transpose(v))
    #print np.linalg.norm(Yite,ord=2)
    if np.linalg.norm(Yite,ord=2)!=0:
       # print L/np.linalg.norm(Yitemp,ord=2)
        if L/np.linalg.norm(Yite,ord=2)<1 :
            YA=L/np.linalg.norm(Yite,ord=2)*Yitemp
        else:
            YA=Yite
        #print YA
    #print YA.shape
    Ai=YA-Di
    AN=np.dot(np.transpose(Ai),Ai)
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




# dataFile = 'data/movielens_10m_top400.mat'
# data = scio.loadmat(dataFile)
# datainput1=data['input']
delta=math.pow(10,-6)
eplison=[0.1,1.0,2.0,5.0]
datainput1=Synthetic()
#datainput2=dataprocess(datainput1)
#L = maxnorm(datainput)
#L=math.pow(n,1.0/4)
T = 5
belta = 1
datainput=Omegamatrix(datainput1,80)
L = maxnorm(datainput)
k = np.linalg.matrix_rank(datainput1)
#print L
#k=30000
#(m, n) = np.shape(data['input'])
(m,n)=np.shape(datainput1)
di=[]
#print datainput
for eplisoni in eplison:
    sigma=math.pow(L,2)*math.sqrt(64*T*np.log10(1/delta))/eplisoni
    print sigma
    v=np.zeros(n)
    lamda=0
    Y=np.zeros((m,n))
    for t in range(T):
        W=np.zeros((n,n))
        lambda1=int(lamda)+int(math.sqrt(sigma*math.log(n/belta))*math.pow(n,1.0/4))
        #print lambda1
        for i in range(m):
            Di=datainput[i,:]
            Yii,AN=update(n,k,v,lambda1,T,t,L,Y[i,:],Di)

            Y[i,:]=Yii
            W=W+AN
        W=W+ np.random.normal(0,sigma )
        lamdasqrt, vv = np.linalg.eig(W)
        lamda=math.sqrt(int(np.real(math.fabs(sorted(lamdasqrt)[1]))))
        v=np.transpose(vv[1,:])
    #print Y
    di.append(rmse(Y,datainput1))
    print di
plt.plot(eplison, di, '-r^');
plt.xlabel('Epsilon');
plt.ylabel('RMSE');
plt.grid(color='black',linewidth='0.3',linestyle='--')
plt.show()








