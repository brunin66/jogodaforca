import tkinter as tk
import random
from palavras_jogo import palavras

#para o jogo funcionar, import o tkinter, random 
#importe o arquivo palavras_jogo

# Função para escolher uma palavra aleatória
def escolher_palavra():
    return random.choice(palavras)

# Inicializa a lista de letras escolhidas pelo usuário
letras_usuario = []
tentativas_usuario = []

# Configurações da janela
janela = tk.Tk()
janela.title("Jogo de Adivinhação")
janela.geometry("300x250")

# Variável para controlar as chances e a palavra
chances = 4
palavra = escolher_palavra()

# Função para reiniciar o jogo
def reiniciar_jogo():
    global chances, palavra, letras_usuario, tentativas_usuario
    chances = 4
    palavra = escolher_palavra()
    letras_usuario = []
    tentativas_usuario = []
    entrada.config(state=tk.NORMAL)
    botao.config(state=tk.NORMAL)
    entrada.delete(0, tk.END)  # Limpa a caixa de entrada
    resultado_label.config(text="")
    tentativas_label.config(text="Tentativas: ")
    chances_label.config(text=f"Chances restantes: {chances}")
    atualizar_palavra()

# Função para verificar a letra escolhida pelo usuário
def verificar_letra():
    global chances
    tentativa = entrada.get().lower()
    if not tentativa.isalpha() or len(tentativa) != 1:
        resultado_label.config(text="Por favor, insira uma única letra.")
        entrada.delete(0, tk.END)
        return

    if tentativa in tentativas_usuario:
        resultado_label.config(text="Você já tentou essa letra.")
    else:
        tentativas_usuario.append(tentativa)
        tentativas_label.config(text=f"Tentativas: {' '.join(tentativas_usuario)}")

        if tentativa not in palavra:
            resultado_label.config(text=f"Você errou! {tentativa} não está na palavra.")
            chances -= 1
            chances_label.config(text=f"Chances restantes: {chances}")
            if chances <= 0:
                resultado_label.config(text=f"Você perdeu! A palavra era: {palavra}")
                entrada.config(state=tk.DISABLED)  # Desativa a caixa de entrada
                botao.config(state=tk.DISABLED)    # Desativa o botão
        else:
            if tentativa not in letras_usuario:
                resultado_label.config(text=f"{tentativa} está na palavra!")
                letras_usuario.append(tentativa)  # Adiciona a letra à lista de letras adivinhadas
                atualizar_palavra()

    entrada.delete(0, tk.END)

# Função para atualizar a palavra exibida na interface
def atualizar_palavra():
    palavra_exibida = " "
    for letra in palavra:
        if letra in letras_usuario:
            palavra_exibida += letra + " "
        else:
            palavra_exibida += "_ "
    palavra_label.config(text=palavra_exibida)

    # Verifica se o jogador ganhou
    if all(letra in letras_usuario for letra in palavra):
        resultado_label.config(text=f"Parabéns, você ganhou! A palavra era: {palavra}")
        entrada.config(state=tk.DISABLED)  # Desativa a caixa de entrada
        botao.config(state=tk.DISABLED)    # Desativa o botão

# Widgets
palavra_label = tk.Label(janela, text="", font=("Arial", 19))
palavra_label.pack()

entrada = tk.Entry(janela)
entrada.pack()

botao = tk.Button(janela, text="Adivinhar", command=verificar_letra)
botao.pack()

resultado_label = tk.Label(janela, text="", font=("Arial", 9))
resultado_label.pack()

chances_label = tk.Label(janela, text=f"Chances restantes: {chances}", font=("Arial", 10))
chances_label.pack()

tentativas_label = tk.Label(janela, text="Tentativas: ", font=("Arial", 10))
tentativas_label.pack()

# Botão para jogar novamente
jogar_novamente_btn = tk.Button(janela, text="Jogar Novamente", command=reiniciar_jogo)
jogar_novamente_btn.pack()

# Menu
menu_bar = tk.Menu(janela)
janela.config(menu=menu_bar)

# Menu "Jogo"
jogo_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Jogo", menu=jogo_menu)
jogo_menu.add_command(label="Jogar Novamente", command=reiniciar_jogo)

# Inicia a interface
atualizar_palavra()
janela.mainloop()