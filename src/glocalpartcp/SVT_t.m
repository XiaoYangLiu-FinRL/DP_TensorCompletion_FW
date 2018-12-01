function [U, S, V] = SVT_t(Z, lambda,sigma,m,n,k,D,beta)

[U, S, V] = svd(Z, 'econ');

S = diag(S);
S = max(S-lambda, 0);
S = S(1:nnz(S));

U = U(:,1:length(S));
V = V(:,1:length(S));
S = diag(S);
%disp(sqrt(8*sigma^2*((m+n+k)*log(2*D/log(3/2))+log(2/beta)))/100 )

end





