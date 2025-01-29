import tools
import tools.Baraja
#from Baraja import cara, valor  

for i in range(len(tools.Baraja.cara)):
    for j in range(len(b.valor)):
        print(b.valor[j], " de ", b.cara[i], sep="")
        
r = b.abs(-10)
print(r)
