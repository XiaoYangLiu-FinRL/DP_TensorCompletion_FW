import csv
import math
import scipy.io as scio
import numpy as np
import pandas as pd
import xlrd
import io
import matplotlib.pyplot as plt
import random
#n_samples, n_features = 500000, 400
#Y=np.zeros((n_samples, n_features))
def Synthetic(n_sample,n_feature):
   # u=np.zeros((500000,1),np.dtype='float16')
    u = np.random.random((n_sample, 1))
    v = np.random.random((n_feature, 1))
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
        loc=np.random.randint(n,size=samplenum)
       # print loc
        for j in loc:
            X[i][j]=1
    Result=X*Xx
    return X,Result

def maxnorm(YY):
    (m,n)=np.shape(YY)

    maxx=0
    for i in range(m):
        temp=np.linalg.norm(YY[i,:],ord=2)
        if maxx<temp:
            maxx=temp
    return math.sqrt(maxx)

def update(Ome,n,k,v,lambda1,T,t,L,Yi,Di):
    YA = np.zeros((1,n))
    Ai = np.zeros(n)
    AN=np.zeros((n,n))
    if t==0:
        Yiii=np.zeros(n)
    else:
        Yiii=Yi
       # Yiii.append(Yi)
    #print
    Ai=(Yiii-Di)*Ome
    #
    #print Ai
    #vi=[]
    #vi.append(v)
    Aii=[]
    Aii.append(Ai)
    #print 'v',v
    ui=(1.0/lambda1)*np.dot(Aii,v)
    #print 'ui:',ui
   # for jj in range(len(ui)):
    #    ui[jj]=float(ui[jj])
   # print 'v',v
   # uii=[]
    #uii.append(ui)
    #vi=[]
    #vi.append(v)
   # print np.shape(uii)
    #print np.shape(vi)
    #if t!=0:
    #    print 'yiii',Yiii
    Yite=(1.0-1.0/T)*Yiii-(float(k)/T)*ui*np.transpose(v)
    #print 'yite;', Yite
    if np.linalg.norm(Yite*Ome,ord=2)!=0:
        if L/np.linalg.norm(Yite*Ome,ord=2)<1 :
            YA=(L/np.linalg.norm(Yite*Ome,ord=2))*Yite
        else:
            YA=Yite
    Ai=(YA-Di)*Ome
   # print 'Ai:',Ai
    #Aii = []
    #Aii.append(Ai)i
    if t!=0:
       # Aii = []
       # Aii.append(Ai)
        #print Aii
        AN=np.dot(np.transpose(Aii),Aii)
    else:
        AN = np.dot(np.transpose(Ai), Ai)
   # print 'An:',AN.shape
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
    rm=np.sqrt(sum(squaredError) / (m*n))
   # print sum(squaredError)
    return rm

#-------parameters
delta=math.pow(10,-6)
eplison=[0.1,1.0,2.0,5.0]
#_sample=5000
#n_feature=40
T = 5
belta = 10
rate=0.2
#------------------------


#---------------inputenexlix---
csv_file=csv.reader(open("C:\Users\ChenKx\Desktop\DPFW\data\etflix_top_400_result.csv",'r'))
#table=csv_file.reader()
data=[]
for i in csv_file:
    #print type(i)
    i=np.array(i)
    #print i[1:len(i)-1]
    data.append(pd.to_numeric(i[1:len(i)-1]))
datainput1=np.array(data)
#datainput1=(np.array(data))
(n_sample,n_feature)=datainput1.shape
samplenumber=rate*n_feature
Xomega,datainput=Omegamatrix(datainput1,int(samplenumber))
#nrows=table.nrows
#ncols=table.ncols
#print nrows,ncols
#data=[]
#for i in range(0,nrows):
#    tabletemp=table.row_values(i)
 #   for jj in range(len(tabletemp)):
 #      # print int(tabletemp[jj])
 #       if int(tabletemp[jj])==99:
 #           tabletemp[jj]=0
  #  data.append(tabletemp)
#data=np.array(data)
#datainput1=(data)
#(n_sample,n_feature)=datainput1.shape
#samplenumber=rate*n_feature
#Xomega,datainput=Omegamatrix(datainput1,int(samplenumber))

#----------inputdate-----
#dataFile = 'data/movielens_10m_top400.mat'
#data = scio.loadmat(dataFile)
#datainput2=data['input']
#datainput1=(datainput2)
#(n_sample,n_feature)=datainput1.shape
#datainput1=Synthetic(n_sample,n_feature)
#samplenumber=rate*n_feature

#Xomega,datainput=Omegamatrix(datainput1,int(samplenumber))
#L =float(maxnorm(datainput))
#print L
#du,ds,dv=np.linalg.svd(datainput1)
#k=sum(ds)
#
#print k
(m,n)=np.shape(datainput)
di=[]
#print 'datainput:',datainput
#print datainput1
#-----------inputdata2---

#-----------------readexcledata---------


#book=xlrd.open_workbook("C:\Users\ChenKx\Desktop\DPFW\data\jester1_rating_data_treated.xlsx")
#table=book.sheet_by_index(0)
#nrows=table.nrows
#ncols=table.ncols
#print nrows,ncols
#data=[]
#for i in range(0,nrows):
#    tabletemp=table.row_values(i)
 #   for jj in range(len(tabletemp)):
 #      # print int(tabletemp[jj])
 #       if int(tabletemp[jj])==99:
 #           tabletemp[jj]=0
  #  data.append(tabletemp)
#data=np.array(data)
#datainput1=(data)
#(n_sample,n_feature)=datainput1.shape
#samplenumber=rate*n_feature
#Xomega,datainput=Omegamatrix(datainput1,int(samplenumber))
(m,n)=np.shape(datainput)
k=200
L =float(maxnorm(datainput))
#-----------------------------------------

#------------------------------glocal-----
for eplisoni in eplison:
    sigma=np.power(L,2)*np.sqrt(T*np.log10(1/delta))/(eplisoni)
    #print '2:',sigma
    #print '1:',np.power(L,2)
    v=np.zeros((n,1))
    lamda=0
    Y=np.zeros((m,n))
    for t in range(T):
        #print t
        #print Y
        W=np.zeros((n,n))
        #for ii in range(len(lamda)):
        lambda1=lamda+math.sqrt(sigma*np.log10(float(n)/belta))*math.pow(n,1.0/4)
       # print '3:',math.sqrt(sigma*np.log10(float(n)/belta))*math.pow(n,1.0/4)
        for i in range(m):
            Di=datainput[i,:]
            Xomegai=Xomega[i,:]
            #if t!=0:
               # print 'yi:', Y[i,:]
            Yii,AN=update(Xomegai,n,k,v,lambda1,T,t,L,Y[i,:],Di)
            Y[i,:]=Yii
            #print 'Yii:',Yii
            #print AN.shape
           # print AN.shape
            for ii in range(n):
                for jj in range(n):
                    W[ii][jj]=W[ii][jj]+AN[ii][jj]
       # print 'An:',W
        #or i in ra
       # print 'AN'
        #print 'W',W
        for it in range(n):
            for jt in range(n):
                W[it][jt]=W[it][jt]+ np.random.normal(0,np.power(sigma,2))
                #print np.random.normal(0,np.power(sigma,1))
        print 'W:',W
        lamdasqrt, vv = np.linalg.eig(W)
        #print 'vv:',vv
        lamdamax=list(lamdasqrt).index(max(lamdasqrt))
        lamda=np.sqrt(lamdasqrt[lamdamax])
        #print 'lamdamx:',lamdasqrt[lamdamax]
        v=np.real(vv[:,lamdamax])
    #print 'Y:',Y
    di.append(rmse(Y*Xomega,datainput))
    print di
#plt.plot(eplison, di, '-r^');
#plt.xlabel('Epsilon');
#plt.ylabel('RMSE');
#plt.grid(color='black',linewidth='0.3',linestyle='--')
#plt.show()








