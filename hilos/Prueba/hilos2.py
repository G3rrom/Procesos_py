import threading

def mostrar_id(n):
    print(f"Hilo {n} Ejecutandose")

def main():
    hilos = []
    for i in range(3):
        t = threading.Thread(target=mostrar_id, args=(i,))
        t.start()
        hilos.append(t)
    for hilo in hilos:
        hilo.join()
        print(f"hilo {hilo} terminado")
if __name__ == "__main__":
    main()
