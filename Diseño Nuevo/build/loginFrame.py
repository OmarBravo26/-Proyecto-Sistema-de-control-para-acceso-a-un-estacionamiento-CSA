import subprocess
import tkinter
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\oscar\OneDrive\Escritorio\Diseño Nuevo\build\recursos\loginWindow")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1073x619")
width = 1073
height = 619
#Centrar ventana
window.geometry(f"{width}x{height}+{window.winfo_screenwidth() // 2 - width // 2}+{window.winfo_screenheight() // 2 - height // 2}")
window.update_idletasks()  # Asegura que la geometría de
window.update_idletasks()
window.configure(bg="#FFFFFF")
window.title("Login")



canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=619,
    width=1073,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
canvas.create_rectangle(
    0.0,
    0.0,
    1073.0,
    619.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    0.0,
    0.0,
    537.0,
    619.0,
    fill="#8CF1FF",
    outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    838.0,
    183.0,
    image=image_image_1
)

canvas.create_text(
    694.0,
    34.0,
    anchor="nw",
    text="BIENVENIDO",
    fill="#000000",
    font=("Montserrat", 32)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    839.0,
    341.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font=("Montserrat", 12)
)
entry_1.place(
    x=675.0,
    y=317.0,
    width=328.0,
    height=47.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    839.0,
    457.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font=("Montserrat", 12,),
    show=("*")
)
entry_2.place(
    x=675.0,
    y=432.0,
    width=328.0,
    height=48.0
)

canvas.create_text(
    659.0,
    276.0,
    anchor="nw",
    text="usuario:",
    fill="#000000",
    font=("Montserrat", 16)
)

canvas.create_text(
    655.0,
    391.0,
    anchor="nw",
    text="contraseña:",
    fill="#000000",
    font=("Montserrat", 16)
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    268.0,
    295.0,
    image=image_image_2
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))

def mostrarMonitoreo():
    subprocess.Popen(['python' ,'monitoreoFrame.py'])
    window.withdraw()

button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=mostrarMonitoreo,
    relief="flat"
)

button_1.place(
    x=751.3572998046875,
    y=511.9445495605469,
    width=174.97361755371094,
    height=56.272727966308594
)

window.resizable(False, False)
window.mainloop()
