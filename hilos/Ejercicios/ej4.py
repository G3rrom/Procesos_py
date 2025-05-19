import threading
import time 
import random

u = 0
t = random.uniform(0.5, 0.10)
lock = threading.Lock()

def servidor(nom, url):
    global u
    print("Servidor iniciado")
    with lock:
        print("Accediendo al servidor.")
        time.sleep(t)
        print(f"Usuario: {nom}")
        print(f"URL solicitada: {url}")
        time.sleep(t)
        print("Solicitud finalizada.")
        u += 1
        print(f"Total de usuarios atendidos {u}")
        time.sleep(t)
        print("Servidor cerrado.")

def main():

    t1 = threading.Thread(target=servidor, args=("Gere", 12345))
    t1.start()
    t1.join()

    t2 = threading.Thread(target=servidor, args=("Seba", 54321))
    t2.start()
    t2.join()

    t3 = threading.Thread(target=servidor, args=("Lucho", 19283))
    t3.start()
    t3.join()

    print("Hilo finalizado")

if __name__ == "__main__":
    main()



    