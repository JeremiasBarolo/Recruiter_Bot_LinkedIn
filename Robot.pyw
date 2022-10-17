import pyautogui as pag
import time
import keyboard

time.sleep(2)


pag.FAILSAFE=True


def Enviar():
    pag.click(x=1178,y=315)


#print(pag.displayMousePosition())

def Recruiter():
    Conectar = pag.locateOnScreen('Boton_conectar.png', confidence=0.8)
    Boton_Siguente = pag.locateOnScreen('Boton_Siguiente.png', confidence=0.8)
    Boton_Seguir = pag.locateOnScreen('Boton_Seguir.png', confidence=0.8)
    No_Pasar = pag.locateOnScreen('No_Pasar.png', confidence=0.8)
    
    while keyboard.is_pressed('q') == False:
        
        if Boton_Seguir:
            pag.click(Boton_Seguir)
            time.sleep(0.5)
            Boton_Seguir = pag.locateOnScreen('Boton_Seguir.png', confidence=0.8)
            Recruiter()
        
        elif Conectar:
            Conectar = pag.locateOnScreen('Boton_conectar.png', confidence=0.8)
            pag.click(Conectar)
            time.sleep(0.5)

            if No_Pasar:
                pag.click(200, 200)
                pag.scroll(-170)
                Conectar = pag.locateOnScreen('Boton_conectar.png', confidence=0.8)
                Recruiter()
        
            else:
                Enviar()
                time.sleep(0.5)
                pag.scroll(-170)
                time.sleep(0.5)
                Recruiter()
        

        elif Boton_Siguente:
            pag.click(Boton_Siguente)
            time.sleep(2)
            Boton_Siguente = pag.locateOnScreen('Boton_Siguiente.png', confidence=0.8)
            Recruiter()
            
            
        
        else:
            try:
                pag.scroll(-500)
                Recruiter()
            
            except:
                print('Debera Reiniciar el programa.')
                pag.moveTo(0,0)
                break
        
       
            
#Invocamos el Programa
Recruiter()

print('Terminado')




  









