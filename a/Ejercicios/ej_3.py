import os 
import multiprocessing
import time

def proceso_hijo_uno(event, event2):
    print(f"Proceso hijo uno: {os.getpid()}")
    print("Estado: Listo")
    time.sleep(0.5)
    print(f"Hijo uno de PID:{os.getpid()} esta En ejecucion")
    print("Hijo esperando el evento... estado bloqueado")
    event.wait()
    print("Proceso hijo uno finalizado.")
def proceso_hijo_dos(event, event2):
    print(f"Proceso hijo dos: {os.getpid()}")
    print("Estado: Listo")
    time.sleep(0.5)
    print(f"Hijo dos de PID:{os.getpid()} esta En ejecucion")
    print("Hijo esperando el evento... estado bloqueado")
    event.wait()
    print("Proceso hijo dos finalizado.")

def main():
    event2 = multiprocessing.Event()
    event = multiprocessing.Event()

    p1 = multiprocessing.Process(target=proceso_hijo_uno, args=(event,))
    p1.start()
    print(f"El proceso padre inicializo el primer proceso hijo de PID: {p1.pid} y esta Nuevo")
    time.sleep(2)
    event.set()
    print(f"Hijo uno de PID:{p1.pid} esta Listo")
    p1.join()
    time.sleep(1)

if __name__ == "__main__":
    main()