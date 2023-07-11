import random
#estrazione di una parola random da un file di testo
lista=[]
file = open("lista_parole.txt", "r") # Apertura in modalità lettura
righe= file.readlines() # Legge una singola riga del file
for parola in righe:
    lista.append(parola)
parola_incognita=random.choice(lista)

#scelgo il livello di difficoltà
livello=input("Scegli il livello: \n1:facile\n2:intermedio\n3:difficile\n ")
while livello!=str(1) and livello!=str(2) and livello!=str(3):
    print("SCELTA NON VALIDA:RIPROVA")
    livello=input("Scegli il livello: \n1:facile\n2:intermedio\n3:difficile\n ")
if livello==str(1):
    tentativi_iniziali=10
elif livello==str(2):
    tentativi_iniziali=6
elif livello==str(3):
    tentativi_iniziali=3
print("Hai "+str(tentativi_iniziali)+" tentativi")

#stampa gli underscore in base alle lettere della parola

print("PAROLA DA INDOVINARE: " +  "_"*len(parola_incognita))
tentativi=tentativi_iniziali
while tentativi>0:
    input

    