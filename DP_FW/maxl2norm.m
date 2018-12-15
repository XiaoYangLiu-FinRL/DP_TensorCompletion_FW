function L=maxl2norm(D)

[m,~]=size(D);

max = 0;
for i=1:m
    buf=norm(D(i,:));
    if max<buf
        max = buf;
    end
end

L=max;