
function [Xi,YYi]=localpart(lamda,t,L,PA,PB,PC,sigma,m,n,k,delta,D,A)


told=t;
Xold=Yi;
%disp(Yi);%for i=1:k

S = diag(PC);
S = max(S-lambda, 0);
S = S(1:nnz(S));

U = PA(:,1:length(S));
V = PB(:,1:length(S));
S = diag(S);

Xnew=U*S*V';
%disp(Xnew);
tnew=(1+sqrt(1+4*told))/2;
R=Xnew+((told-1)/tnew)*(Xnew-Xold);
Xi=R-1/L*(R-A);
YYi=Xnew;


end