import tkinter as tk
import random
import time

# Lista para armazenar os números sorteados
numeros_sorteados = []

def sortear_numero():
    # Gerar um número aleatório entre 1 e 100
    numero = random.randint(1, 100)
    numeros_sorteados.append(numero)
    # Atualizar o label com o número sorteado
    label_numero.config(text=str(numero))
    # Atualizar a interface
    root.update()
    # Aguardar 2 segundos
    time.sleep(2)
    # Resetar o label
    label_numero.config(text="")
    # Atualizar a interface
    root.update()

# Configuração da interface
root = tk.Tk()
root.title("Sorteio Aleatório")

# Criação do label para exibir o número sorteado
label_numero = tk.Label(root, text="", font=("Helvetica", 48))
label_numero.pack(pady=20)

# Criação do botão de sorteio
botao_sortear = tk.Button(root, text="Sortear", command=sortear_numero, font=("Helvetica", 24))
botao_sortear.pack(pady=20)

# Execução da interface
root.mainloop()
