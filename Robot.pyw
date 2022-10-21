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


#<======================================Funcion Conectar=====================================================>
def Fun_conectar():
    Conectar = pag.locateOnScreen('assets/imgs/Boton_Conectar.png', confidence=0.8)
    pag.click(Conectar)
    time.sleep(0.5)
    Boton_Enviar = pag.locateOnScreen('assets/imgs/Boton_Enviar.png', confidence=0.8)
    Salir_No_Pasar = pag.locateOnScreen('assets/imgs/Salir_No_Pasar.png', confidence=0.8)

#<======================================Funcion Main=====================================================>

def Recruiter():
    
    def Parar():
        if keyboard.is_pressed('q'):
            return True

    Conectar = pag.locateOnScreen('assets/imgs/Boton_conectar.png', confidence=0.8)
    Boton_Siguente = pag.locateOnScreen('assets/imgs/Boton_Siguiente.png', confidence=0.8)
    Boton_Seguir = pag.locateOnScreen('assets/imgs/Boton_Seguir.png', confidence=0.8)
    Salir_No_Pasar = pag.locateOnScreen('assets/imgs/Salir_No_Pasar.png', confidence=0.8)
    Boton_Mensaje = pag.locateOnScreen('assets/imgs/Boton_Mensaje.png', confidence=0.8)
    
    
    
    
    
    while Parar() == False:
        
        #Seguir
        if Boton_Seguir:
            pag.click(Boton_Seguir)
            print('Siguiendo al reclutador...') 
            time.sleep(0.5)
            Boton_Seguir = pag.locateOnScreen('assets/imgs/Boton_Seguir.png', confidence=0.8)
            Recruiter()

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
                            Recruiter()
                            print('Resuleto :D')

                        else:
                            try:
                                for i in range(4):
                                    print('Intentando cambiar de Boton...')
                                    pag.click(Salir_No_Pasar)
                                    pag.scroll(-170)

                                    Recruiter()
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
                    Recruiter()

        #Siguiente
        elif Boton_Siguente:
            pag.click(Boton_Siguente)
            print('Cambiando de Pagina...')  
            time.sleep(2)
            Boton_Siguente = pag.locateOnScreen('assets/imgs/Boton_Siguiente.png', confidence=0.8)
            Recruiter()

        else:
            try:
                pag.scroll(-500)
                Recruiter()
            
            except:
                print('Haz alcanzado el limite semanal de seguimientos ;)')
                msg.showinfo('Terminado', 'Limite Semanal de Interacciones')
                break
    if failsafe:
        print('Hemos detenido el programa.')


#<===========================================Tkinter Window=====================================================>

def Instrucciones(event):
    instructions = (
        "https://github.com/JeremiasBarolo/Recruiter_Bot_LinkedIn")
    webbrowser.open_new_tab(instructions)

def Minimizar_Ejecutar():
    l = msg.askyesno('Iniciando el Programa', 'Desea iniciar el Bot?')
    if l != False:
        Recruiter()
        print('Iniciando Programa...')

def Detener_Programa():
    pag.moveTo(0,0)

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("assets/assets_tkinter")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("703x400")
window.configure(bg = "#FFFFFF")
window.title('Recruiter Bot')


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 400,
    width = 703,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    403.0,
    0.0,
    703.0,
    400.0,
    fill="#0A66C2",
    outline="")

canvas.create_text(
    24.0,
    36.0,
    anchor="nw",
    text="Recruiter Bot LinkedIn",
    fill="#000000",
    font=("Adamina Regular", 32 * -1)
)

canvas.create_text(
    34.0,
    82.0,
    anchor="nw",
    text="Por favor, leer las instrucciones.",
    fill="#000000",
    font=("Adamina", 16 * -1)
)

canvas.create_text(
    29.0,
    368.0,
    anchor="nw",
    text="¡Suerte en la busqueda, Developers!",
    fill="#000000",
    font=("Adamina", 12 * -1)
)

canvas.create_rectangle(
    27.0,
    76.0,
    386.0,
    79.0,
    fill="#0A66C2",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_instrucciones = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=Instrucciones,
    relief="flat"
)
button_instrucciones.place(
    
    x=506.0,
    y=214.0,
    width=104.0,
    height=39.0     
)
button_instrucciones.bind('<Button-1>', Instrucciones)
""" 
    x=506.0,
    y=272.0,
    width=104.0,
    height=40.0
"""

"""
button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_OPCIONES= Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)

button_OPCIONES.place(
    x=506.0,
    y=214.0,
    width=104.0,
    height=39.0
)
"""

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_DETENER = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=Detener_Programa,
    relief="flat"
)
button_DETENER.place(
    x=506.0,
    y=155.0,
    width=104.0,
    height=39.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_INICIAR = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=Minimizar_Ejecutar,
    relief="flat"
)

button_INICIAR.place(
    x=506.0,
    y=94.0,
    width=104.0,
    height=41.0
)
window.resizable(False, False)
window.mainloop()

  









