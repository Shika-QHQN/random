uses crt; 
var D,a,b,c,x1,x2:real;
begin
    clrscr;
write('Nhap a:');readln(a);
 write('Nhap b:');readln(b);
  write('Nhap c:');readln(c);

D:=b*b-4*a*c;
if D > 0 then
begin
    x1:=(-b+sqrt(D))/(2*a);
    x2:=(-b+sqrt(D))/(2*a);
    write('Hai nghiem cua phuong trinh la',x1:8:3,x2:8:3);
end;    

if D = 0 then
begin
        x1:=-b/(2*a);
        write('Hai nghiem cua phuong trinh la',x1:8:3);
end;

if D < 0 then write('Phuong trinh vo nghiem');

readln;
end.
