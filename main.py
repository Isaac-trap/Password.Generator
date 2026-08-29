import funtionsPM as Red
l = Red.ConfigPass()
le = l[0]
config = l[1]
c = l[2]
print(config)
print(c)
p = Red.CreatePass(le,config)
print(p)
Red.SafeConfig(p,c,le)