print("Tüm kenarları tam sayı ve dik kenarları 1-50 (1<= a,b <= 50) \n arasında mümkün olan bütün a-b-c Pisagor üçgenlerini veren Program")

for i in range(1,50,1):
    for j in range(1,50,1):
        c = (i**2+j**2)**(1/2)
        if  c.is_integer() == True:
            print(i,j,int(c))
