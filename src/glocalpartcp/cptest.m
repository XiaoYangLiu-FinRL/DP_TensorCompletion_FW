X = sptenrand([2 2 2], 6); 
disp(X);
P = parafac_als(X,2);
B1=(P.U{1}(:,1) * P.U{2}(:,1)');
B2=(P.U{1}(:,2) * P.U{2}(:,2)');
C=P.U{3}(:,1);
C1=P.U{3}(:,2);
XS=P.lambda(1)*B1*C(1)+P.lambda(2)*B2*C1(1);
disp(XS);
%[U,S,V]=svd(double(X(:,:,1)))
A=[[1,2,3];[4,5,6];[1,4,7]];
B=[[1,1,2];[2,3,1];[1,2,3]];
C=[[0,1,1];[2,2,5];[0,2,4]];
[U,S,V]=svd(A);
[U1,S1,V1]=svd(B);
[U2,S2,V2]=svd(C);
disp(U1*U2')
disp(U1-U2)

%B1=reshape(kron(P.U{1}(:,1) * P.U{2}(:,1)', P.U{3}(:,1)), [length(P.U{1}(:,1)), length(P.U{2}(:,1)), length(P.U{3}(:,1))]);
%B2=reshape(kron(P.U{1}(:,2) * P.U{2}(:,2)', P.U{3}(:,2)), [length(P.U{1}(:,2)), length(P.U{2}(:,2)), length(P.U{3}(:,2))]);
%B1=outerProduct(P.U{1}(:,1),P.U{2}(:,1),P.U{3}(:,1));
%B2=outerProduct(P.U{1}(:,2),P.U{2}(:,2),P.U{3}(:,2));
%C1=outerProduct(B1,P.U{3}(:,1));
%C2=outerProduct(B2,P.U{3}(:,1));
%[xx, yy, zz] = ndgrid(1:length(P.U{1}(:,1)), 1:length(P.U{2}(:,1)), 1:length( P.U{3}(:,1)));
% desired outerproduct
%M1 =( P.U{1}(:,1)(xx)) .* P.U{2}(:,1)(yy) .* P.U{3}(:,1)(zz);

%[xx1, yy1, zz1] = ndgrid(1:length(P.U{1}(:,1)), 1:length(P.U{2}(:,1)), 1:length( P.U{3}(:,1)));
% desired outerproduct
%M2 = P.U{1}(:,2)(xx1) .* P.U{2}(:,2)(yy1) .* P.U{3}(:,2)(zz1);

%XS=P.lambda(1)*B1*C(2)+P.lambda(2)*B2*C1(2);
%disp(XS);

%TT=[[1,2,3,2];[4,5,6,3];[7,8,9,2]]
%[Q,R]=qr(TT)
%TT1=[[1,2];[4,5];[7,8]]
%TT2=[[3,2];[6,3];[9,2]]
%[QR,RR]=svd(TT2)
%v1=[1,2,3,2];
%B2=2*v1' * v1;



