from tkinter import Tk, Canvas, Entry, Button, Label,Image,PhotoImage
from tkinter import filedialog
from pathlib import Path
from PIL import Image, ImageTk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\oscar\OneDrive\Escritorio\Diseño Nuevo\build\recursos\monitoreoWindow")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def seleccionarImagen():
    global imgSeleccionada
    imgSeleccionada = filedialog.askopenfilename()
    print("Imagen seleccionada:", imgSeleccionada)
    cargarImagen()

def cargarImagen():
    global imgSeleccionada, imgLabel, photo
    if imgSeleccionada:
        image = Image.open(imgSeleccionada)
        image = image.resize((300, 300))
        photo = ImageTk.PhotoImage(image)
        imgLabel.configure(image=photo)
        imgLabel.image = photo
        imgLabel.place(x=145, y=129)

window = Tk()
window.geometry("1073x619")
window.configure(bg="#FFFFFF")
window.title("Monitoreo")

#Centrar ventana
width = 1073
height = 619
window.geometry(f"{width}x{height}+{window.winfo_screenwidth() // 2 - width // 2}+{window.winfo_screenheight() // 2 - height // 2}")
window.update_idletasks()  # Asegura que la geometría de
window.update_idletasks()


imgSeleccionada = None
photo = None

buttonFont = ("Montserrat", 12)

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
    853.5,
    386.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font=("Montserrat",12,"bold")
)
entry_1.place(
    x=704.0,
    y=370.0,
    width=299.0,
    height=30.0
)

canvas.create_text(
    614.0,
    376.0,
    anchor="nw",
    text="Matricula",
    fill="#000000",
    font=("Montserrat", 12)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    853.5,
    334.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font=("Montserrat",12,"bold")
)
entry_2.place(
    x=704.0,
    y=318.0,
    width=299.0,
    height=31.0
)

canvas.create_text(
    634.0,
    321.0,
    anchor="nw",
    text="Puesto",
    fill="#000000",
    font=("Montserrat", 12)
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    855.0,
    282.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font=("Montserrat",12,"bold")
)
entry_3.place(
    x=706.0,
    y=266.0,
    width=298.0,
    height=30.0
)

canvas.create_text(
    557.0,
    270.0,
    anchor="nw",
    text="Apellido Paterno",
    fill="#000000",
    font=("Montserrat", 12)
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    855.0,
    229.0,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font=("Montserrat",12,"bold")
)
entry_4.place(
    x=706.0,
    y=212.0,
    width=298.0,
    height=32.0
)

canvas.create_text(
    556.0,
    217.0,
    anchor="nw",
    text="Apellido Materno",
    fill="#000000",
    font=("Montserrat", 12)
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    855.0,
    173.5,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font=("Montserrat",12,"bold")
)
entry_5.place(
    x=706.0,
    y=158.0,
    width=298.0,
    height=29.0
)

canvas.create_text(
    627.0,
    162.0,
    anchor="nw",
    text="Nombre",
    fill="#000000",
    font=("Montserrat", 12)
)

canvas.create_text(
    496.0,
    30.0,
    anchor="nw",
    text="Monitoreo",
    fill="#1E1E1E",
    font=("Montserrat", 32)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    464.0,
    61.0,
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
        command=lambda: print("Btn Salir"),
    relief="flat"
)
button_1.place(
    x=828.0,
    y=500.0,
    width=181.0,
    height=51.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Btn Menu"),
    relief="flat"
)
button_2.place(
    x=89.0,
    y=500.0,
    width=173.0,
    height=44.266571044921875
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Btn Invitado"),
    relief="flat"
)
button_3.place(
    x=450.0,
    y=500.0,
    width=173.0,
    height=44.266571044921875
)

canvas.create_rectangle(
    89.0,
    134.0,
    508.0,
    428.0,
    fill="#D9D9D9",
    outline="")
window.resizable(False, False)

button = Button(window, text="Seleccionar Imagen", command=seleccionarImagen, font=buttonFont)
button.pack()
button.place(x=765.0,y=422.0)

imgLabel = Label(window)

window.mainloop()

