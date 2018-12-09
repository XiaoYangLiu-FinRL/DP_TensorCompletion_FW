
function [Xi,YYi]=localpart(lamda,t,L,Yi,sigma,m,n,k,delta,D,A)


told=t;
Xold=Yi;
%disp(Yi);%for i=1:k

[Ulocal,Slocal,Vlocal]=SVT_t(Xold,lamda,sigma,m,n,k,D,delta);

Xnew=Ulocal*Slocal*Vlocal';
%disp(Xnew);
tnew=(1+sqrt(1+4*told))/2;
R=Xnew+((told-1)/tnew)*(Xnew-Xold);
disp(size(R));
Xi=R-1/L*(R-A);
disp(size(Xi));
YYi=Xnew;


end