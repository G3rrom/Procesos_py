import os 
import time 
import multiprocessing

def proceso_hijo():
    print(f"Proceso hijo: PID = {os.getpid()}, padre = {os.getpid}")
    time.sleep(1)
    print("Proceso hijo finalizado.")

def main():
    print("Hola - ")
    print(f"Proceso padre: PID {os.getpid()}")
    
    p = multiprocessing.Process(target=proceso_hijo)
    p.start()
    
    print(f"Processo padre creo un hijo con PID = {p.pid}")
    
    p.join()
    
    print("Proceso padre")

if __name__ == "__main__":
    main()