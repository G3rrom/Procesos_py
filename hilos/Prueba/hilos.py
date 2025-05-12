#def: Parte de un proceso 
#Proceso: Independiente y tiene sus propios recursos
#Hilos: Tiene recursos compartidos y es una parte de un proceso
#Proceso: Mas seguro y consume mas recursos
#Hilos: Menos seguro y consume menos recursos


#Lanzar un hilo basico
import threading
def tarea():
    print("Hola desde el hilo") # Esta funcion se ejecutara en el hilo

def main():
    hilo = threading.Thread(target=tarea) # Crear un hilo
    hilo.start() # Iniciar el hilo
    hilo.join() # Esperar a que el hilo termine
    print("Hilo finalizado")

if __name__ == "__main__":
    main()