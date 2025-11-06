import random
 lebegőpontos - float -tört
a = 1.25
b = float(input("adjon meg egy tizedestörtet: "))
print (b*4)

#gneráljon ki  [1,9] közötti tört számot 2 tizedesjegyre
#pl 1.36, 2.30

#c = random.randint(100,999)/100
c = random.random() #[0,1[
print(round(c,2))

#szövegkezelés
szoveg =input("adjon meg egy szöveget: ")
print(szoveg)
print("szöveg hossza: ",len(szoveg),"karakter"),
print("első karakter",szoveg[0])
#szöveg karakterekből épűl fel
#szöveg = karakter lánc
karakter = szoveg[0]
kod =ord(szoveg[0])
print(kod)
ujkod = kod + 1
ujkarakter = chr(ujkod)
print(ujkarakter)

#kérje a felhasználó keresztnevét/ Generáljon neki egy jelszót,
#az első 3 karakterének ascii kódjának szorzatát! ha nincs a név 3 jegyű, akkor kettő
#esetén a hossz értéke legyen a szorzat 3. taja
#1 esetén pediga köne legyen
#alma - 65 * 108 * 109
#co - 67 * 111 * 2
#G - 71 *71 *71