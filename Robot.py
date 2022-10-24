import pyautogui as pag
import time
import keyboard
from Mensaje import Mensaje
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import messagebox as msg
import webbrowser

#<======================================Configuraciones=====================================================>
time.sleep(2)
failsafe = pag.FAILSAFE=True


def Ejecutar_Script():
    while keyboard.is_pressed('q') == False:
            Recruiter()
    print('Frenando el programa')

#<======================================Funcion Conectar=====================================================>
def Fun_conectar():
    Conectar = pag.locateOnScreen('assets/imgs/Boton_Conectar.png', confidence=0.8)
    pag.click(Conectar)
    time.sleep(0.5)
    Boton_Enviar = pag.locateOnScreen('assets/imgs/Boton_Enviar.png', confidence=0.8)
    Salir_No_Pasar = pag.locateOnScreen('assets/imgs/Salir_No_Pasar.png', confidence=0.8)

#<======================================Funcion Main=====================================================>
def Recruiter():
    Conectar = pag.locateOnScreen('assets/imgs/Boton_conectar.png', confidence=0.8)
    Boton_Siguente = pag.locateOnScreen('assets/imgs/Boton_Siguiente.png', confidence=0.8)
    Boton_Seguir = pag.locateOnScreen('assets/imgs/Boton_Seguir.png', confidence=0.8)
    Salir_No_Pasar = pag.locateOnScreen('assets/imgs/Salir_No_Pasar.png', confidence=0.8)
    Boton_Mensaje = pag.locateOnScreen('assets/imgs/Boton_Mensaje.png', confidence=0.8)
    
    
    
    
    
    while keyboard.is_pressed('q') == False:

        if keyboard.is_pressed('q') == True:
            break
            print('Frenando el programa')
            
        
        #Seguir
        if Boton_Seguir:
            pag.click(Boton_Seguir)
            print('Siguiendo al reclutador...') 
            time.sleep(0.5)
            Boton_Seguir = pag.locateOnScreen('assets/imgs/Boton_Seguir.png', confidence=0.8)
            Ejecutar_Script()

        #Conectar
        elif Conectar:
            #Por si no puede encontrar un conectar real.
                try:
                    
                        print('Conectando con el reclutador...'  )
                        for i in range(3):
                            Fun_conectar()
                        Boton_Enviar = pag.locateOnScreen('assets/imgs/Boton_Enviar.png', confidence=0.8)
                        Multiple_Choise = pag.locateOnScreen('assets/imgs/multiple_choise.png', confidence=0.8)
                        Salir_No_Pasar = pag.locateOnScreen('assets/imgs/Salir_No_Pasar.png', confidence=0.8)
                
                        #Enviar
                        if Boton_Enviar:
                            print('Enviado :D')  
                            pag.click(Boton_Enviar)
                            time.sleep(0.5)
                            Limite_Semanal = pag.locateOnScreen('assets/imgs/Limite_Semanal.png', confidence=0.8)

                            if Limite_Semanal:
                                print('Haz alcanzado el limite semanal de seguimientos ;)')
                                msg.showinfo('Terminado', 'Limite Semanal de Interacciones')
                                break
                            
                            else:
                                pag.scroll(-170)
                                time.sleep(1)

                        


                        #Multiple Choise
                        elif Multiple_Choise:
                            print('Resolviendo MultipleChoise...')  
                            Other_Button = pag.locateOnScreen('assets/imgs/other.png', confidence=0.8)
                            pag.click(Other_Button)
                            time.sleep(0.1)
                            Inside_Conectar = pag.locateOnScreen('assets/imgs/Inside_Conectar_Button.png')
                            pag.click(Inside_Conectar)
                            time.sleep(0.1)
                            Boton_Enviar = pag.locateOnScreen('assets/imgs/Boton_Enviar.png', confidence=0.8)
                            pag.click(Boton_Enviar)
                            Ejecutar_Script()
                            print('Resuleto :D')

                        else:
                            try:
                                for i in range(4):
                                    print('Intentando cambiar de Boton...')
                                    pag.click(Salir_No_Pasar)
                                    pag.scroll(-170)

                                    Ejecutar_Script()
                            except:
                                pag.scroll(-170)
                                Boton_Siguente = pag.locateOnScreen('assets/imgs/Boton_Siguiente.png', confidence=0.8)
                                pag.click(Boton_Siguente)
                                print('Cambiando de Pagina...')  
                except:
                    pag.scroll(-500)
                    Boton_Siguente = pag.locateOnScreen('assets/imgs/Boton_Siguiente.png', confidence=0.8)
                    pag.click(Boton_Siguente)
                    print('Cambiando de Pagina...')  
                    time.sleep(1.5)
                    Ejecutar_Script()

        #Siguiente
        elif Boton_Siguente:
            pag.click(Boton_Siguente)
            print('Cambiando de Pagina...')  
            time.sleep(2)
            Boton_Siguente = pag.locateOnScreen('assets/imgs/Boton_Siguiente.png', confidence=0.8)
            Ejecutar_Script()

        else:
            try:
                pag.scroll(-500)
                Ejecutar_Script()
            
            except:
                print('Haz alcanzado el limite semanal de seguimientos ;)')
                msg.showinfo('Terminado', 'Limite Semanal de Interacciones')
                break
    if failsafe:
        print('Hemos detenido el programa.')


  









