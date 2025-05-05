import os 
import multiprocessing
import time
import random

tiempo = random.uniform(0.2, 1.0)

def proceso_hijo_uno(event):
    print(f"Proceso hijo uno: {os.getpid()}")
    print("Estado: Listo")
    time.sleep(tiempo)
    print("Hijo esperando el evento... estado bloqueado")
    event.wait()
    print(f"Hijo uno de PID:{os.getpid()} esta En ejecucion")
    print("Proceso hijo uno finalizado.")

def main():
    print("-----------------------------------------------------------------------------------")
    print(f"PID proceso padre: {os.getpid()}, padre = {os.getpid()}")
    event = multiprocessing.Event()
    p1 = multiprocessing.Process(target=proceso_hijo_uno, args=(event,))
    p1.start()
    print(f"El proceso padre inicializo el primer proceso hijo de PID: {p1.pid} y esta Nuevo")
    time.sleep(tiempo)
    event.set()
    print(f"Hijo uno de PID:{p1.pid} esta Listo")
    p1.join()
    time.sleep(tiempo)

    print("-----------------------------------------------------------------------------------")

    p2 = multiprocessing.Process(target=proceso_hijo_uno, args=(event,))
    p2.start()
    print(f"El proceso padre inicializo el primer proceso hijo de PID: {p2.pid} y esta Nuevo")
    time.sleep(tiempo)
    event.set()
    print(f"Hijo uno de PID:{p2.pid} esta Listo")
    p2.join()
    time.sleep(tiempo)

    print("-----------------------------------------------------------------------------------")

    p3 = multiprocessing.Process(target=proceso_hijo_uno, args=(event,))
    p3.start()
    print(f"El proceso padre inicializo el primer proceso hijo de PID: {p3.pid} y esta Nuevo")
    time.sleep(tiempo)
    event.set()
    print(f"Hijo uno de PID:{p3.pid} esta Listo")
    p3.join()
    time.sleep(tiempo)

    print("-----------------------------------------------------------------------------------")

    print("Proceso padre finalizados")
    
if __name__ == "__main__":
    main()