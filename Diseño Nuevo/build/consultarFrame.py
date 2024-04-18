from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter.font import Font
import subprocess

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\oscar\OneDrive\Escritorio\Diseño Nuevo\build\recursos\consultarWindow")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def mostrarDatosUser():
    subprocess.Popen(['python', 'datosUserFrame.py'])
    window.withdraw()

window = Tk()

window.geometry("1073x619")
window.configure(bg = "#FFFFFF")

width = 1073
height = 619
#Centrar ventana
window.geometry(f"{width}x{height}+{window.winfo_screenwidth() // 2 - width // 2}+{window.winfo_screenheight() // 2 - height // 2}")
window.update_idletasks()  # Asegura que la geometría de
window.update_idletasks()
window.title("Consultar User")

monserratFont = Font(family="Montserrat", size=12)
monserratBlack = Font(family="Montserrat",size=12,weight="bold")

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
    39.0,
    0.0,
    1034.0,
    619.0,
    fill="#FFFFFF",
    outline="")

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    593.0,
    195.5,
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
    x=315.0,
    y=170.0,
    width=556.0,
    height=49.0
)

canvas.create_text(
    191.0,
    184.0,
    anchor="nw",
    text="Nombre",
    fill="#000000",
    font=monserratFont
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    598.0,
    284.5,
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
    x=320.0,
    y=259.0,
    width=556.0,
    height=49.0
)

canvas.create_text(
    196.0,
    273.0,
    anchor="nw",
    text="Apellidos",
    fill="#000000",
    font=monserratFont
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=mostrarDatosUser,
    relief="flat"
)
button_1.place(
    x=509.0,
    y=392.0,
    width=174.97361755371094,
    height=56.272727966308594
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    136.0,
    66.0,
    image=image_image_1
)

canvas.create_text(
    484.0,
    49.0,
    anchor="nw",
    text="Consultar Usuario",
    fill="#1E1E1E",
    font=("Montserrat",32)

)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    450.0,
    78.0,
    image=image_image_2
)
window.resizable(False, False)
window.mainloop()
