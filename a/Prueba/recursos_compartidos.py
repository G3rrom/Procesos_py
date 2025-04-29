import os 
import time
import multiprocessing

def proceso_hijo(valor):
    print(f"Valor: {valor.value}")#Se muestra viejo valor (0)
    valor.value = 80#Se modifica
   
    
def main():
    valor = multiprocessing.Value('i', 0)#Creas un valor y entre '' definis el tipo de valor.
    p = multiprocessing.Process(target=proceso_hijo, args=(valor,))
    p.start()
    

    
    p.join()
    print(f"Padre vio el valor: {valor.value}")#Se muestra el nuevo valor (80)
    
if __name__ == "__main__":
    main()