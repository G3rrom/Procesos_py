import os 
import multiprocessing
import time

def proceso_hijo_uno():
    print(f"Proceso hijo uno: {os.getpid()}, padre = {os.getpid()}")
    time.sleep(2)
    print("Proceso hijo uno finalizado.")
    
def proceso_hijo_dos():
    print(f"Proceso hijo dos: {os.getpid()}, padre = {os.getpid()}")
    time.sleep(2)
    print("Proceso hijo dos finalizado.")
    
def proceso_hijo_tres():
    print(f"Proceso hijo tres: {os.getpid()}, padre = {os.getpid()}")
    time.sleep(2)
    print("Proceso hijo tres finalizado.")

def main():
    print(f"PID proceso padre: {os.getpid()}, padre = {os.getpid()}")
    
    p1 = multiprocessing.Process(target=proceso_hijo_uno)
    p2 = multiprocessing.Process(target=proceso_hijo_dos)
    p3 = multiprocessing.Process(target=proceso_hijo_tres)
    
    p1.start()
    p2.start()
    p3.start()
    
    print(f"El proceso padre inicializo el primer proceso hijo de PID: {p1.pid}")
    print(f"El proceso padre inicializo el segundo proceso hijo de PID: {p2.pid}")
    print(f"El proceso padre inicializo el tercer proceso hijo de PID: {p3.pid}")
    
    p1.join()
    p2.join()
    p3.join()
    
    print("Procesos padre finalizados")
    
if __name__ == "__main__":
    main()