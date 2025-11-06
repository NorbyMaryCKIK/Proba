import random
import math
import tkinter as tk
def randomanimal():
    t =  ["kutya", "macska", "papagaj", "hal", "hörcsög"]
    r = str(random.randint(10,999))
    if(len(r) ==2):
        r = "0"+r
    print (r)
    
    paratlanok = 0
    
    for i in r:
        if(int(i) % 2 !=0):
            paratlanok += 1

    print(paratlanok)
    print(t[paratlanok])

def szamkategoria(szam):
        if(szam == 0):
            print("Nulla")
        elif(9 >=szam >0):
            print("Egyjegyű pozitív")
        elif(10<=szam <=99):
            print("ketjegyu")
        elif(szam >=100):
            print("haromjegyu")
        else:
            print("negetiv szam")


def szoelemzo(szoveg):
    maganhangzok = ["a", "á", "e", "é", "i", "í", "o", "ó", "ö", "ő", "u", "ú", "ü", "ű"]
    maganhangzok_szama = 0
    massalhangzok_szama = 0

    for i in szoveg: #i akarmi lehet, a "szoveg" is
        if(i != " "):
            if(i in maganhangzok):
                maganhangzok_szama += 1
            else:
                massalhangzok_szama += 1

    print(f"Maganhangozk {maganhangzok_szama} Mássalhanzók {massalhangzok_szama}")

#Feladat 1.

def teglalap():
    ao = int(input("Add meg az A-oldalát: "))
    bo = int(input("Add meg a B-oldalát: "))

    print("Kerület", 2* ao +  2* bo )
    print("Terület", ao * bo)

#Feladat 2.

def koratmero():
    r = 5
    atmero = 2 * r
    kerulet = math.pi * atmero
    terulet = (math.pi /4) *atmero **2
    print("atmero",atmero,"kerulet",kerulet,"terulet",terulet)

#Feladat 3.

def haromszog_oldalai():
    a = 5
    b = 6
    c = 7
    kerulet = a + b + c
    s = kerulet / 2
    terulet = math.sqrt(s * (s - a) * (s - b) * (s - c))
   
    print("Kerület :",kerulet,"terulet",terulet)

#Feladat 4.

def szabalyos_haromszog_o():
    A = 10
    magassag = A* math.sqrt(3) / 2
    print("Magassag",magassag)

#Feladat 5.

def haromszog_lap():
    a = float(input("Add meg a kocka élének hosszát: "))
    lap_atlo = a* math.sqrt(2)
    test_atlo =a* math.sqrt(3)
    print(f"A lapátló hossza: {lap_atlo:.2f}")
    print(f"A testátló hossza: {test_atlo:.2f}")

#Feladat 6.

def vnev_knev():
    vezeteknev = input("Add meg a vezetek neved: ")
    keresztnev = input("Add meg a keresztneved: ")
    vezetek_keresz = vezeteknev + " " + keresztnev
    print(vezetek_keresz)

#Feladat 7.

def Parose():
    szam = int(input("Adj meg egy számot: "))
    if szam % 2 ==0:
        print("Páros a számod",szam)
    else:
        print("Páratlan a számod",szam)

#Feladat 8.

def eredmeny():
    jegy = int(input("add meg a jegyet amit kaptál: "))
    if (jegy == 1):
        print("Elégtelen")
    elif(jegy == 2):
        print("Elégséges")
    elif(jegy == 3):
        print("Közepes")
    elif(jegy == 4):
        print("Jó")
    elif(jegy == 5):
        print("Kiválló")
    else:
        print("Nem azonosítható jegy")

#Feladat 9.

def szilarde():
    fok = 0
    if fok <= 0:
        print("Szilárd")
    elif fok < 100:
        print("Folyékony")
    else:
        print("Gáz")

#Feladat 10.

def haromszogszerkzethetoe():
    a = 1
    b = 1
    c = 10
    if(a+b>c or b+c>a or a+c>b):
        print("Szerkeztheto")
    else:
        print("nem szerkeztheto")

#Feladat 11.

def farenheittocelsius():
    F = float(input("Add meg a homersekletet Farenheiben : "))
    c = (F - 32) * 5 / 9
    print("Celsiusban ez :",c,"-fok")

#Feladat 12.

def celsiustofarenheit():
    c = float(input("Add meg a homersekletet Celsiusban"))
    f = c * 9 / 5 + 32
    print("Farenheitben ez :",f,"fok")

#Feladat 13.

def mptoh():
    masodperc = int(input("Adj meg egy szamot"))
    ora = masodperc // 3600
    maradek_masodperc = masodperc % 3600
    perc = maradek_masodperc // 60
    mp = maradek_masodperc % 60

    print(f"{ora} ó {perc} p {mp} mp")

#Feladat 14.
def utolsokarakter():
    szo = input("Adj meg egy szót: ")
    utolsobetu = (szo[-1])
    print("utolsó karakter: ",utolsobetu)

#Feladat 15.
def utolsoandelso():
    szo = input("Adj meg egy szót : ")
    betu1 = (szo[0])
    betuutso = (szo[-1])

    print(betu1,betuutso)

#Feladat 16.
def mindenmasodik():
    szo = input("adj meg egy szót : ")
    betuk = (szo[::2])
    print(betuk,)

#Feladat 17.-18.

def visszafele():
    szo = input("adj meg egy szót : ")
    v = (szo[::-1])
    print(v*3)

#Feladat 19.
def visszafele2():
    szo = input("adj meg egy szót : ")
    vszo2 = (szo[::2])
    print(vszo2[::-1])

#Feladat 20.
def bekertvissza():
    szoveg = input ("adj meg egy szoveget")
    print(szoveg.replace(" ",""))

#Feladat 21. 
def palindrom():
    szo = input("adj meg egy szot")
    if szo == szo[::-1]:
        print("ez egy palindrom szam")
    else: 
        print("ez nem egy palindrom szam")

#Feladat 22.



#Gyakorlas
def allatok():
    allatok = ["Kutya","Macska","Elefant","Zsiraf"]
    random.randint(10,999)

def maybegambling():
    teszam = int(input("adj meg egy szamot"))
    szam = random.randint(0,50)
    if szam >teszam:
            print("vesztettel", szam)
    else:
        print("nyertel")
    
#Ablak
def kisproba():
    ablak = tk.Tk()
    ablak.title("Ablak")
    ablak.geometry("800x400")

    ablak.mainloop()

def nmtom():
     r = random.randint(0,999)
     r2 = random.randint(0,999)
     sz = int(input("adj meg egy szamot"))
     print(r,"+",r2,"+",sz,"a szamok osszege =", r+r2+sz)


        






   
#meg egy feladat

    # t = ["Laci","Akos","Cumler"]
    # for i in range( len(t)):
    #     print("Szia " + t[i])


def main():
    # randomanimal()
    # szamkategoria(99) #<-- szam
    # szoelemzo("kaki")
    # teglalap()
    # koratmero()
    # haromszog_oldalai()
    # szabalyos_haromszog_o()
    # haromszog_lap()
    # vnev_knev()
    # Parose()
    # eredmeny()
    # szilarde()
    # haromszogszerkzethetoe()
    # farenheittocelsius()
    # celsiustofarenheit()
    # mptoh()
    # utolsokarakter()
    # utolsoandelso()
    # mindenmasodik()
    # visszafele()
    # visszafele2()
    #  bekertvissza()
    #  palindrom()
    # maybegambling()
    # kisproba()
    # nmtom()
    nmtom2()
main()