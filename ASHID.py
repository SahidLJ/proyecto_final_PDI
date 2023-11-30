import speech_recognition as sr
import tkinter as tk
from tkinter import filedialog


recognizer = sr.Recognizer()
recognizer.energy_threshold = 4000  


def seleccionar_audio():
    archivo_audio = filedialog.askopenfilename(filetypes=[("Archivos de audio", "*.wav")])
    if archivo_audio:
        resultado.config(state=tk.NORMAL)
        resultado.delete(1.0, tk.END)
        resultado.insert(tk.END, "Archivo de audio seleccionado: " + archivo_audio)
        resultado.config(state=tk.DISABLED)
        reconocer_audio(archivo_audio)


def reconocer_audio(archivo_audio):
    with sr.AudioFile(archivo_audio) as source:
       
        audio = recognizer.record(source)

        try:
            
            text = recognizer.recognize_google(audio, language="es-ES")
            resultado.config(state=tk.NORMAL)
            resultado.delete(1.0, tk.END)
            resultado.insert(tk.END, "Texto reconocido: \n" + text)
            resultado.config(state=tk.DISABLED)
        except sr.UnknownValueError:
            resultado.config(state=tk.NORMAL)
            resultado.delete(1.0, tk.END)
            resultado.insert(tk.END, "Google Speech Recognition no pudo entender el audio.")
            resultado.config(state=tk.DISABLED)
        except sr.RequestError as e:
            resultado.config(state=tk.NORMAL)
            resultado.delete(1.0, tk.END)
            resultado.insert(tk.END, "No se pudo solicitar resultados de Google Speech Recognition; {0}".format(e))
            resultado.config(state=tk.DISABLED)


ventana = tk.Tk()
ventana.title("Reconocimiento de Voz en Español")


resultado = tk.Text(ventana, height=10, width=60, state=tk.DISABLED)
resultado.pack()


boton_seleccionar = tk.Button(ventana, text="Seleccionar Audio", command=seleccionar_audio)
boton_seleccionar.pack()

ventana.mainloop()

