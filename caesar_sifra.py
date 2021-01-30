# definovani funkci

# nacteni vstupnich dat
def nacist_text(soubor):
    try:
        with open(soubor, 'r') as h:
            obsah = h.readlines() 
        return obsah
    except FileNotFoundError:
        exit("Nenalezen vstupní soubor vstup.txt")
    except PermissionError:
        exit("Nemám přístup k vstupnímu souboru vstup.txt")

# zaklicovani abecedy - tj. vytvoreni nove abecedy dle klice
def zaklicovani(klic):
    abc_velka = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    abc_mala = "abcdefghijklmnopqrstuvwxyz"
    nova_velka = list(abc_velka)
    nova_mala = list(abc_mala)
    # zaklicovani predni casti nove abecedy
    for i in range(len(abc_velka)-klic):
        nova_velka[i] = abc_velka[i+klic]
        nova_mala[i] = abc_mala[i+klic]
    # zaklicovani konce nove abecedy
    for k in range(klic):
        nova_velka[len(abc_velka)-1-k]=abc_velka[klic-k-1]
        nova_mala[len(abc_mala)-1-k]=abc_mala[klic-k-1]
    return(abc_velka, abc_mala, nova_velka, nova_mala)

# prevod textu do cesarovy sifry
def do_cesara(vstup, klic):
    abc_velka, abc_mala, nova_velka, nova_mala = zaklicovani(klic)
    vystup = list(vstup)
    for i in range(len(vstup)):
        if vstup[i] in abc_velka:
            kdeje = abc_velka.find(vstup[i])
            vystup[i] = nova_velka[kdeje]
        elif vstup[i] in abc_mala:
            kdeje = abc_mala.find(vstup[i])
            vystup[i] = nova_mala[kdeje]
        else:
            vystup[i] = vstup[i]
    return(vystup)

# prevod textu zpet z cesarovy sifry do citelneho
def z_cesara(vystup, klic):
    abc_velka, abc_mala, nova_velka, nova_mala = zaklicovani(klic)
    zpatky = list(vystup)
    for i in range(len(vystup)):
        if vystup[i] in abc_velka:
            kdeje = nova_velka.index(vystup[i])
            zpatky[i] = abc_velka[kdeje]
        elif vystup[i] in abc_mala:
            kdeje = nova_mala.index(vystup[i])
            zpatky[i] = abc_mala[kdeje]
        else:
            zpatky[i] = vystup[i]
    return(zpatky)

# zasifrovani textu a ulozeni do souboru
def uloz_sifru(co, kam, klic):
    try:
        with open(kam,'w') as k:
            for radek in co:
                vcezaru = do_cesara(radek, klic)
                for i in vcezaru:
                    k.write(str(i))
    except PermissionError:
        exit("Nemám přístup k výstupnímu souboru zaklicovane.txt")

# rozsifrovani textu a ulozeni do souboru
def uloz_rozklicovane(co, kam, klic):
    try:
        with open(kam,'w') as k:
            for radek in co:
                zcezara = z_cesara(radek, klic)
                for i in zcezara:
                    k.write(str(i))
    except PermissionError:
        exit("Nemám přístup k výstupnímu souboru rozklicovane.txt")

# hlavni cast programu

# nacteni hodnoty klice od uzivatele
p=1
while p==1: 
    try:
        klic = int(input("Zadej hodnotu klice:"))
        if klic<0 or klic>26:
            print("Klíč musí být v rozsahu 0 - 26")
        else:
            p+=1
    except ValueError:
        exit("Hodnota klíče musí být celé číslo.")

# nacteni textu ze souboru vstup.txt 
vstupni_text = nacist_text('vstup.txt')
# ulozeni zasifrovaneho textu do zaklicovane.txt
uloz_sifru(vstupni_text,'zaklicovane.txt', klic)
# nacteni zasifrovaneho textu
zasifrovany_text = nacist_text('zaklicovane.txt')
# rozklicovani zasifrovaneho textu a ulozeni do souboru rozklicovane.txt
uloz_rozklicovane(zasifrovany_text,'rozklicovane.txt',klic)