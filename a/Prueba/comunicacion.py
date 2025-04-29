import multiprocessing.process
import multiprocessing.queues
import os 
import multiprocessing

def proceso_hijo(q):
    q.put("Mesnaje desde el hijo")#Mandas por cola un mensaje
    q.put("Otro mensaje desde el hijo")
    
def main():
    print("Proceso padre")
    q = multiprocessing.Queue() #Creas una cola
    p = multiprocessing.Process(target= proceso_hijo, args={q,})
    
    p.start()
    
    print(q.get())#Lo corta y pega de la cola
    print(q.get())#Lo corta y pega de la cola
    
    p.join()
    
if __name__ == "__main__":
    main()