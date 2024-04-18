from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage
from tkinter.font import Font

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\oscar\OneDrive\Escritorio\Diseño Nuevo\build\recursos\menuWindow")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()

window.geometry("1073x619")
window.configure(bg="#FFFFFF")
width = 1073
height = 619
#Centrar ventana
window.geometry(f"{width}x{height}+{window.winfo_screenwidth() // 2 - width // 2}+{window.winfo_screenheight() // 2 - height // 2}")
window.update_idletasks()  # Asegura que la geometría de
window.update_idletasks()
window.title("Menu")

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
    fill="#8CF1FF",
    outline=""
)
canvas.create_rectangle(
    31.0,
    0.0,
    1026.0,
    619.0,
    fill="#FFFFFF",
    outline=""
)
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png")
)
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Btn Invitado"),
    relief="flat"
)
button_1.place(
    x=380.0,
    y=379.0,
    width=340.0,
    height=97.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png")
)
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Btn Consultar Usuario"),
    relief="flat"
)
button_2.place(
    x=380.0,
    y=244.0,
    width=340.0,
    height=97.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png")
)
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Btn Salir"),
    relief="flat"
)
button_3.place(
    x=471.0,
    y=515.0,
    width=174.97361755371094,
    height=56.272727966308594
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png")
)
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Btn Registrar Usuario"),
    relief="flat"
)
button_4.place(
    x=380.0,
    y=108.0,
    width=340.0,
    height=97.0
)

font = Font(family="Montserrat", size=32, weight="normal")
canvas.create_text(
    500.0,
    30.0,
    anchor="nw",
    text="Menu ",
    fill="#1E1E1E",
    font=font
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png")
)
image_1 = canvas.create_image(
    127.0,
    69.0,
    image=image_image_1
)
window.resizable(False, False)
window.mainloop()
