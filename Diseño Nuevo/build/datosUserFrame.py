from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter.font import Font
import subprocess

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\oscar\OneDrive\Escritorio\Diseño Nuevo\build\recursos\datosUserWindow")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()
window.geometry("1073x619")
window.configure(bg = "#FFFFFF")

width = 1073
height = 619
#Centrar ventana
window.geometry(f"{width}x{height}+{window.winfo_screenwidth() // 2 - width // 2}+{window.winfo_screenheight() // 2 - height // 2}")
window.update_idletasks()  # Asegura que la geometría de
window.update_idletasks()
window.title("Datos User")

monserratFont = Font(family="Montserrat", size=12)
monserratBlack = Font(family="Montserrat",size=12,weight="bold")

def actualizar():
    subprocess.Popen(['python','actualizarUserFrame.py'])
    window.withdraw()

def eliminar():
    subprocess.Popen(['python','datosUserFrame.py'])
    window.withdraw()

def aceptar():
    subprocess.Popen(['python','menuFrame.py'])
    window.withdraw()



canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 619,
    width = 1073,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    1073.0,
    619.0,
    fill="#8CF1FF",
    outline="")

canvas.create_rectangle(
    31.0,
    0.0,
    1026.0,
    619.0,
    fill="#FFFFFF",
    outline="")

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    586.5,
    370.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font=monserratBlack
)
entry_1.place(
    x=437.0,
    y=354.0,
    width=299.0,
    height=30.0
)

canvas.create_text(
    368.0,
    309.0,
    anchor="nw",
    text="Puesto",
    fill="#000000",
    font=monserratFont
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    586.5,
    318.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font=monserratBlack
)
entry_2.place(
    x=437.0,
    y=302.0,
    width=299.0,
    height=31.0
)

canvas.create_text(
    342.0,
    359.0,
    anchor="nw",
    text="Matricula",
    fill="#000000",
    font=monserratFont
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    588.0,
    266.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font=monserratBlack
)
entry_3.place(
    x=439.0,
    y=250.0,
    width=298.0,
    height=30.0
)

canvas.create_text(
    290.0,
    254.0,
    anchor="nw",
    text="Apellido Paterno",
    fill="#000000",
    font=monserratFont
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    588.0,
    213.0,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font=monserratBlack
)
entry_4.place(
    x=439.0,
    y=196.0,
    width=298.0,
    height=32.0
)

canvas.create_text(
    289.0,
    201.0,
    anchor="nw",
    text="Apellido Materno",
    fill="#000000",
    font=monserratFont
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    588.0,
    157.5,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font=monserratBlack
)
entry_5.place(
    x=439.0,
    y=142.0,
    width=298.0,
    height=29.0
)

canvas.create_text(
    360.0,
    146.0,
    anchor="nw",
    text="Nombre",
    fill="#000000",
    font=monserratFont
)

canvas.create_text(
    496.0,
    64.0,
    anchor="nw",
    text="Datos Usuario",
    fill="#000000",
    font=("Montserrat",32)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    127.0,
    69.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=261.0,
    y=440.0,
    width=173.0,
    height=44.266571044921875
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=actualizar, #actualizar
    relief="flat"
)
button_2.place(
    x=261.0,
    y=440.0,
    width=173.0,
    height=44.266571044921875
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=eliminar, #eliminar
    relief="flat"
)
button_3.place(
    x=711.0,
    y=440.0,
    width=173.0,
    height=44.266571044921875
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=aceptar, #Aceptar
    relief="flat"
)
button_4.place(
    x=483.0,
    y=440.0,
    width=173.0,
    height=44.266571044921875
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    460.0,
    97.0,
    image=image_image_2
)
window.resizable(False, False)
window.mainloop()
