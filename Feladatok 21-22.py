import random

def vmi():
    mondat = input("Mondat: ")
    maganhangzok = ["a", "á", "e", "é", "i", "í", "o", "ó", "ö", "ő", "u", "ú", "ü", "ű"]
    r = random.randint(10, 999)
    
    db = 0 
    for betu in mondat.lower():  
        if betu in maganhangzok:
            db += 1
    
    print(db)

def main():
    vmi()

main()
