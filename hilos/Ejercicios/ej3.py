import threading 
import queue

lock = threading.Lock()
cola = queue.Queue()

def productor():
    print("Hilo Iniciado")
    for i in range(5):
        cola.put(i)
        print(f"Productor: el producto {i} ah sido añadido a la cola")
    print("Hilo finalizado")
def consumidor(retirar):
    print("Hilo Iniciado")
    for i in range (retirar):
       with lock:
           if not cola.empty():
               item =cola.get()
               print(f"El consumidor ah retirado el producto {item} de la cola")
    print("Hilo finalizado")

def main():

    t1 = threading.Thread(target=productor)
    t1.start()
    t1.join()

    t2 = threading.Thread(target=consumidor, args=(2,))
    t2.start()
    t2.join()

    print("Hilos finalizados")

if __name__ == "__main__":
    main()