p = 69691
g = 1001

A = 17016
B = 47643
# Dickie Hellman
# find a and b such pow
k=0
for i in range(p):
    if pow(g,i,p)==A:
        print(f'a:{i}')
        a=i
        k+=1
        if i==2:
            break
    if pow(g,i,p)==B:
        print(f'b: {i}' )
        b=i
        k+=1
        if i==2:
            break
# b: 7919
# a:12552
print(pow(B,a,p))
print(pow(A,b,p))