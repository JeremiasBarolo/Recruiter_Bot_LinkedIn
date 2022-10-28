import pyautogui as pag
import time
import keyboard
from mensaje import Mensaje
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import messagebox as msg
import webbrowser
from Robot import Ejecutar_Script

def Instrucciones(event):
    instructions = (
        "https://github.com/JeremiasBarolo/Recruiter_Bot_LinkedIn")
    webbrowser.open_new_tab(instructions)

def Ejecutar():
    l = msg.askyesno('Iniciando el Programa', 'Desea iniciar el Bot?')
    if l != False:
        print('Iniciando Programa...')
        Ejecutar_Script()
        

def Detener_Programa():
    exit()

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
    y=155.0,
    width=104.0,
    height=39.0 
)
button_instrucciones.bind('<Button-1>', Instrucciones)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_INICIAR = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=Ejecutar,
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