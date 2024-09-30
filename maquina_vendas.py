# cada estado = 0,25
# q0 = 0,00 | q1 = 0,25 | q2 = 0,50

Sigma = ['b','25','50','100'] # alfabeto
Q = [0,1,2,3,4,5,6,7,8] # conjunto de estados
q0 = 0 # estado inicial
estado_atual = q0

# tabela de transição de estados
delta = [[0, 1, 2, 4], #q0
         [1,2,3,5], #q1
         [2,3,4,6], #q2
         [3,4,5,7], #q3
         [4,5,6,8], #q4
         [5,6,7,8], #q5
         [6,7,8,8], #q6
         [7,8,8,8], #q7
         [0,8,8,8]] #q8


saida = [['n','n','n','n'], 
         ['n','n','n','n'], 
         ['n','n','n','n'], 
         ['n','n','n','n'], 
         ['n','n','n','n'], 
         ['n','n','n','t25'], 
         ['n','n','n','t50'], 
         ['n','n','t25','t75'], 
         ['r','t25','t50','t100']]

def g(estado_atual, entrada):
    #funcao de saida
    #retorna a saida de um estado com a proxima entrada
    return saida[estado_atual][Sigma.index(entrada)]

# função que executa o autômato
def f(estado_atual, entrada):
    #funcao de transicao de estados
    #retorna o proximo estado
    return delta[estado_atual][Sigma.index(entrada)]

rodando = True

while rodando:
    entrada = input("digite acao\n'b','25','50','100', 'q' para sair\n")
    if (entrada == 'q'):
        rodando = False
    else:
        print("saida com input -> ", g(estado_atual, entrada))
        estado_atual = f(estado_atual, entrada)
        print("estado atual = ", estado_atual)
