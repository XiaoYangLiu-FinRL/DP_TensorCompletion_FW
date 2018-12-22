# How to

## Step 1. run startup.m

## Step 2. run demo/link_predict_demo.m

## Step 3. Change route in startup.m

The main DP iteration process file is src/acctenfw.m

目前直接加入的一个给定的eplision，具体加入在afftenfw.m文件中

```
delta = 10^(-8);
epsilon = 2*log(1/delta);
sigma = 2*(L*sqrt(T*log(1/delta)))/epsilon;

newcomp =   (spmultic(Pi{j}, Pj{j}, u, v')+normrnd(0,sigma^2))*tau * fac_size(j); 
```

## Step 4. noise is added in the newcomp at the 154 line of acctenfw.m file.

Newcomer is used to iteration step. 

## Step 5. At the same time, it will change the eigenvalue at 167 line of acctenfw.m.

```
lambda_new = (1+sqrt(1+4*lambda_old^2))/2+sqrt(8*sigma^2*(cumsum(Asize)*log(2*D/log(3/2))+log(2/delta)));
```

> 注意: matrix completion 里面是不含DP的矩阵还原算法
