def citire():
    l=[]
    givenstring = input("Introduceti elementele listei separate prin cate o virgula: ")
    charsAsString = givenstring.split(",")
    for x in charsAsString:
        l.append(x)
    return l

def segaseste(l,c):
    '''
    param: l-lista,c-sirul care trebuie gasit in lista
    return: True daca se gaseste,false daca nu se gaseste
    '''
    for x in l:
        if x ==c:
            return True
    return False

def test_gaseste():
    assert segaseste(['aaa','bbb','ccc'],'aaa') == True
    assert segaseste(['aaa','bbb','ccc','ddd'],'eee') == False
    assert segaseste(['aaa','bbb','ccc','zzz','yyy'],'ccc') == True

def repeta(l,s):
    '''
    param:l-lista initiala,s-lista in care vom pune elementele care se repeta
    return :s-lista in care vom pune elementele care se repeta
    '''
    s=[]
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[i] == l[j]:
                s.append(l[j])
    
    return s

def test_repeta():
    s=[]
    assert repeta(['aaa','bbb','ccc','aaa','bbb','ccc'],s) ==['aaa','bbb','ccc']
    assert repeta(['aaa','bbb','ccc','ddd'],s) ==[]
    assert repeta(['yyy','zzz','aaa','bbb','ccc','ddd','zzz'],s) ==['zzz']

def pal(l,c):
    '''
    param:l-lista initiala,c-lista unde vom pune toate string-urile care sunt palindroame
    return:c-lista unde vom pune toate string-urile care sunt palindroame
    '''

    c=[] 
    for x in l:
        if x == x[::-1]:
            c.append(x)
    return c

def test_pal():
    c=[]
    assert pal(['aaa','abb','acc'],c) ==['aaa']
    assert pal(['abb','bba','cca'],c) ==[]
    assert pal(['zxz','yzy','bab','abb','caa'],c) == ['zxz','yzy','bab']
'''
def inloc(l):
    c=[]
    max_frequency = {}
    for j in l:
        for i in l[j]:
            if i in max_frequency:
                max_frequency[i] += 1
            else:
                max_frequency[i] = 1
        my_result = max(max_frequency, key = max_frequency.get)
    print(my_result)
'''

    



def printmenu():
    print("1) Citirea listei:")
    print("a) Afisarea listei: ")
    print("2) Verificare daca un sir citit de la tastatura se gaseste in lista: ")
    print("3) Afisarea unei liste cu toate sirurile de caractere care  se repeta: ")
    print("4) Afisati toate sirurile din lista care sunt palindrom: ")
    print("5) Afișați lista obținută prin înlocuirea șirurilor care conțin caracterul care apare de cele mai multe ori în toată lista: ")

def main():
    test_gaseste()
    test_repeta()
    test_pal()
    l=[]
    s=[]
    l1=[]
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
        elif optiune  =="3":
            d=repeta(l,s)
            print(d)
        elif optiune =="4":
            e=pal(l,l1)
            print(e)
        elif optiune =="5":
            pass
        elif optiune =="x":
            break
        else:
            print("Optiune incorecta,reincercati:")
            pass

        



main()