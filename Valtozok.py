# VÁLTOZÓ deklarálása ás inicialiálása
#változó létrehozása és kezdőérték adása
# valtozoNev = "Kezdoertek"
nev = "Mari Norbert"
osztaly = "10.B"
datum ="2025.09.08"

print(nev,osztaly,datum,sep="\n")
  #osszefuzes csak szöveg ki írasa. kettö vagy tobb osszefuzes=szoveg1+szoveg2
osszefuzes= nev+osztaly
print(osszefuzes)
#többszörözés
soknev = nev * 5
print(soknev)
"""
Elemi Típusok
-szöveg-string-str
(-karakter)
-szám - egész(integer- int), lebegőpontos (tört) (Float)
-Logikai - true, false
"""
aEgesz = 123
bTort = 34.23
szSzam ="12"
logikai = True

print("a Egész", aEgesz)
print("B Tört", bTort)
print("sz Szám", szSzam)
print("logikai",logikai)

# Egesz Operatorok
print("a + 2 =",aEgesz + 2)
print("a - 2 =",aEgesz - 2)
print("a * 2 =",aEgesz * 2)
print("a / 2 =",aEgesz / 2)

#Div  egészrész, Mod - modulus(maradék)
#Div = //
#mod = °%

print("a div 8 =", aEgesz // 8)
print("a mod 8 =", aEgesz % 8)

print(int(szSzam)+aEgesz)
print(szSzam+str (aEgesz))


print(str(aEgesz)+szSzam)
print(aEgesz+int(szSzam))