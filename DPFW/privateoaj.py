import io
import numpy
import scipy.io as scio
import math

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

ataFile = 'data/movielens.mat'
data = scio.loadmat(dataFile)
datainput=data['input']
k = 2 * np.linalg.matrix_rank(datainput)
eplison=[0.1,1.0,2.0,5.0]
delta=math.pow(10,(-6))

L = maxnorm(datainput)
T = 20
belta = 10
(m, n) = np.shape(data['input'])

for eplisoni in eplison:
    namda=0.2
    sigma=math.pow(L,2)*math.sqrt(256*T*np.log10(2/delta))/eplisoni
    v0=np.zeros(n)
    v0=v0+np.random.normal(0, sigma)
    fot t in range(T):
        if t==0:
            vt=v0
        else:
            namta=1/(T*sigma*math.sqrt(n))
            gt=np.zeros((n,n))
            gt=gt+np.random.normal(0, sigma)
            vtt=vt+namta*(np.dot(np.dot(np.transpose(A),A)),vt)+gt)
            vtt=vtt/np.linalg.norm(vtt,ord=2)

    print vtt
    lamda=math.pow(np.linalg.norm(np.dot(A,vtt),ord=2),2)+np.random.normal(0, sigma)
    print lamda
        
                 
