# kérjen be egy egész számot és döntse el, hogy páros vagy páratlan?
import math
szam = int(input("Adjon meg egy egész számot:"))
if(szam % 2 == 0):
    print("páros")
else:
    print("páratlan")

    #Kérjen be a felhasználótol egy számot és mondja 
    # meg, hogy 10-zel osztható -e?
    #Ha nem osztható 10-zel írja ki az utolsó számjegyet

if(szam % 10 ==0):
    print("Tízzel osztható")
else:
    print("Tízzel nem osztható")
    print("Az utolsó számjegy:"+ str(szam % 10))

    szam2 = int(input("Adjon meg még egy egész számot:"))
if(szam !=0):
    if(szam2 != 0):
        rec = 1/szam
        rec2 = 1/szam2
        print(rec+rec2)
    else:
        print("a második számnak nincs reciproka")
else:
    print("az első számnak nincs reciproka")
    #adja meg a két számnak a gyökét

    if(szam + szam2 >=0):
        print(math.sqrt(szam+szam2))
    else:
        print("A két szám összege negatív")


if(szam != 0 and szam2 != 0):
    rec = 1/szam
    rec2 = 1/szam2
    print(rec+rec2)
else:
    print("A kér szám valamelyike nulla!")

    #HF : bool algebra
    #HF : Kérjen be a felhasználótol 3 db számot (lehet tört is) a három szám egy háromszöh három oldala
    #1. derékszög-e a háromszög?
    #2. egyenlőszárú-e a háromszög?
    # 3 szabályos-e a háromszög?

    
a = float(input("Add meg az első oldalt: "))
b = float(input("Add meg a második oldalt: "))
c = float(input("Add meg a harmadik oldalt: "))


if a + b > c and a + c > b and b + c > a:
    print("Ez egy létező háromszög.")

   
    oldal = sorted([a, b, c]) 
    if abs(oldal[0]**2 + oldal[1]**2 - oldal[2]**2) < 1e-6:
        print("Derékszögű háromszög.")
    else:
        print("Nem derékszögű háromszög.")

 
    if a == b or b == c or a == c:
        print("Egyenlő szárú háromszög.")
    else:
        print("Nem egyenlő szárú háromszög.")

  
    if a == b == c:
        print("Szabályos háromszög.")
    else:
        print("Nem szabályos háromszög.")

else:
    print("Nem létező háromszög. (A háromszög-egyenlőtlenség nem teljesül)")

#HF python - ciklusok, loops, literációk,...

#HF generáljon ki három véletlen háromjegyű számot,amelyk 13-AL OSZTHATÓAK!
#Állítsa ezeke sorrandbe
#adja meg az átlaguk!
#van-e közöttük 4-el végződő

#otthon tessek lemasolni a github-os repository tartalmát (pull)
#házi elkeszitese
#add, commit, push
#git learning breanching web oldal

