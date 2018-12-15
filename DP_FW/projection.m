function r=projection(D,L)

[m,n]=size(D);

max = 0;
for i=1:m
    buf=norm(D(i,:));
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
