print("armstrong sayilari")

for i in range(1,9,1):
    for j in range(0,9,1):
        for k in range (0,9,1):
            sayi1 = 100 * i + 10 * j + k
            sayi2 = i*i*i + j*j*j +  k*k*k
            if(sayi1 == sayi2):
                 print(100*i+10*j+k)