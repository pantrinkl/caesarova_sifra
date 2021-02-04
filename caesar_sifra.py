# defining functions

# load input data
def load_text(textfile):
    try:
        with open(textfile, 'r') as h:
            content = h.readlines() 
        return content
    except FileNotFoundError:
        exit("Nenalezen vstupní soubor.")
    except PermissionError:
        exit("Nemám přístup k vstupnímu souboru.")

# generate new alphabet with key
def generate_abc(key):
    abc_big = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    abc_small = "abcdefghijklmnopqrstuvwxyz"
    new_big = list(abc_big)
    new_small = list(abc_small)
    for i in range(len(abc_big)-key):
        new_big[i] = abc_big[i+key]
        new_small[i] = abc_small[i+key]
    for k in range(key):
        new_big[len(abc_big)-1-k]=abc_big[key-k-1]
        new_small[len(abc_small)-1-k]=abc_small[key-k-1]
    return(abc_big, abc_small, new_big, new_small)

# generate text into Caesars cipher
def to_cesar(intext, key):
    abc_big, abc_small, new_big, new_small = generate_abc(key)
    outtext = list(intext)
    for i in range(len(intext)):
        if intext[i] in abc_big:
            where = abc_big.find(intext[i])
            outtext[i] = new_big[where]
        elif intext[i] in abc_small:
            where = abc_small.find(intext[i])
            outtext[i] = new_small[where]
        else:
            outtext[i] = intext[i]
    return(outtext)

# generate text from Caesars cipher to regular
def from_cesar(outtext, key):
    abc_big, abc_small, new_big, new_small = generate_abc(key)
    back = list(outtext)
    for i in range(len(outtext)):
        if outtext[i] in abc_big:
            where = new_big.index(outtext[i])
            back[i] = abc_big[where]
        elif outtext[i] in abc_small:
            where = new_small.index(outtext[i])
            back[i] = abc_small[where]
        else:
            back[i] = outtext[i]
    return(back)

# save text in Caesars cipher to text file
def save_cipher(what, where, key):
    try:
        with open(where,'w') as k:
            for line in what:
                incesar = to_cesar(line, key)
                for i in incesar:
                    k.write(str(i))
    except PermissionError:
        exit("Nemám přístup k výstupnímu souboru zaklicovane.txt")

# save text from Caesars cipher to text file
def save_decrypted(what, where, key):
    try:
        with open(where,'w') as k:
            for line in what:
                fromcesar = from_cesar(line, key)
                for i in fromcesar:
                    k.write(str(i))
    except PermissionError:
        exit("Nemám přístup k výstupnímu souboru rozklicovane.txt")

# main program

# get key value from user
p=1
while p==1: 
    try:
        key = int(input("Zadej hodnotu klice: "))
        if key<0 or key>26:
            print("Klíč musí být v rozsahu 0 - 26")
        else:
            p+=1
    except ValueError:
        exit("Hodnota klíče musí být celé číslo.")

# get input file name from user
input_name = str(input("Zadejte název vstupního souboru: "))

# load text from file: vstup.txt 
input_text = load_text(input_name)
# save translated text to Caesars cipher to file: zaklicovane.txt
save_cipher(input_text,'zaklicovane.txt', key)
# load translated text
encrypted_text = load_text('zaklicovane.txt')
# save translated text to readable format to: rozklicovane.txt
save_decrypted(encrypted_text,'rozklicovane.txt',key)