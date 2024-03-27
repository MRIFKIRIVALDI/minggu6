#soal nomor 1 sampai 9 

print("no 1")
for i in range(1,6):
    for j in range(1,6):
        print(i*j,end=' ')
    print( )     

# print("no 2")
# for i in range(1,6):
#     for j in range(6,i,+1):
#         print(' ',end=' ')

#     for k in range(i):
#         print(i+k,end=' ')
#     print( )  

print("no 2")
for i in range(1,6):
    for j in range(i,i+i):
        print(j,end=' ')
    print( )           

print("no 3")
for i in range(1,6):
    for j in range(i,6):
        print(j,end=' ')
    print( ) 

print("no 4")
for i in range(1,6):
    n = i
    for j in range(1,6):
        print(n,end=' ')
        n +=2
    print( )

print("no 5")
x = 2
for i in range(1,6):
    n = i 
    for j in range(5):
        print(n, end=' ')
        n += x
    x += 1    
    print( )

print("no 6")
b = 5
k = 5
for i in range(b, 0, -1):
    for j in range(1, k +1):
        if j < i :
            print("+", end=" ")
        else :
            print(j, end=" ")    
    print( )    

print("no 7")
b = 4
k = 5
kar = ['A','B']
for i in range(b):
    for j in range(k):
        print(kar[(i+j)%2], end=" ")   
    print( )  

print("no 8")
b = 5
kar = ['S','0']
for i in range(b):
    for j in range(b-i):
        print(kar[(i+j)%2], end=" ")   
    print( )      

print("no 9")
#looping jumlah bintang sesuai dengan angka fibonaci

a = [0, 1]
b = 10

while len(a) < b:
    next_num = a[-1] + a[-2]
    a.append(next_num)

for num in a:
    for _ in range(num):
        print("*", end=" ")
    print()

