from __future__ import division
import numpy as np
import logging
import scipy.io as scio
import math

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
    Result=X
    return Result

def svt_solve(A, mask, tau=None, delta=None, epsilon=1e-2, max_iterations=1000):
  """
  Solve using iterative singular value thresholding.

  [ Cai, Candes, and Shen 2010 ]

  Parameters:
  -----------
  A : m x n array
    matrix to complete

  mask : m x n array
    matrix with entries zero (if missing) or one (if present)

  tau : float
    singular value thresholding amount;, default to 5 * (m + n) / 2

  delta : float
    step size per iteration; default to 1.2 times the undersampling ratio

  epsilon : float
    convergence condition on the relative reconstruction error

  max_iterations: int
    hard limit on maximum number of iterations

  Returns:
  --------
  X: m x n array
    completed matrix
  """
  logger = logging.getLogger(__name__)
  Y = np.zeros_like(A)

  if not tau:
    tau = 5 * np.sum(A.shape) / 2
  if not delta:
    delta = 1.2 * np.prod(A.shape) / np.sum(mask)

  for _ in range(max_iterations):

    U, S, V = np.linalg.svd(Y, full_matrices=False)

    S = np.maximum(S - tau, 0)

    X = np.linalg.multi_dot([U, np.diag(S), V])
    Y += delta * mask * (A - X)

    rel_recon_error = np.linalg.norm(mask * (X - A)) / np.linalg.norm(mask * A)
    if _ % 1 == 0:
      logger.info("Iteration: %i; Rel error: %.4f" % (_ + 1, rel_recon_error))
    if rel_recon_error < epsilon:
      break

  return X

#datainput1=Synthetic()
#datainput2=dataprocess(datainput1)
#L = maxnorm(datainput)
#L=math.pow(n,1.0/4)
T = 400
#belta = 1
dataFile = 'data/movielens_10m_top400.mat'
data = scio.loadmat(dataFile)
datainput1=data['input']
datainput=Omegamatrix(datainput1,80)
#datainput=Omegamatrix(datainput1,7)
Yt=svt_solve(datainput1,datainput)
print rmse(Yt,datainput1)