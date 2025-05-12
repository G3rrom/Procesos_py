import threading
lock = threading.Lock()
saldo = 100

def retirar_dinero(n):
    print(f"Hilo {n} retirando dinero inicializado")
    global saldo
    if saldo - 50 < 0:
        print("No hay suficiente dinero")
    else:
        for _ in range(50):
            with lock:
                saldo -= 1
        print(f"Retiro exitoso | saldo actual: {saldo}")
    print(f"Hilo {n} retirando dinero  finalizado")

def main():

    h = threading.Thread(target=retirar_dinero, args=(1,))
    h.start()
    h.join()

    h1 = threading.Thread(target=retirar_dinero, args=(2,))
    h1.start()
    h1.join()

    h2 = threading.Thread(target=retirar_dinero, args=(3,))
    h2.start()
    h2.join()

    print("Hilos finalizados")

if __name__ == "__main__":
    main()


