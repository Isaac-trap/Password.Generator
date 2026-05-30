def ConfigPass():
    import string
    while 1:
        l = input("determina el largo de la contraseña: ")
        if l.isdigit() == False :
            print("debe ingresar un numero, ejemplo: 6")
        else:
            break
    while 1:
        choise3=input("deseas agregar simbolos? Y/N: ")
        choise2=input("deseas agregar numeros? Y/N: ")
        choise1=input("deseas agregar letras? Y/N: ")
        if (choise1.upper() not in ("Y", "N")or choise2.upper() not in ("Y", "N")or choise3.upper() not in ("Y", "N")):
            print("debes escoger Y o N")
            continue
            print("debes escoger ""Y"" o ""N""")
        if (choise1.upper() == "Y") and (choise2.upper() == "Y") and(choise3.upper() == "Y"):
            characters= (string.ascii_letters+string.digits+string.punctuation)
            break
        elif (choise1.upper() == "Y") and (choise2.upper() == "Y") and(choise3.upper() == "N"):
            characters= (string.ascii_letters+string.digits)
            break
        elif (choise1.upper() == "Y") and (choise2.upper() == "N") and(choise3.upper() == "Y"):
            characters= (string.ascii_letters+string.punctuation)
            break
        elif (choise1.upper() == "N") and (choise2.upper() == "Y") and(choise3.upper() == "Y"):
            characters= (string.digits+string.punctuation)
            break
        elif (choise1.upper() == "Y") and (choise2.upper() == "N") and(choise3.upper() == "N"):
            characters= (string.ascii_letters)
            break
        elif (choise1.upper() == "N") and (choise2.upper() == "N") and(choise3.upper() == "Y"):
            characters= (string.punctuation)
            break
        elif (choise1.upper() == "N") and (choise2.upper() == "N") and(choise3.upper() == "N"):
            print("no puedes elimar todos")
    return l, characters

def CreatePass(le,config):
    import random
    c = []
    for i in range(int(le)):
        a = random.choice(config)
        c.append(a)
    c = "".join(c)
    return print(c)