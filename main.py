import tkinter as tk
import random

def iniciar_jogo():
    global numero_secreto, tentativas
    numero_secreto = int(entry_numero_secreto.get())
    tentativas = 0
    frame_inicial.pack_forget()  # Esconde a tela inicial
    frame_jogo.pack(expand=True, fill='both')  # Mostra a tela do jogo

def verificar_palpite():
    palpite = int(entry_palpite.get())
    global tentativas
    tentativas += 1

    # Margem para considerar um palpite "próximo"
    margem_proxima = 10

    if palpite < numero_secreto:
        if numero_secreto - palpite <= margem_proxima:
            label_resultado.config(text="Você está perto! Tente um pouco mais alto.", fg="orange")
        else:
            label_resultado.config(text="Muito baixo! Tente novamente.", fg="blue")
    elif palpite > numero_secreto:
        if palpite - numero_secreto <= margem_proxima:
            label_resultado.config(text="Você está perto! Tente um pouco mais baixo.", fg="orange")
        else:
            label_resultado.config(text="Muito alto! Tente novamente.", fg="blue")
    else:
        label_resultado.config(text=f"Parabéns! Você acertou em {tentativas} tentativas.", fg="green")
        button_verificar.config(state="disabled")
        efeito_parabens()

def efeito_parabens():
    for _ in range(5):
        janela.config(bg=random.choice(["yellow", "light green", "light blue"]))
        janela.after(200)
    janela.config(bg="white")

def reiniciar_jogo():
    frame_jogo.pack_forget()
    frame_inicial.pack(expand=True, fill='both')
    label_resultado.config(text="")
    entry_palpite.delete(0, tk.END)
    entry_numero_secreto.delete(0, tk.END)
    button_verificar.config(state="normal")
    janela.config(bg="white")

# Criação da janela principal
janela = tk.Tk()
janela.title("Jogo de Adivinhação")

# Configuração da janela para permitir autoajuste
janela.geometry("300x200")  # Tamanho inicial, mas a janela pode ser redimensionada automaticamente

# Frame inicial (definição do número secreto)
frame_inicial = tk.Frame(janela)
label_instrucoes_inicial = tk.Label(frame_inicial, text="Defina o número secreto para adivinhar:")
label_instrucoes_inicial.pack(pady=10)

entry_numero_secreto = tk.Entry(frame_inicial)
entry_numero_secreto.pack(pady=5)

button_iniciar = tk.Button(frame_inicial, text="Iniciar Jogo", command=iniciar_jogo)
button_iniciar.pack(pady=10)

# Frame do jogo (tentativa de adivinhação)
frame_jogo = tk.Frame(janela)
label_instrucao = tk.Label(frame_jogo, text="Digite seu palpite:")
label_instrucao.pack(pady=10)

entry_palpite = tk.Entry(frame_jogo)
entry_palpite.pack(pady=5)

button_verificar = tk.Button(frame_jogo, text="Verificar", command=verificar_palpite)
button_verificar.pack(pady=10)

label_resultado = tk.Label(frame_jogo, text="")
label_resultado.pack(pady=5)

button_reiniciar = tk.Button(frame_jogo, text="Reiniciar Jogo", command=reiniciar_jogo)
button_reiniciar.pack(pady=10)

# Mostrar a tela inicial primeiro
frame_inicial.pack(expand=True, fill='both')

# Iniciar o loop principal
janela.mainloop()
