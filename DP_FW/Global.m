data = 'movielens_10m_top400'; %�����ļ���
path = strcat('C:\Users\ChenKx\Desktop\DP_FW\data\',data,'.mat');
load(path);  
addpath(genpath('C:\Users\ChenKx\Desktop\DP_FW\'));
addpath(genpath('C:\Users\ChenKx\Desktop\DP_FW\'));
D = input;   %��ȡ�����ļ�
[m,n] = size(D); %����data�����ļ���ľ����С
%fprintf('data has been loaded: m = %d, n = %d; \n', m,n);
%for i=[1:m]
%    EMEAN=sum(D(i,:));
%    D(i,:)=D(i,:)-EMEAN;
%end
    
%��ʼ��global��������Ĳ���
%rho = .75;  %������
%Omega = rand(m,n)<=rho;
%disp(size(D));
% ii=2;
%epsilon = 2*log(1/delta);
[row, col, val] = find(data);
idx = randperm(length(val));

val = val - mean(val);
val = val/std(val);

traIdx = idx(1:floor(length(val)*0.5));
tstIdx = idx(ceil(length(val)*0.5): end);

clear idx;

traData = sparse(row(traIdx), col(traIdx), val(traIdx));
traData(size(data,1), size(data,2)) = 0;

para.test.row  = row(tstIdx);
para.test.col  = col(tstIdx);
para.test.data = val(tstIdx);
ii=1
for epsilon=[0.1,1.0,2.0,5.0]
    delta = 10^(-6);
    T = 20;
    L = maxl2norm(traData);

    beta = 10;
    k = 30000;
  
    Y=zeros(m,n);

    p=zeros(1,T);

    sigma = (L^2*sqrt(32*T*log(1/delta)))/epsilon;
    v = zeros(1,n);
    lamda = 0;
    Yi = zeros(1,n);

    for t=1:T
    W = zeros(n,n);
    lamda1 = lamda + sqrt(sigma*log(n/beta))*n^(1/4);
    for i = 1:m
        [Yi,AN] = Local_Update(i,v,lamda1,T,t,L,D,k,Yi) ;
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
    
    ii=ii+1;
    disp(rmse(D,Y));
end

plot(epsilon,p);
