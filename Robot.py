import pyautogui as pag
import time
import keyboard
from mensaje import Mensaje
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import messagebox as msg
import webbrowser

#<======================================Configuraciones=====================================================>
time.sleep(2)
pag.FAILSAFE=True

#<======================================Funcion Seguir Adelante =====================================================>
def Seguir_Adelante():
    if keyboard.is_pressed('q')== False:
        Ejecutar_Script()
        print('Ejecutando Script')

#<======================================Funcion Ejecutar=====================================================>
def Ejecutar_Script():
    try:
        if keyboard.is_pressed('q') == False:
            Recruiter()
        elif keyboard.is_pressed('q') == True:
            print('Programa detenido por la Q')
            exit()

    except ValueError as e:
        print('Error:', e)

#<======================================Funcion Conectar=====================================================>
def Fun_conectar():
    Conectar = pag.locateOnScreen('assets/imgs/Boton_Conectar.png', confidence=0.8)
    pag.click(Conectar)
    time.sleep(0.3)
    Boton_Enviar = pag.locateOnScreen('assets/imgs/Boton_Enviar.png', confidence=0.8)
    Salir_No_Pasar = pag.locateOnScreen('assets/imgs/Salir_No_Pasar.png', confidence=0.8)
    Multiple_Choise = pag.locateOnScreen('assets/imgs/multiple_choise.png', confidence=0.8)
    
                
    #Enviar
    if Boton_Enviar:
        pag.click(Boton_Enviar)
        time.sleep(0.2)
        Limite_Semanal = pag.locateOnScreen('assets/imgs/Limite_Semanal.png', confidence=0.8)
        print('Enviado :D')  


        if Limite_Semanal:
            print('Haz alcanzado el limite semanal de seguimientos ;)')
            msg.showinfo('Terminado', 'Limite Semanal de Interacciones')
            
        #Multiple Choise
        if Multiple_Choise:
            print('Resolviendo MultipleChoise...')  
            Other_Button = pag.locateOnScreen('assets/imgs/other.png', confidence=0.8)
            pag.click(Other_Button)
            time.sleep(0.1)
            Inside_Conectar = pag.locateOnScreen('assets/imgs/Inside_Conectar_Button.png')
            pag.click(Inside_Conectar)
            time.sleep(0.1)
            Boton_Enviar = pag.locateOnScreen('assets/imgs/Boton_Enviar.png', confidence=0.8)
            pag.click(Boton_Enviar)
            Seguir_Adelante()

        else: #Si no reconoce que hacer...
            print('No reconoce que hacer...')
            pag.scroll(-100)
            Seguir_Adelante()
            

#<======================================Funcion Main=====================================================>
def Recruiter():
    Conectar = pag.locateOnScreen('assets/imgs/Boton_conectar.png', confidence=0.8)
    Boton_Siguente = pag.locateOnScreen('assets/imgs/Boton_Siguiente.png', confidence=0.8)
    Boton_Seguir = pag.locateOnScreen('assets/imgs/Boton_Seguir.png', confidence=0.8)
            
    #Seguir
    if Boton_Seguir:
            pag.click(Boton_Seguir)
            print('Siguiendo al reclutador...')
            pag.scroll(-170) 
            time.sleep(0.5)
            Boton_Seguir = pag.locateOnScreen('assets/imgs/Boton_Seguir.png', confidence=0.8)
            Seguir_Adelante()

    #Conectar
    elif Conectar:
        #Por si no puede encontrar un conectar real.
            try:
                print('Conectando con el reclutador...'  )
                Conectar = pag.locateOnScreen('assets/imgs/Boton_conectar.png', confidence=0.8)
                Fun_conectar()    
            except:
                pag.scroll(-500)
                Boton_Siguente = pag.locateOnScreen('assets/imgs/Boton_Siguiente.png', confidence=0.8)
                pag.click(Boton_Siguente)
                print('No se reconocio otro conectar...') 
                print('Cambiando de pag...')  
                time.sleep(1.5)
                Seguir_Adelante()

    #Siguiente
    elif Boton_Siguente:
        pag.click(Boton_Siguente)
        print('Cambiando de Pagina...')  
        time.sleep(2)
        Boton_Siguente = pag.locateOnScreen('assets/imgs/Boton_Siguiente.png', confidence=0.8)
        Seguir_Adelante()

    
    else:
        try:
            pag.scroll(-500)
            Seguir_Adelante()
            
        except:
            print('Programa termiando')
            msg.showinfo('Terminado', 'Programa terminado')
            
    
