#Simula una familia realizando tareas del hogar al mismo tiempo. Crea al
#menos tres hilos: uno para lavar los platos, otro para barrer el piso y otro para
#cocinar. Cada hilo debe imprimir mensajes indicando el inicio y fin de su tarea,
#simulando que cada una tarda un tiempo distinto (usa time.sleep). Asegúrate de
#que todas las tareas terminen antes de imprimir un mensaje final desde el hilo
#principal que diga "Todas las tareas han sido completadas".
import threading
import time 

def lavar_platos():
    print("Hilo lavar platos iniciado")
    time.sleep(1)
    print("Hilo lavar platos finalizado")
def barrer_piso():
    print("Hilo barrer piso iniciado")
    time.sleep(1.4)
    print("Hilo barrer piso finalizado")
def cocinar():
    print("Hilo cocinar iniciado")
    time.sleep(2)
    print("Hilo cocinar finalizado")

def main():

    t = threading.Thread(target=lavar_platos) 
    t.start()
    t.join()

    t1 = threading.Thread(target=barrer_piso)  
    t1.start()
    t1.join()

    t3 = threading.Thread(target=cocinar)
    t3.start()
    t3.join()

    print("Todos los hilos han finalizado")
    
if __name__ == "__main__":
    main()
