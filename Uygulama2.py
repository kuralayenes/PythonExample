sayi = int(input("Bir Sayi Giriniz :"))
liste = []
for i in range (1,sayi+1,1):
    if(sayi%i==0):
        liste.append(i)
print(liste)
