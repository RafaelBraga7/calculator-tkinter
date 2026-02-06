import tkinter as tk
import re


class Calculadora:

    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.title("Calculadora")
        self.raiz.geometry("330x440")
        self.raiz.resizable(False, False)

        self.expressao = ""

        self.raiz.grid_rowconfigure(0, weight=0)
        self.raiz.grid_rowconfigure(1, weight=1)
        self.raiz.grid_columnconfigure(0, weight=1)

        self.display = tk.Entry(
            self.raiz,
            font=("Arial", 22),
            bd=10,
            relief=tk.RIDGE,
            justify="right"
        )
        self.display.grid(row=0, column=0, sticky="nsew", padx=8, pady=(8, 6), ipady=10)

        self.frame_botoes = tk.Frame(self.raiz)
        self.frame_botoes.grid(row=1, column=0, sticky="nsew", padx=8, pady=(0, 8))

        for linha in range(5):
            self.frame_botoes.grid_rowconfigure(linha, weight=1)
        for coluna in range(4):
            self.frame_botoes.grid_columnconfigure(coluna, weight=1)

        self.criar_botoes()
        self.vincular_teclado()

    # INTERFACE
    def criar_botoes(self):

        layout = [
            ["C", "←", "(", ")"],
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "=", "+"],
        ]

        for linha, valores in enumerate(layout):
            for coluna, texto in enumerate(valores):
                botao = tk.Button(
                    self.frame_botoes,
                    text=texto,
                    font=("Arial", 16),
                    command=lambda valor=texto: self.ao_clicar(valor)
                )
                botao.grid(row=linha, column=coluna, sticky="nsew", padx=5, pady=5, ipady=8)

    def vincular_teclado(self):
        self.display.focus_set()

        self.raiz.bind("<Return>", lambda e: self.calcular())
        self.raiz.bind("<KP_Enter>", lambda e: self.calcular())
        self.raiz.bind("<BackSpace>", lambda e: self.apagar_ultimo())
        self.raiz.bind("<Escape>", lambda e: self.limpar())
        self.raiz.bind("<Key>", self.ao_digitar)

    def ao_clicar(self, valor):

        if valor == "=":
            self.calcular()
        elif valor == "C":
            self.limpar()
        elif valor == "←":
            self.apagar_ultimo()
        else:
            self.adicionar_expressao(valor)

    def ao_digitar(self, evento):

        teclas_permitidas = "0123456789.+-*/()"

        if evento.char in teclas_permitidas:
            self.adicionar_expressao(evento.char)
            return "break"

    def adicionar_expressao(self, valor):

        operadores = "+-*/"

        if valor in operadores and self.expressao:
            if self.expressao[-1] in operadores:
                self.expressao = self.expressao[:-1] + valor
                self.atualizar_display()
                return

        self.expressao += str(valor)
        self.atualizar_display()

    def atualizar_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.expressao)

    def limpar(self):
        self.expressao = ""
        self.atualizar_display()

    def apagar_ultimo(self):
        if self.expressao:
            self.expressao = self.expressao[:-1]
            self.atualizar_display()

    def calcular(self):

        if not self.expressao.strip():
            return

        try:
            if not re.fullmatch(r"[0-9\.\+\-\*\/\(\)\s]+", self.expressao):
                raise ValueError("Expressão inválida")

            resultado = eval(self.expressao, {"__builtins__": None}, {})
            self.expressao = str(resultado)
            self.atualizar_display()

        except:
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "Erro")
            self.expressao = ""


if __name__ == "__main__":
    raiz = tk.Tk()
    app = Calculadora(raiz)
    raiz.mainloop()
