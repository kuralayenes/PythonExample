print("Mükemmel Sayı")

x = int(input("Mükemmel sayi tahmininizi giriniz: "))

total = 0

for i in range(1,x,1):
    if(x%i==0):
        total += i          # total = total + i


if(x == total):
    print("Mükemmel Sayi")
else:
    print("Mükemmel Sayi değildir.")





