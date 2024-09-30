
import tkinter as tk

# Definições do autômato
Sigma = ['b', '25', '50', '100']  # alfabeto
Q = [0, 1, 2, 3, 4, 5, 6, 7, 8]  # conjunto de estados
q0 = 0  # estado inicial
estado_atual = q0  # estado inicial atual
troco = 0

# Tabela de transição de estados
delta = [[0, 1, 2, 4],  # q0
         [1, 2, 3, 5],  # q1
         [2, 3, 4, 6],  # q2
         [3, 4, 5, 7],  # q3
         [4, 5, 6, 8],  # q4
         [5, 6, 7, 8],  # q5
         [6, 7, 8, 8],  # q6
         [7, 8, 8, 8],  # q7
         [0, 8, 8, 8]]  # q8

saida = [['n', 'n', 'n', 'n'],
         ['n', 'n', 'n', 'n'],
         ['n', 'n', 'n', 'n'],
         ['n', 'n', 'n', 'n'],
         ['n', 'n', 'n', 'n'],
         ['n', 'n', 'n', 't25'],
         ['n', 'n', 'n', 't50'],
         ['n', 'n', 't25', 't75'],
         ['r', 't25', 't50', 't100']]

def g(estado_atual, entrada):
    # Função de saída
    # Retorna a saída de um estado com a próxima entrada
    return saida[estado_atual][Sigma.index(entrada)]

def f(estado_atual, entrada):
    # Função de transição de estados
    # Retorna o próximo estado com dada entrada
    return delta[estado_atual][Sigma.index(entrada)]

# Função para processar a entrada
def processa_input(entrada):
    global estado_atual
    global troco
    if entrada not in Sigma:
        output_text.set(f"Entrada: {entrada}\nERRO: Entrada não pertence ao alfabeto\nEstado Atual: {estado_atual}")
        return

    if entrada == 'b':
        if estado_atual == 8:
            output_text.set(f"Você retirou o refrigerante e recebeu o troco de R${troco}")
            troco = 0
            estado_atual = 0
            return  
        else:
            output_text.set(f"Saldo insuficiente (custo R$2,00)\nSaldo: R${estado_atual*0.25}\nTroco: R${troco}")
            return
        
    saida_atual = g(estado_atual, entrada)
    estado_atual = f(estado_atual, entrada)
    if 't' in saida_atual:
        troco = troco + int(saida_atual[1:])/100
    output_text.set(f"Entrada: {entrada}\nSaída: {saida_atual}\nEstado Atual: {estado_atual}\nSaldo: R${estado_atual*0.25}\nTroco: R${troco}")

# Função para finalizar o programa
def sair():
    root.quit()

# Configuração da interface gráfica
root = tk.Tk()
root.title("Máquina de vendas - AFD")

# Variável para armazenar o estado de saída
output_text = tk.StringVar()
output_text.set(f"Estado Inicial: {estado_atual}")

# Campo de texto para mostrar a saída
output_label = tk.Label(root, textvariable=output_text, height=4, width=50, padx=10, pady=10)
output_label.pack()

# Campo de entrada para digitar o valor
entry_field = tk.Entry(root)
entry_field.pack()

# Botão para processar a entrada 'b'
btn_b = tk.Button(root, text="Botão retirar", command=lambda: processa_input('b'))
btn_b.pack()

# Botão para processar o valor digitado
btn_custom = tk.Button(root, text="Entrada personalizada", command=lambda: processa_input(entry_field.get()))
btn_custom.pack()

# Botão para sair
btn_quit = tk.Button(root, text="Sair", command=sair)
btn_quit.pack()

# Iniciar a interface
root.mainloop()
