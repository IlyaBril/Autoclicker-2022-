import time
import csv
from pynput import keyboard, mouse
from threading import Thread, Lock


lock = Lock()


def stop ():
    write_to ('stop')
    
def start ():      
    write_to ('start')

def write_to (action):
    initial_time = time.time()
    global stop_lis
    
    def writecsv(command, i=[0]):
        with open ('writescv.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            i[0] += 1
            command = command.replace('(',',').replace(')',',')
            action = []
            action = command.split(',')
            command = str(i[0])+',' + command + str(time.time() - initial_time)
            action.insert(0,i[0])
            print (command, file=f)
    

    def keyb_listening():
        global stop_lis      
        with keyboard.Events() as events:
            for event in events:
                result = writecsv(str(format(event)))
                if stop_lis is True:
                    
                    break


    def mouse_listening():
        global stop_lis
        with mouse.Events() as events:
            for event in events:
                result = writecsv(str(format(event)))
                if stop_lis is True:
                    
                    break
   
 
    if action == 'start':
        stop_lis = False
        #print('Action start  ',action)
        t = Thread(target=keyb_listening)
        q = Thread(target=mouse_listening)
        t.start()
        q.start()

    if action == 'stop':
        lock.acquire()
        stop_lis = True
        lock.release()
        #print ('else stop lis is True  ',stop_lis)
        
        
    
if __name__ == "__main__":
    main()







