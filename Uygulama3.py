sayi = int(input("Bir Sayi Giriniz: "))

s=0

for i in range(2, sayi-1,1):
    if(sayi%i==0):
        s=s+1
if(s==1):
    print("Asal Sayı")
else:
    print("Asal Sayi Değil")