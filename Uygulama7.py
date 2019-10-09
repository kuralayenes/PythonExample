print("Girilen pozitif bir tamsayının,iki sayının kareleri toplamı şeklinde \n yazılıp yazılmayacağını veren program !")

sayi1 = int(input("Bir sayi giriniz: "))

for i in range(1,sayi1,1):
    for j in range (1,sayi1,1):
        topla = i**2+j**2
        if(sayi1 == topla):
            print(i,j,sayi1)

