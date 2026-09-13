def ConfigPass():
    import string
    while 1:
        l = input("determina el largo de la contraseña de minimo 3: ")
        if l.isdigit() == False :
            print("debe ingresar un numero, ejemplo: 6")
            continue
        if ((int(l) - 3) == -1 ) or ((int(l) - 3) == -2) or ((int(l) - 3) == -3):
            print("debe ser como minimo de 3 caracteres")
        else:
            break
    while 1:
        choise3=input("deseas agregar simbolos? Y/N: ")
        choise2=input("deseas agregar numeros? Y/N: ")
        choise1=input("deseas agregar letras? Y/N: ")
        if (choise1.upper() not in ("Y", "N")or choise2.upper() not in ("Y", "N")or choise3.upper() not in ("Y", "N")):
            print("debes escoger Y o N")
            continue
        if (choise1.upper() == "Y") and (choise2.upper() == "Y") and(choise3.upper() == "Y"):
            characters= (string.ascii_letters+string.digits+string.punctuation)
            c = string.ascii_letters,string.digits,string.punctuation
            break
        elif (choise1.upper() == "Y") and (choise2.upper() == "Y") and(choise3.upper() == "N"):
            characters= (string.ascii_letters+string.digits)
            c = string.ascii_letters,string.digits
            break
        elif (choise1.upper() == "Y") and (choise2.upper() == "N") and(choise3.upper() == "Y"):
            characters= (string.ascii_letters+string.punctuation)
            c = string.ascii_letters,string.punctuation
            break
        elif (choise1.upper() == "N") and (choise2.upper() == "Y") and(choise3.upper() == "Y"):
            characters= (string.digits+string.punctuation)
            c = string.digits,string.punctuation
            break
        elif (choise1.upper() == "Y") and (choise2.upper() == "N") and(choise3.upper() == "N"):
            characters= (string.ascii_letters)
            c = string.ascii_letters
            break
        elif (choise1.upper() == "N") and (choise2.upper() == "Y") and(choise3.upper() == "N"):
            characters= (string.digits)
            c = string.digits
            break
        elif (choise1.upper() == "N") and (choise2.upper() == "N") and(choise3.upper() == "Y"):
            characters= (string.punctuation)
            c = string.punctuation
            break
        elif (choise1.upper() == "N") and (choise2.upper() == "N") and(choise3.upper() == "N"):
            print("no puedes elimar todos")
    return int(l), characters, c

def CreatePass(le,config,c):
    import random
    contraseña = []
    obligatorio = []
    for i in range(len(c)):
        b =(random.choice(c[i]))
        obligatorio.append(b)
    rest = int(le) - int(len(obligatorio))
    for i in range(rest):
        a = random.choice(config)
        contraseña.append(a)
    contraseña = contraseña + obligatorio
    random.shuffle(contraseña)
    p = "".join(contraseña)
    return p

