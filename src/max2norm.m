function L=maxl2norm(D,Omega)

[m,~]=size(D);
DD= Omega.*D;
max = 0;
for i=1:m
    buf=norm(DD(i,:,:));
    if max<buf
        max = buf;
    end
end

L=max;
