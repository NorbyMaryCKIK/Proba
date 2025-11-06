import math
import random

#2. feladat---------------------------------------------------------------

ora = int(input("Adja meg a tenger alatt töltött időt, órában :"))
het = ora//168
nap = (ora -het * 168) //24
ora2 = (ora -het * 168)  - nap *24 
print("Átszámolva", het,"hét",nap,"nap",ora2,"ora")

#3. feladat---------------------------------------------------------------

szam = random.randint(100,999)
print("generált hármjegyű szám",szam)
elso = szam // 100
masodik = (szam -elso * 100) //10
harmadik = szam % 10

if(elso ** 3 +masodik **3 + harmadik ** 3 == szam):
    print("a szam Armstrong szam")
else:
    print("Nem armstorng szam")

#4. feladat---------------------------------------------------------------

a = random.randint(0,10)
b = random.randint(0,10)
c = random.randint(0,10)

print(a,b,c)
if(a != 0 and b !=0 and c !=0):
    harmonk = 3 / (1/a + 1/b + 1/c)
elif(a == 0 and b != 0 and c !=0):
    print("2")