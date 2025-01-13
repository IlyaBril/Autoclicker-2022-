# from typing import Dict, List
import sys
from time import sleep
from threading import Thread, Lock
from pynput.mouse import Button, Controller
mouse = Controller()
from pynput.keyboard import Key, Controller
keyboard = Controller()
lock = Lock()


def Move(*args):
    global last_x
    x = args[0][0].strip()
    x = int(x[2:])
    y = args[0][1].strip()
    y = int(y[2:])
    last_x = x
    stop_from_mouse(last_x)
    mouse.position = (x, y)


def Click(*args):
    action = {' button=Button.left': 'left_button',
              ' button=Button.right': 'right_button',
              ' pressed=True': 'mouse.press',
              ' pressed=False': 'mouse.release'}
    press_release = (action[args[0][3]].strip())
    press_release = eval(press_release)
    side = action[args[0][2]].strip()
    
    def left_button():
        press_release(Button.left)
        

    def right_button():
        press_release(Button.right)
        
    f_name = eval(side)
    result = f_name()

def Press(*args):
    x = args[0][0].replace("key=","")
    action = "keyboard.press("+x+")"
    
    action = eval(action)
    
   
def Release(*args):
    x = args[0][0].replace("key=","")
    action = "keyboard.release("+x+")"
    action = eval(action)
    

# READ THE FILE
def execute():
    init_time = 0
    
    #stop_from_mouse_thread = Thread(target=stop_from_mouse)
    #stop_from_mouse_thread.start()
                                 
    with open('writescv.csv') as data:
        ignore = data.readline()
        action: dict[str, list[str]] = {}
        for line in data:
            test = line.strip().split(',')
            func_name = eval(test[1])
            args = test[2:]
            sleep_time = float(test[-1]) - init_time
            init_time = float(test[-1])
            #print (init_time)
            sleep (sleep_time)
            
            lock.acquire()
            func_name(args)
            lock.release()

def stop_from_mouse(last_x):   
    x = mouse.position
    difference = last_x - x[0]
    #print (difference)
    if difference > 100:
        print(difference)
        sys.exit(0)
   
         
      

if __name__=="__main__":
    execute()
