from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, IntVar, Radiobutton
from tkinter.font import Font

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\oscar\OneDrive\Escritorio\Diseño Nuevo\build\recursos\infoUserWindow")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()
window.geometry("1073x619")
window.configure(bg="#FFFFFF")
width = 1073
height = 619

#Centrar ventana
window.geometry(f"{width}x{height}+{window.winfo_screenwidth() // 2 - width // 2}+{window.winfo_screenheight() // 2 - height // 2}")
window.update_idletasks()
window.update_idletasks()
window.title("Registrar Usuario")

# Montserrat font
montserrat_font = Font(family="Montserrat", size=12)

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
    39.0,
    0.0,
    1034.0,
    619.0,
    fill="#FFFFFF",
    outline=""
)

# Entry 1
entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(635.0, 361.5, image=entry_image_1)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font=montserrat_font
)
entry_1.place(x=357.0, y=336.0, width=556.0, height=49.0)

canvas.create_text(
    233.0,
    350.0,
    anchor="nw",
    text="Matricula",
    fill="#000000",
    font=("Montserrat", 12, "bold")
)

# Entry 2
entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(635.0, 272.5, image=entry_image_2)
entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font=montserrat_font
)
entry_2.place(x=357.0, y=247.0, width=556.0, height=49.0)

canvas.create_text(
    233.0,
    259.0,
    anchor="nw",
    text="Apellidos ",
    fill="#000000",
    font=("Montserrat", 12, "bold")
)

# Entry 3
entry_image_3 = PhotoImage(file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(635.0, 187.5, image=entry_image_3)
entry_3 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font=montserrat_font
)
entry_3.place(x=357.0, y=162.0, width=556.0, height=49.0)

canvas.create_text(
    242.0,
    174.0,
    anchor="nw",
    text="Nombre",
    fill="#000000",
    font=("Montserrat", 12, "bold")
)


opcion = IntVar()

def puestoSeleccion():
    if opcion.get() == 1:
        print("Estudiante selected")
    elif opcion.get() == 2:
        print("Docente selected")
    elif opcion.get() == 3:
        print("Administrativo selected")

radiobutton1 = Radiobutton(window, text="Estudiante", variable=opcion, value=1, command=puestoSeleccion, font=("Montserrat", 12),bg="#FFFFFF")
radiobutton1.place(x=400, y=430, anchor="center")

radiobutton2 = Radiobutton(window, text="Docente", variable=opcion, value=2, command=puestoSeleccion, font=("Montserrat", 12), bg="#FFFFFF")
radiobutton2.place(x=530, y=430, anchor="center")

radiobutton3 = Radiobutton(window, text="Administrativo", variable=opcion, value=3, command=puestoSeleccion, font=("Montserrat", 12), bg="#FFFFFF")
radiobutton3.place(x=675, y=430, anchor="center")

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Btn Regresar"),
    relief="flat"
)
button_1.place(x=345.0, y=470.0, width=174.97361755371094, height=56.272727966308594)

button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Btn Guardar"),
    relief="flat"
)
button_2.place(x=750.0, y=470.0, width=174.97361755371094, height=56.272727966308594)

image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(136.0, 66.0, image=image_image_1)

image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(460.0, 66.0, image=image_image_2)

canvas.create_text(
    500.0,
    30.0,
    anchor="nw",
    text="Registrar Usuario",
    fill="#1E1E1E",
    font=("Montserrat", 32)
)

window.resizable(False, False)
window.mainloop()
