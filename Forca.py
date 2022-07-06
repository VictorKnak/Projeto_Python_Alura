################################################################################################################################################################
# No Python existe a funcao '.find("")' que ela procura uma letra dentro de uma palavra e retorna a posicao dela, iniciando sempre no 0 para a primeira letra
# Quando uma letra que nao existe na palavra e procurada, ela retorna '-1'
# Ex: palavra = "banana"
#      palavra.find("b") -> Retorna 0
#      palavra.find("n") -> Retorna 2
#      palavra.find("z") -> Retorna -1
# Mas como a palavra "banana" tem dois "n", esta funcao tras somente a posicao do primeiro "n" achado pois ela percorre ate encontrar a letra desejada e retorna a posicao
# E para encontrar a posica das duas letras prescisa-se usar um loop em cima de cada letra
#
# O '.find' também aceita um segundo parâmetro, que define a partir de qual posição gostaríamos de começar
#  Ex: palavra = "aluracursos"
#      palavra.find("a",1)  #procurando "a" a partir da segunda posição
#      Retorna 4
#################################################################################################################################################################

# 'def' é usado para definir um modulo de uma função, para que ela possa ser chamada(importada) dentro de outras funcoes.
# Tudo dentro dela deve estar indentado para identificaro inicio e o final da funcao 
def jogar():

    print("***********************************")
    print("*** Bem vindo ao jogo de Forca! ***")
    print("***********************************")

    # Variavel com a palavra a ser descoberta
    palavra_secreta = "banana"

    # para criar uma lista(array) usa-se colchetes; 
    letras_acertadas = ["_","_","_","_","_","_"]

    # Variaveis de controle com operadores logicos, o valor logico colocado com a primera letra em maiuscula pois se trata de um valor;
    enforcou = False
    acertou = False

    print(letras_acertadas)

    # Enquanto nao enforcou e nao acertou, faca; se algum valor de variavel for True, sai fora do while;
    while(not enforcou and not acertou):

        # inicia a variável para a iteracao
        index = 0

        # 'input' pega os dados que o usuário digitou e coloca dentro da variável
        chute = input("Qual letra?")
        # variavel recebe ela mesma com a fucao 'strip' que retira os espeços em branco de uma palavra
        chute = chute.strip()

        # Inicio do 'for' para interar cada letra da palavra; a variavel do 'letra' no 'for' nao precisa ser inicializada antes, pode-se usa-la diretamente no loop
        for letra in palavra_secreta:
            
            # Valida se a letra da palavra é igual ao chute colocando a funcao 'upper' para deixar tudo em maiusculo e comparar
            if(chute.upper() == letra.upper()):

                # a medida que cada volta no loop ocorre, ele pega a proxima letra dentro da variavel escolhida e a iteracao com a posicao
                # ou seja, o loop roda em cada letra da paravra incrementando o index ate achar a condicao do 'if' e entrar nele imprimindo ambos. 
                #print("Encontrei a letra {} na posicao {}".format(chute, index))

                # Em uma lista, pode-se passar a posicao que o dado que voce quer se colocar o que irá receber, ou seja, passamos a posicao 'index' que é a posicao
                # e a posicao recebe a letra de comparacao que esta dentro da palavra
                letras_acertadas[index] = letra

            # Faz o incremento e coloca dentro da propria variavel para imprimir a posicao da letra
            index = index + 1

        # imprime a lista com as letras que foram 'acertadas', imprimindo o tamanho da palavra junto com as letras que ja foram descobertas
        print(letras_acertadas)

    print("Fim do jogo!")

    
if(__name__ == "__main__"):
    jogar()    