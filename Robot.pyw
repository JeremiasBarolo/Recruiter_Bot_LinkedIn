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
    Salir_No_Pasar = pag.locateOnScreen('Salir_No_Pasar.png', confidence=0.8)

    
    
    while keyboard.is_pressed('q') == False:
        
        if Boton_Seguir:
            pag.click(Boton_Seguir)
            time.sleep(0.5)
            Boton_Seguir = pag.locateOnScreen('Boton_Seguir.png', confidence=0.8)
            Recruiter()
        
        elif Conectar:
            Conectar = pag.locateOnScreen('Boton_conectar.png', confidence=0.8)
            pag.click(Conectar)
            time.sleep(1.5)
            Boton_Enviar = pag.locateOnScreen('Boton_Enviar.png', confidence=0.8)
            Salir_No_Pasar = pag.locateOnScreen('Salir_No_Pasar.png', confidence=0.8)
            

            if Boton_Enviar:    
                pag.click(Boton_Enviar)
                time.sleep(0.5)
                pag.scroll(-170)
                time.sleep(0.5)
                Recruiter()
                
            else:
                try:
                    for i in range(3):
                        pag.moveTo(Salir_No_Pasar)
                        pag.click()
                        time.sleep(0.5)
                        pag.scroll(-170)
                        Conectar = pag.locateOnScreen('Boton_conectar.png', confidence=0.8)
                except:
                    Boton_Siguente = pag.locateOnScreen('Boton_Siguiente.png', confidence=0.8)
                    pag.moveTo(Boton_Siguente)
                    time.sleep(2)
        

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




  









