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



factor_dims = 50;
factor_dims = [factor_dims, factor_dims, 50];
core_dims   = [20, 20, 20];
    
% Problem setting
U = cell(1, length(core_dims));
for i = 1:length(core_dims)
    U{i} = randn(factor_dims(i), core_dims(i));
    % [U{i}, ~] = qr(U{i}, 0);
end
C = randn(core_dims);

% Generate low-rank tensor
gnd = ttensor(tensor(C), U);

gnd = double(gnd);
gnd = gnd - mean(gnd(:));

X = gnd + randn(size(gnd))*mean(abs(gnd(:)))*0.05;

ratio = 5*prod(core_dims)/sqrt(prod(factor_dims));
O = rand(size(X));
idx = find(O < ratio);

M = zeros(size(O));
M(idx) = 1;

clear O idx;

traX = cell(size(M, 3), 1);
for i = 1:size(M, 3)
    traX{i} = sparse(X(:,:,i).*M(:,:,i));
end
%disp(X);
%disp(cell2mat(traX(1)));


D = 20;

T =400;
%for timet=1:6
    
   % delta = 10^(-(timet));
     delta = 10^(-6);
    epsilon = log(1/delta)/2;
  %   epsilon = timet;
   % q(1,timet)=epsilon;
    [n,k]=size(cell2mat(traX(1)));
    m=20;
    beta = 10^(-2);disp(epsilon);

    Y=zeros(n,k);
    max = 0;
    B=10;
    %print(opts(2));
    for i=1:m
        tempp=cell2mat(traX(i));

        buf=normest(tempp);
        if max<buf
           max = buf;
        end
    end

    L=max;
  

    decay = 0.8;
    Xnew=zeros(n,k,m);
    Xold=zeros(n,k,m);
    A=zeros(n,k,m);
    sigma=(2*B*sqrt(log(1/delta)))/epsilon/sqrt(T);
    %ssi=sqrt(8*sigma^2*((m+n+k)*log(2*D/log(3/2))+log(2/delta)))/1000
    disp(sigma);
    for mmm=1:m
        Xold(:,:,mmm)=cell2mat(traX(mmm));
        A(:,:,mmm)=cell2mat(traX(mmm));
    end


    AA=fft(A,[],3);
     Z=zeros(n,k,m);
    for t=1:T

       Z=fft(Z,[],3);

        for j=1:m
            if t==1


                lamda=0.2;
              %  disp(AA(:,:,j))
                [Xi,YYi]=localpart(lamda/L,t,L,AA(:,:,j),sigma,m,n,k,beta,D,AA(:,:,j));
                Z(:,:,j)=Xi;
            else
                lamda=2*10^(-5);

                %disp(Z)
                Yi=Z(:,:,j);
                [Xi,YYi]=localpart(lamda/L,t,L,Yi,sigma,m,n,k,beta,D,AA(:,:,j));
                Z(:,:,j)=Xi;

          % Z=Z+normrnd(0,sigma^2);
        end
    end
        Z=ifft(Z,[],3);
        Z=Z+normrnd(0,sigma^2);
         p(1,t)=rmse(Z,A);






    % clear Xold;
     %  Xold=Xnew;
      %  clear Xnew;
     
    end
   %  p(1,timet)=rmse(Z,A);
%end

    q=[1:T];
    plot(q,p);
    %
    %disp(Xnew)
     
       

     
       
        