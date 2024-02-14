import tkinter as tk 
from tkinter import ttk 
import random

class SimuladorDadosApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Simulador de Dados")

        self.label_cantidad = ttk.Label(self.master, text="Cantidad de dados:")
        self.label_cantidad.grid(row=0, column=0, padx=5, pady=5)

        self.cantidad_entry = ttk.Entry(self.master, width=10)
        self.cantidad_entry.grid(row=0, column=1, padx=5, pady=5)

        self.label_caras = ttk.Label(self.master, text="Cantidad de caras:")
        self.label_caras.grid(row=1, column=0, padx=5, pady=5)

        self.caras_entry = ttk.Entry(self.master, width=10)
        self.caras_entry.grid(row=1, column=1, padx=5, pady=5)

        self.lanzar_button = ttk.Button(self.master, text="Lanzar", command=self.lanzar_dados)
        self.lanzar_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        self.resultados_label = ttk.Label(self.master, text="")
        self.resultados_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    def lanzar_dados(self):
        try:
            cantidad = int(self.cantidad_entry.get())
            caras = int(self.caras_entry.get())
            if cantidad <= 0 or caras <= 0:
                raise ValueError("La cantidad de dados y caras debe ser mayor que cero.")
            
            resultados = [random.randint(1, caras) for _ in range(cantidad)]
            resultados_texto = ", ".join(str(resultado) for resultado in resultados)
            self.resultados_label.config(text=f"Resultados: {resultados_texto}")
        except ValueError as e:
            self.resultados_label.comfig(text=str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = SimuladorDadosApp(root)
    root.mainloop()