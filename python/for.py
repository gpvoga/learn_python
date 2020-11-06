n = int(input('Número a testar: '))
for i in range(2,n):
    if(n % i == 0):
        print(' numero não é primo. Divisor =', i);break
    elif(i==n-1):
        print('numero é primo', n) 
    
