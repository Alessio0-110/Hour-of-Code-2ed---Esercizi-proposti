"""
In questo esercizio si richiede di progettare una funzione che prenda due argomenti, la LUNGHEZZA di un lato e il NUMERO di lati,
calcolando in uscita PERIMETRO e AREA di un relativo poligono regolare.
Ritornare None nel caso di valori di input non validi.
Aspettarsi che l'input della funzione siano due interi.
Dopo gli assert, si pone un loop di input utente per testare la funzione. Si inserisca un'espressione non valida per terminare il loop.
"""
import math
print ("Calcolatore area e perimetro di un poligono regolare.")

while True:
    numero = int(input ("Inserisci il numero dei lati: "))
    if numero < 3 or numero > 18 :
            print("Inserire un numero di lati compreso tra 3 e 18.")
            break
    lunghezza_lato = int(input ("Inserisci la lunghezza del lato: "))
    if lunghezza_lato == 0:
            print("Inserire una lunghezza valida.")
            break
    

    def poligono_regolare(lunghezza_lato, numero):
        
        numero_fisso =  [0.289, 0.5, 0.688, 0.866, 1.038, 1.207, 1.374, 1.539, 1.703, 1.866, 2.029, 2.191, 2.352, 2.514, 2.675, 2.836, 2.996, 3.157]
        
        numero_fisso= numero_fisso[lunghezza_lato-3] 
        apotema = numero_fisso * lunghezza_lato
        
        perimetro = lunghezza_lato * numero
        area = perimetro * apotema / ( 2 )
        
        print ("Perimetro: ",perimetro)
        print ("Area: ", area)
    poligono_regolare(lunghezza_lato,numero)
    break