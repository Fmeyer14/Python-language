
import time
while 54: # Boucle infinie
    a = time.localtime()
    print (a[2],"/", a[1],"/",a[0]) # On affiche jour, le moi et l'année
time.sleep(0.25) # 0.25s est le taux de rafraichissement
