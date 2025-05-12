import threading

def saludar(nombre):
    print(f"Hola {nombre} desde el hilo")
    print("Proceso finalizado")

def main():
    nom = input("Ingrese su nombre: ")
    hilo = threading.Thread(target=saludar, args=(nom, ))
    hilo.start()
    hilo.join()
    print("Hilo finalizado")
if __name__ == "__main__":
    main()