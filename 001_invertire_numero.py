"""
In questo esercizio si richiede di invertire un dato numero intero, es: 1234 diventa 4321.
Aspettarsi che l'input della funzione da definire sia già un numero intero n.
"""
x= input
def inverti_numero (x):
    x= input ("inserisci un numero: ")
    x=  list(str(x))
    
    str1="".join(x)
    leggi_x = len(str1)
    inverti_x = str1[leggi_x::-1]
    print(inverti_x)
inverti_numero(x)