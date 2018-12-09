
function [Xi,YYi]=localpart(lamda,t,Yi,Ui,Si,Vi,sigma,m,n,delta,D,A)




%disp(Yi);%for i=1:k


   
if Si-lamda>0
    Si=Si-lamda;
   
else
    Ui=zeros(1,400);
  
%disp(size(Ui)); 


Xnew=Si*Ui*Vi';
disp(size(Xnew));
told=t;
tnew=(1+sqrt(1+4*told))/2;
Xold=Yi;
R=Xnew+((told-1)/tnew)*(Xnew-Xold);

Xi=R-1/L*(R-A);

YYi=Xnew;


end