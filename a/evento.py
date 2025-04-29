import os 
import time
import multiprocessing

def proceso_hijo(evento):
    print("Hijo esperando el evento..")
    evento.wait()#Espera a recibir el evento
    print("Hijo recibio el evento.")
def main():
    evento = multiprocessing.Event()#Crea un evento
    p = multiprocessing.Process(target=proceso_hijo, args=(evento,))
    p.start()
    
    time.sleep(1)
    print("Padre activa el evento")
    evento.set()#Manda el evento
    
    p.join()
    
if __name__ == "__main__":
    main()