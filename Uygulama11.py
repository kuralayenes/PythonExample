rs = input("Romen rakamlarıyla sayıyı giriniz: ")

k1 = 0

sy = 0
print("\n")

for i in range(0,len(rs),1):
        k2 = k1
        deger = rs[i]

        if (deger == 'I'):
            k1 = 1

        elif (deger == 'V'):
            k1 = 5

        elif (deger == 'X'):
            k1 = 10
        elif (deger == 'L'):
            k1 = 50
        elif (deger == 'C'):
            k1 = 100
        elif (deger == 'D'):
            k1 = 500
        elif (deger == 'M'):
            k1 = 1000

        if (k1 > k2):
            k3 = -2 * k2
        else:
            k3 = 0
        sy = sy + k1 + k3

print("sayi = ", sy)
