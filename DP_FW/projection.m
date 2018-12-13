function r=projection(D,L,Omega)

[m,n]=size(D);
DD=omega(D,Omega);
max = 0;
for i=1:m
    buf=norm(DD(i,:));
    if max<buf
        max = buf;
    end
end
a = L/max;
if a>1
    r=D;
else 
    r=A*D;
end
