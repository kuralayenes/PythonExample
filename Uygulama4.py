print("ax+b=0 şeklindeki birinci dereceden denklemin kökünü hesaplayınız ?")

sayi1 = int(input("a değişkenini giriniz : "))
sayi2=  int(input("b değişkenini giriniz : "))

if(sayi1==0 and sayi2==0):
    print("Her sayi köktür")
elif(sayi2==0):
    print("Kök yoktur")
else:
    x = -sayi2/sayi1
    print("Kök =",x)