from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter.font import Font


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\oscar\OneDrive\Escritorio\Diseño Nuevo\build\recursos\invitadoWindow")


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
window.title("Invitado")


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

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    588.5,
    436.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font=monserratBlack,
    show=("*")
)
entry_2.place(
    x=439.0,
    y=420.0,
    width=299.0,
    height=30.0
)

canvas.create_text(
    347.0,
    309.0,
    anchor="nw",
    text="Matricula",
    fill="#000000",
    font=monserratFont
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    586.5,
    318.5,
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
    x=437.0,
    y=302.0,
    width=299.0,
    height=31.0
)

canvas.create_text(
    238.0,
    359.0,
    anchor="nw",
    text="Justificación de Ingreso",
    fill="#000000",
    font=monserratFont
)

canvas.create_text(
    274.0,
    425.0,
    anchor="nw",
    text="Ingresa contraseña",
    fill="#FF0000",
    font=monserratFont
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    588.0,
    266.0,
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

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    588.0,
    213.0,
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

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    588.0,
    157.5,
    image=entry_image_6
)
entry_6 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font=monserratBlack
)
entry_6.place(
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
    45.0,
    anchor="nw",
    text="Invitado",
    fill="#000000",
    font=Font(family="Montserrat",size=32)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    467.0,
    75.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    127.0,
    69.0,
    image=image_image_2
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Btn Regresar"),
    relief="flat"
)
button_1.place(
    x=342.0,
    y=501.0,
    width=181.0,
    height=51.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Btn Guardar"),
    relief="flat"
)
button_2.place(
    x=654.0,
    y=502.0,
    width=173.0,
    height=44.266571044921875
)
window.resizable(False, False)
window.mainloop()
