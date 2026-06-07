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
            c = string.digits+string.punctuation
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
    return l, characters, c

def CreatePass(le,config):
    import random
    c = []
    for i in range(int(le)):
        a = random.choice(config)
        c.append(a)
    p = "".join(c)
    return p,

def SafeConfig(p,c,le):
    import random
    import string
    letters = []
    digits = []
    puntuations = []
    if (c == string.ascii_letters) or (c == string.digits) or (c == string.punctuation):
        return print(p)
    elif c == (string.ascii_letters,string.digits,string.punctuation):
        for i in p:
            if i in string.ascii_letters:
                letters = letters + 1
            elif i in string.digits:
                digits = digits + 1
            else:
                puntuations = puntuations + 1
            if letters == 0:
                a = random.randint(1,le)
                for i in range(a):
                    b = random.randint(0,le)
                    p.pop(b)
                    d = random.randint(string.ascii_letters)
                    p.append(b,d)
                return print(p)
            elif digits == 0:
                a = random.randint(1,le)
                for i in range(a):
                    b = random.randint(0,le)
                    p.pop(b)
                    d = random.randint(string.digits)
                    p.append(b,d)
                return print(p)
            elif puntuations == 0:
                a = random.randint(1,le)
                for i in range(a):
                    b = random.randint(0,le)
                    p.pop(b)
                    d = random.randint(string.punctuation)
                    p.append(b,d)
                return print(p)
    elif c == (string.ascii_letters,string.digits):
        for i in p:
            if i in string.ascii_letters:
                letters = letters + 1
            elif i in string.digits:
                digits = digits + 1
            if letters == 0:
                a = random.randint(1,le)
                for i in range(a):
                    b = random.randint(0,le)
                    p.pop(b)
                    d = random.randint(string.ascii_letters)
                    p.append(b,d)
                return print(p)
            elif digits == 0:
                a = random.randint(1,le)
                for i in range(a):
                    b = random.randint(0,le)
                    p.pop(b)
                    d = random.randint(string.digits)
                    p.append(b,d)
                return print(p)
    elif c == (string.ascii_letters,string.punctuation):
        for i in p:
            if i in string.ascii_letters:
                letters = letters + 1
            else:
                puntuations = puntuations + 1
            if letters == 0:
                a = random.randint(1,le)
                for i in range(a):
                    b = random.randint(0,le)
                    p.pop(b)
                    d = random.randint(string.ascii_letters)
                    p.append(b,d)
                return print(p)
            elif puntuations == 0:
                a = random.randint(1,le)
                for i in range(a):
                    b = random.randint(0,le)
                    p.pop(b)
                    d = random.randint(string.punctuation)
                    p.append(b,d)
                return print(p)
    elif c == (string.digits,string.punctuation):
        for i in p:
            if i in string.digits:
                digits = digits + 1
            else:
                puntuations = puntuations + 1
            if digits == 0:
                a = random.randint(1,le)
                for i in range(a):
                    b = random.randint(0,le)
                    p.pop(b)
                    d = random.randint(string.digits)
                    p.append(b,d)
                return print(p)
            elif puntuations == 0:
                a = random.randint(1,le)
                for i in range(a):
                    b = random.randint(0,le)
                    p.pop(b)
                    d = random.randint(string.punctuation)
                    p.append(b,d)
                return print(p)