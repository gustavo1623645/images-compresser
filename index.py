"""
import random

def adivina_numero(x):
    print("===================================================")
    print("              BIENVENIDO AL JUEGO                 ")
    print("===================================================")
    print(f"La meta es adivinar el numero aleatorio de 1 a {x}")

    aleatorio=random.randint(1,x)
    prediccion=0
    intentos=0

    while prediccion != aleatorio:
        prediccion=int(input("ingrese su prediccion: "))
        if prediccion > aleatorio:
            print("el numero es menor al que ingresaste")
            intentos+=1
        elif prediccion < aleatorio:
            print("el numero es mayor al que ingresaste")
            intentos+=1
        elif  prediccion == aleatorio: 
            print (f" ganaste el numero a adivinar era {aleatorio}")  
            intentos+=1

    print(f"intentos: {intentos}")                 

    
   

adivina_numero(1000)
"""
"""
from PIL import Image
import os

downloadsFolder = "C:/Users/vale/Downloads/nunca/"

picturesFolder = "C:/Users/vale/Downloads/nunca/nueva/"

if __name__ == "__main__":
    for filename in os.listdir(downloadsFolder):
        name, extension = os.path.splitext(downloadsFolder + filename)

        if extension in [".jpg", ".jpeg", ".png"]:
            picture = Image.open(downloadsFolder + filename)
            picture.save(picturesFolder + "compressed_"+filename+".webp", optimize=True, quality=60)
            os.remove(downloadsFolder + filename)
            print(name + ": " + extension)

        if extension in [".mp3"]:
            musicFolder = "/Users/nicolasschurmann/Music/"
            os.rename(downloadsFolder + filename, musicFolder + filename)
"""


"""

from PIL import Image
import os

parent_folder = "C:/Users/vale/Downloads/SUN/"

if __name__ == "__main__":
    for root, dirs, files in os.walk(parent_folder):
        for name in files:
            filepath = os.path.join(root, name)
            filename, extension = os.path.splitext(filepath)

            if extension in [".jpg", ".jpeg", ".png"]:
                picture = Image.open(filepath)
                compressed_filename = filename + "_compressed.webp"
                picture.save(compressed_filename, optimize=True, quality=60)
                  

                print(f"Imagen comprimida y guardada en {compressed_filename}")"""

from tkinter import Tk, Button, Label, filedialog, StringVar, Entry
from PIL import Image
import os

def select_folder():
    folder_path = filedialog.askdirectory()
    folder_entry.delete(0, "end")
    folder_entry.insert(0, folder_path)

def compress_images():
    folder_path = folder_entry.get()
    format_selected = format_var.get()

    for root, dirs, files in os.walk(folder_path):
        for name in files:
            filepath = os.path.join(root, name)
            filename, extension = os.path.splitext(filepath)

            if extension.lower() in [".jpg", ".jpeg", ".png"]:
                picture = Image.open(filepath)
                compressed_filename = filename + "_compressed." + format_selected
                picture.save(compressed_filename, optimize=True, quality=60)

                status_label.config(text=f"Imagen comprimida y guardada en {compressed_filename}")

# Crear la ventana principal
window = Tk()
window.title("Compresor de Imágenes")
window.geometry("400x200")

# Etiqueta y campo de entrada para la carpeta
folder_label = Label(window, text="Carpeta:")
folder_label.pack()

folder_entry = Entry(window, width=30)
folder_entry.pack()

folder_button = Button(window, text="Seleccionar carpeta", command=select_folder)
folder_button.pack()

# Etiqueta y campo de entrada para el formato
format_label = Label(window, text="Formato:")
format_label.pack()

format_var = StringVar()
format_entry = Entry(window, textvariable=format_var)
format_entry.pack()

# Botón para iniciar la compresión
compress_button = Button(window, text="Comprimir Imágenes", command=compress_images)
compress_button.pack()

# Etiqueta de estado
status_label = Label(window, text="")
status_label.pack()

# Iniciar el bucle principal de la ventana
window.mainloop()



