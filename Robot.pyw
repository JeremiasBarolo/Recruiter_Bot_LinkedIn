import multiprocessing
import pyautogui as pag
import time
import keyboard


#<======================================Configuraciones=====================================================>
time.sleep(2)
pag.FAILSAFE=True



#<======================================Funciones=====================================================>
def Fun_conectar():
    Conectar = pag.locateOnScreen('assets/imgs/Boton_Conectar.png', confidence=0.8)
    pag.click(Conectar)
    time.sleep(1.5)
    Boton_Enviar = pag.locateOnScreen('assets/imgs/Boton_Enviar.png', confidence=0.8)
    Salir_No_Pasar = pag.locateOnScreen('assets/imgs/Salir_No_Pasar.png', confidence=0.8)

def Recruiter():
    Conectar = pag.locateOnScreen('assets/imgs/Boton_conectar.png', confidence=0.8)
    Boton_Siguente = pag.locateOnScreen('assets/imgs/Boton_Siguiente.png', confidence=0.8)
    Boton_Seguir = pag.locateOnScreen('assets/imgs/Boton_Seguir.png', confidence=0.8)
    Salir_No_Pasar = pag.locateOnScreen('assets/imgs/Salir_No_Pasar.png', confidence=0.8)
    

    
    
    while keyboard.is_pressed('q') == False:
        
        #Seguir
        if Boton_Seguir:
            pag.click(Boton_Seguir)
            time.sleep(0.5)
            Boton_Seguir = pag.locateOnScreen('assets/imgs/Boton_Seguir.png', confidence=0.8)
            Recruiter()

        #Conectar
        elif Conectar:
            Fun_conectar()
            Boton_Enviar = pag.locateOnScreen('assets/imgs/Boton_Enviar.png', confidence=0.8)
            Multiple_Choise = pag.locateOnScreen('assets/imgs/multiple_choise.png', confidence=0.8)
            Salir_No_Pasar = pag.locateOnScreen('assets/imgs/Salir_No_Pasar.png', confidence=0.8)
            
            #Enviar
            if Boton_Enviar:    
                pag.click(Boton_Enviar)
                time.sleep(0.5)
                pag.scroll(-170)
                time.sleep(0.5)
                Recruiter()
            #Multiple Choise
            elif Multiple_Choise:
                Other_Button = pag.locateOnScreen('assets/imgs/other.png', confidence=0.8)
                pag.click(Other_Button)
                time.sleep(0.1)
                Inside_Conectar = pag.locateOnScreen('assets/imgs/Inside_Conectar_Button.png')
                pag.click(Inside_Conectar)
                time.sleep(0.1)
                Boton_Enviar = pag.locateOnScreen('assets/imgs/Boton_Enviar.png', confidence=0.8)
                pag.click(Boton_Enviar)
                Recruiter()
  
            else:
                try:
                    for i in range(4):
                        pag.click(Salir_No_Pasar)
                        pag.scroll(-170)
                        Recruiter()
                except:
                    pag.scroll(-170)
                    Boton_Siguente = pag.locateOnScreen('assets/imgs/Boton_Siguiente.png', confidence=0.8)
                    pag.click(Boton_Siguente)



        #Siguiente
        elif Boton_Siguente:
            pag.click(Boton_Siguente)
            time.sleep(2)
            Boton_Siguente = pag.locateOnScreen('assets/imgs/Boton_Siguiente.png', confidence=0.8)
            Recruiter()
            
            
        
        else:
            try:
                pag.scroll(-500)
                Recruiter()
            
            except:
                print('Debera Reiniciar el programa.')
                pag.moveTo(0,0)
                break
        
 
          
#<======================================Invocamos el Programa=====================================================>
Recruiter()

print('Terminado')



  









