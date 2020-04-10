def draw():
    
    for i in range(n):
        for j in range(n):
            print(x[i][j],end = " ")
        print(" \n") 
                 



print("введите диагональ квадрата: ")
n = int(input())
x = [[0]*n for i in range(n)]
print(n,x)
s=0
k=0
s0=0
s1=0
c = [0]*n #массив для суммы строк
d = [0]*n #массив для суммы столбцов

#Ввод массива и проверка суммы 
#главной и побочной диагонали матрицы
print("Введите матрицу: ")
for i in range(n):
    for j in range(n):
        x[i][j]=int(input())
        print(x)
for i in range(n):
    for j in range(n):
        if (i == j):
            s0+=x[i][j]
        elif (i + j == n - 1):
            s1+=x[i][j]

#складываем строки
i = 0
while i < n:
    for j in range(n):
        s+=x[i][j]
    
    c[i]=s
    s=0
    i+=1

s=0
#складываем столбцы
j = 0
while j < n:
    for i in range(n):
        s+=x[i][j]
        
    d[j]=s
    s=0
    j+=1
  
i=0
j=0  
#проверка равности сумм
for i in range(n): 
    if (c[i]==s0) and (c[i]==s1):
        k+=0
    else:
        k+=1

for i in range(n):
    if (d[i]==s0) and (d[i]==s1):
        k+=0
    else:
        k+=1

#вывод


if k==0:
    print("cube is magic")
    print("sum of cube is:",s0)


















        
    





