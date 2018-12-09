clear;
clear global
% ndims = [300, 300, 50];
% r = [5, 5, 20];
% nmodes = length(r);
% m=50;
% disp('Generate synthetic data...');
% [data, ~] = synthetic(ndims, r,  'CORE');
% data = sptensor(data);
% err_type = 'AUC';
% density = 0.05;
% 
% [data_train, P_train, data_test_post, P_test, data_mean, data_std] = tensplitspdata(data, density);
% data_test = data .* P_test;

%maxNumCompThreads(1);
data = 'movielens'; %数据文件名
path = strcat('C:\Users\ChenKx\Desktop\DP_FW\data\',data,'.mat');
load(path);  
addpath(genpath('C:\Users\ChenKx\Desktop\DP_FW\'));
addpath(genpath('C:\Users\ChenKx\Desktop\DP_FW\'));
DD = input;   %读取数据文件
[m,n] = size(DD); %返回data数据文件里的矩阵大小
%fprintf('data has been loaded: m = %d, n = %d; \n', m,n);

%初始化global部分所需的参数
rho = .75;  %采样率
Omega = rand(m,n)<=rho;

%disp(cell2mat(traX(1)));


D = 20;

T =50;
for timet=1:20
    
    delta = 10^(-(timet));
    
    epsilon = log(1/delta)/2;
  %   epsilon = timet;
    q(1,timet)=epsilon;
   
    m=20;
    beta = 10^(-2);disp(epsilon);

    Y=zeros(m,n);
    max = 0;
    B=3;
    %print(opts(2));
    for i=1:m
       
       

        buf=norm(DD(i,:));
        if max<buf
           max = buf;
        end
    end

    L=max;


    decay = 0.8;
    Xnew=zeros(m,n);
    Xold=zeros(m,n);
    A=zeros(m,n);
    sigma=(2*B*sqrt(log(1/delta)))/epsilon/sqrt(T);
    %ssi=sqrt(8*sigma^2*((m+n+k)*log(2*D/log(3/2))+log(2/delta)))/1000
    disp(sigma);
    AA=DD;
     Z=zeros(m,n);
    for t=1:T

     Z=fft(Z);

        for j=1:m
            if t==1


                lamda=2*10^(-5);
              %  disp(AA(:,:,j))
                [U,S,V]=svd(AA);
                [Xi,YYi]=localpartcp(lamda,t,AA(j,:),U(j,:),S(j,j),V,sigma,m,n,beta,D,AA(j,:));
                Z(j,:)=Xi;
            else
                lamda=2*10^(-5);

                %disp(Z)
                [U,S,V]=svd(Z);
                Yi=Z(j,:);
                [Xi,YYi]=localpartcp(lamda,t,Yi,U(j,:),S(j,j),V,sigma,m,n,beta,D,AA(j,:));
                Z(j,:)=Xi;

          % Z=Z+normrnd(0,sigma^2);
        end
    end
        Z=ifft(Z);
        Z=Z+normrnd(0,sigma^2);






    % clear Xold;
     %  Xold=Xnew;
      %  clear Xnew;
     
    end
     p(1,timet)=rmse(Z,A);
end

    
    plot(q,p);
    %
    %disp(Xnew)
     
       

     
       
        