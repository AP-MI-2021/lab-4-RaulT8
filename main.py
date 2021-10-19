def citire():
    l=[]
    givenstring = input("Introduceti elementele listei separate prin cate o virgula: ")
    charsAsString = givenstring.split(",")
    for x in charsAsString:
        l.append(x)
    return l

def segaseste(l,c):
    for x in l:
        if x ==c:
            return True
    return False




def printmenu():
    print("1) Citirea listei:")
    print("a) Afisarea listei: ")
    print("2) Verificare daca un sir citit de la tastatura se gaseste in lista: ")
    print("3) Afisarea unei liste cu toate sirurile de caractere care nu se repeta: ")
    print("4) Afisati toate sirurile din lista care sunt palindrom: ")
    print("5) ")

def main():
    l=[]
    while True:
        printmenu()
        optiune = input("Introduceti optiunea: ")
        if optiune =="1":
            l=citire()
        elif optiune =="a":
            print(l)
        elif optiune =="2":
            c=str(input("Dati un sir: "))
            var =segaseste(l,c)
            if var ==1:
                print("DA")
            else:
                print("NU")
        



main()