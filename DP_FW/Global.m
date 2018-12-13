data = 'movielens'; %数据文件名
path = strcat('C:\Users\ChenKx\Desktop\DP_FW\data\',data,'.mat');
load(path);  
addpath(genpath('C:\Users\ChenKx\Desktop\DP_FW\'));
addpath(genpath('C:\Users\ChenKx\Desktop\DP_FW\'));
D = input;   %读取数据文件
[m,n] = size(D); %返回data数据文件里的矩阵大小
%fprintf('data has been loaded: m = %d, n = %d; \n', m,n);

%初始化global部分所需的参数
%rho = .75;  %采样率
%Omega = rand(m,n)<=rho;
%disp(size(D));
 ii=2
%epsilon = 2*log(1/delta);
for epsilon=[0.1,1.0,2.0,5.0]
    delta = 10^(-6);
    T = 20;
    L = maxl2norm(D,Omega);

    beta = 10;
    k = 2*rank(D);
  
    Y=zeros(m,n);

    p=zeros(1,T);

    sigma = (L^2*sqrt(64*T*log(1/delta)))/epsilon;
    v = zeros(1,n);
    lamda = 0;
    Yi = zeros(1,n);

    for t=1:T
    W = zeros(n,n);
    lamda1 = lamda + sqrt(sigma*log(n/beta))*n^(1/4);
    for i = 1:m
        [Yi,AN] = Local_Update(i,v,lamda1,T,t,L,D,k,Omega,Yi) ;
      %  display(Yi);
        Y(i,:)=Yi;
        W = W + AN;
    end
    W1 = W + normrnd(0,sigma^2);
    [V, S] = eig(W1);
    lambda = wrev(diag(S));
    V = fliplr(V);
    v=(V(:,1))';
    lamda=sqrt(lambda(1,:));
    
    
    end
    p(1,ii)=rmse(D,Y);
    q(1,ii)=epsilon;
    ii=ii+1;
    disp(rmse(D,Y));
end

plot(p,q);
