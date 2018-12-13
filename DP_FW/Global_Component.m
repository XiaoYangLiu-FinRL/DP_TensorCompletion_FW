data = 'movielens'; %数据文件名
path = strcat('.\data\',data,'.mat');
load(path);  
D = input;   %读取数据文件
[m,n] = size(D); %返回data数据文件里的矩阵大小
%fprintf('data has been loaded: m = %d, n = %d; \n', m,n);

%初始化global部分所需的参数
rho = .75;  %采样率
Omega = rand(m,n)<=rho;
delta = 10^(-6);

%--------------------------------------------------------------------------
epsilon_list = [0.1, 1.0, 2.0, 5.0];
result = zeros(1,4);
for epsilon_index = 1:4
    epsilon = epsilon_list(epsilon_index);
%--------------------------------------------------------------------------
    % epsilon = 2*log(1/delta);
    % epsilon = 0.1;
    T = 20;
    L = maxl2norm(D,Omega);
    beta = 10^(-2);
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
            Y(i,:)=Yi;
            W = W + AN;
        end
        W = W + normrnd(0,sigma^2);
        
        % V 是 W 的右特征向量(列向量)组成的矩阵
        % S 是对角矩阵，对角线是 W 的特征值
        [V, S] = eig(W);
        
        % diag(S) 取 S 的对角线作为列向量返回
        % wrev 是倒置向量   (1,2,3,4) 变成 (4,3,2,1)
        lambda = wrev(diag(S));
        
        % fliplr 是水平翻转矩阵
        %    1 2 3     3 2 1
        %    4 5 6  => 6 5 4
        %    7 8 9     9 8 7
        V = fliplr(V);
        
        v=(V(:,1))';
        lamda=lambda(1,:);
        p(1,t)=rmse(D,Y);
    end
%--------------------------------------------------------------------------
    result(epsilon_index) = p(T);
end
%--------------------------------------------------------------------------

plot(epsilon_list, result, '-r^',...
    'MarkerEdgeColor','b','MarkerFaceColor','b', 'MarkerSize', 10);
xlabel('Epsilon');
ylabel('RMSE');
grid on;
%q=[1:T];
%semilogy(q,p);
