import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
from pyautogui import *
import keyboard
from time import sleep
import cv2
import re
import pyperclip
from random import randint, random
from multiprocessing import Process
#import easyoc  r
win_r=[0]
percent=[0]
sleep(2)
datos={}
datos_completos={}
datos_completos_anterior={}
def copy_clipboard():
    hotkey('ctrl', 'c')
    sleep(0.01)
    dev=pyperclip.paste()
    if dev.find('.')>-1:
        dev=float(dev)
    else:
        dev=int(dev)
    return dev
rest=copy_clipboard()
datos_completos.update({'1':rest})
""" or y in range(2,42):
    press('tab')  
    rest=copy_clipboard()
    datos_completos.update({str(y):rest})
    sleep(0.2)
print(datos_completos)
for _ in range(40):
    hotkey('shift', 'tab')
    sleep(0.05) """
x=0
def mouse_move():
    bandera=True
    while True:
        sleep(0.01)
        if bandera==True:
            x1=randint(0,10)
            y1=randint(0,10)
            sleep(0.1)
            move(x1,y1)
            bandera=not bandera
        else:
            sleep(0.1)
            move(-x1,-y1)
            bandera=not bandera
        sleep(random()*3)
def scroll_mouse():
    bandera1=True
    while True:
        sleep(0.01)
        if bandera1==True:
            xy=randint(0,10)
            sleep(0.1)
            scroll(xy)
            bandera1=not bandera1
        else:
            sleep(0.1)
            scroll(-xy)
            bandera1=not bandera1
        sleep(random()*3)
if __name__ == '__main__':
    process1 = Process(target=mouse_move)
    process = Process(target=scroll_mouse)
    process1.start()
    process.start()
    while x<41:
        #rest=copy_clipboard()
        #datos_completos.update({str(x):rest})
        x+=1
        conteo=0
        flask=True
        for i in range(41):
            sleep(randint(1,3))
            screenshot('winrate.png',region=(539,569, 231, 45))
            screenshot('percent.png',region=(1019,569, 231, 45))
            img1 = cv2.imread('winrate.png')
            img2 = cv2.imread('percent.png')
            textos=[]
            textos.append(pytesseract.image_to_string(img1))
            textos.append(pytesseract.image_to_string(img2))
            s_w = [float(s_w) for s_w in re.findall(r'-?\d+\.?\d*', textos[0])]
            s_p = [float(s_p) for s_p in re.findall(r'-?\d+\.?\d*', textos[1])]
            conteo+=1
            try:
                if [y < s_w[0] for y in win_r][-1] and [yy < s_p[0] for yy in percent][-1]:
                    print(s_w,s_p,'Incremento',i,'Variable',x)
                    win_r.append(s_w[0])
                    percent.append(s_p[0])
                    conteo=0
                    datos.update({x:['+',i]})
                    for _ in range(x-1):
                        hotkey('shift', 'tab')
                        sleep(0.15)
                    flask=False
                    x=0
                    break
                if conteo >= 6:
                    for e in range(i):
                        press('down')
                        sleep(0.4)
                    break
            except:
                for e in range(i):
                    press('down')
                    sleep(0.4)
                break
            press('up')
            sleep(randint(3,4))

        conteo=0
        if flask:
            for i in range(40):
                sleep(randint(1,3))
                screenshot('winrate.png',region=(539,569, 231, 45))
                screenshot('percent.png',region=(1019,569, 231, 45))
                img1 = cv2.imread('winrate.png')
                img2 = cv2.imread('percent.png')
                textos=[]
                textos.append(pytesseract.image_to_string(img1))
                textos.append(pytesseract.image_to_string(img2))
                s_w = [float(s_w) for s_w in re.findall(r'-?\d+\.?\d*', textos[0])]
                s_p = [float(s_p) for s_p in re.findall(r'-?\d+\.?\d*', textos[1])]
                conteo+=1
                try:
                    if [x < s_w[0] for x in win_r][-1] and [x < s_p[0] for x in percent][-1]:
                        print(s_w,s_p,'Incremento:',-i,'Variable',x)
                        win_r.append(s_w[0])
                        percent.append(s_p[0])
                        conteo=0
                        datos.update({x:['-',i]})
                        for _ in range(x-1):
                            hotkey('shift', 'tab')
                            sleep(0.15)
                        flask=False
                        x=0
                        break
                    if conteo >= 6:
                        for e in range(i):
                            press('up')
                            sleep(0.4)
                        break
                except:
                    for e in range(i):
                        press('up')
                        sleep(0.4)
                    break
                press('down')
                sleep(randint(3,4))
        try:
            if datos[x][0] == '+':
                if type(datos_completos[str(x)])==int:
                    datos_completos[str(x)]=int(datos_completos[str(x)])+datos[x][1]
                else:
                    datos_completos[str(x)]=float(datos_completos[str(x)])+datos[x][1]*0.1
            elif datos[x][0] == '-':
                if type(datos_completos[str(x)])==int:
                    datos_completos[str(x)]=int(datos_completos[str(x)])-datos[x][1]
                else:
                    datos_completos[str(x)]=float(datos_completos[str(x)])-datos[x][1]*0.1
                """ for e in range(datos[x][1]):
                    press('down')
                    sleep(0.3)"""
        except:
            pass
        sleep(randint(1,4))
        if flask:
            press('tab')
        if datos_completos != datos_completos_anterior:
            datos_completos_anterior=datos_completos
            print(datos_completos)
    print(datos_completos)