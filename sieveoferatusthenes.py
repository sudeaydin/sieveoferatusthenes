N=input("Hangi sayiya kadar olan asal sayilari ogrenmek istiyorsunuz ? ")
N=int(N)
asalsayi=list()
for i in range(N-1):
    asalsayi.append(1)
for i in range(2,N-1,2):
    asalsayi.pop(i)
    asalsayi.insert(i,0)

nn=(N**0.5)+1
nn=int(nn)
for i in range(1,nn-1,2):
    if asalsayi[i]!=0:
        j=(i+2)**2
        while j<=N:
            asalsayi[j-2]=0
            j=j+i+2

print("{} sayisina kadar olan asal sayilar:".format(N))

for i in range(len(asalsayi)):
    if asalsayi[i]==1:
        print(i+2)
