data = 'movielens'; %�����ļ���
path = strcat('.\data\',data,'.mat');
load(path);  
D = input;   %��ȡ�����ļ�
[m,n] = size(D); %����data�����ļ���ľ����С
%fprintf('data has been loaded: m = %d, n = %d; \n', m,n);

%��ʼ��global��������Ĳ���
rho = .75;  %������
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
        
        % V �� W ������������(������)��ɵľ���
        % S �ǶԽǾ��󣬶Խ����� W ������ֵ
        [V, S] = eig(W);
        
        % diag(S) ȡ S �ĶԽ�����Ϊ����������
        % wrev �ǵ�������   (1,2,3,4) ��� (4,3,2,1)
        lambda = wrev(diag(S));
        
        % fliplr ��ˮƽ��ת����
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
