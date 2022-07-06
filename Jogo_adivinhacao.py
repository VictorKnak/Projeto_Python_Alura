############################################################################################################################################################################
#--------------------------------------------------------------------------|
# A IDENTACAO DEVE SER FEITA CORRETAMENTE, POIS SE NAO O PROGRAMA DA PAU!  |
#--------------------------------------------------------------------------|
# Identacao e feita com 4 espacos e usar 'snack_case' e nao 'camelCase'
#
# Lembrando que a funcao print automaticamente aplica um separador entre os valores. O separador e um espaÃƒÂ§o por padrao, mas pode ser reconfigurado pelo parametro sep:
# Exemplo: nome = "Nico"
#          sobrenome = "Steppat"
#          print(nome, sobrenome, sep="_")
#          Imprime Nico_Steppat 
#
# Mas caso nao tivese o sep definido e separado por somente virgula iria imprimir Nico Steppat 
# E caso fosse concatenado com "+" seria impresso NicoSteppat se nao tivesse o espaco entre as Strings
############################################################################################################################################################################

import random # Importa biblioteca para gerar numero aleatorios (entre 0.0 e 1.0)

# 'def' Ã© usado para definir um modulo de uma funÃ§Ã£o, para que ela possa ser chamada(importada) dentro de outras funcoes.
# Tudo dentro dela deve estar indentado para identificaro inicio e o final da funcao 
def jogar():

    print("***************************************")
    print("** Bem vindo ao jogo de Adivinhacao! **")
    print("***************************************")

    # Atribuicao de variavel

    # Multiplica por 100 para gerar um numero inteiro e usa o ROUND para arredondar o numero para cima ou para baixo
    #numero_secreto = round(random.random() *100) 

    # 'randrange' gera um numero entre os parametros passados menos 1 - (1 param 'inicio', 2 param 'fim - 1', 3 param pode escolher se gera numero par ou impar)
    numero_secreto = random.randrange(1,101)
    print(numero_secreto) # Somente para verificar se o numero esta sendo gerado

    # Inicia a variavel
    total_tentativas = 0 
    #rodada = 1  comentado pq o for nao precisa iniciar variavel
    pontos = 1000   # inicia varivavel de pontos

    print("Qual Ã© o nivel de dificuldade?")
    print("(1) Facil - (2) Medio - (3) Dificil")

    # Transforma o input em inteiro
    nivel = int(input("\nDefina o nivel: "))

    # Valida o tipo de nivel escolhido
    if (nivel == 1):
        total_tentativas = 20
    elif (nivel == 2):
        total_tentativas = 10
    elif (nivel == 3):
        total_tentativas = 5
    else:
        print("***********************************************")
        print("** Nivel invalido! Escolha um nivel correto! **")
        print("***********************************************")
                    

    # While nao executado enquando essa condicao for verdadeira 
    #while(rodada <= total_tentativas):
        # Exemplo String concatenada normal
        # print("\nTentativa", rodada, "de", total_tentativas)

    # for e executado com o a funcao range que e parametrizado com o primeiro parametro sendo o inicio e o segudo paramentro sendo te aonde ele vai(limite de repeticao) mas o segundo fica exclusivo e nao aparece
    # a variavel posta siginifica que o for rodara para a variavel declarada 'entre'(in) os valores parametrizados. Pode-se usar o terceiro parametro para informa se haver um 'step' => range(start, stop, [step]) pular 3em3 ou 2em2
    # foi somado +1 pois o ultimo numero no for fica exclusivo e nao aparece, entao para resolver e 'rodar' +1 vez
    for rodada in range(1,total_tentativas + 1):

        # Exemplo de String INTERPOLATION com a funcao "format" => PS: Lembrar de usar o ponto final (.) para finalizar a string e iniciar a funcao 'format'
        print("\nTentativa {} de {}".format(rodada, total_tentativas))

        # Input trava e execucao e o usuario preenche e aperta 'Enter' e sempre devolve como string
        chute_str = input("\nDigite um numero entre 1 e 100: ")  
        # Converte a string e numero inteiro
        chute_num = int(chute_str) 

        if(chute_num < 1 or chute_num > 100):
            print("\n===============================================")
            print("|  Voce deve digitar um numero entre 1 e 100  |")
            print("===============================================")
            print("------------> Tente novamente! <------------")
            continue # Para continuar a interacao do 'for'    

        # Declara as variaveis com o que cada uma recebe
        acertou = chute_num == numero_secreto
        maior   = chute_num >  numero_secreto
        menor   = chute_num <  numero_secreto 

        # Se declara a variavel apos o print para execucao, a virgula 'concatena' com a String
        print("\nVoce digitou: ", chute_str)  

        # Para comparar a igualdade e usado == e nao somente um igual e atribuicao de valor, a condicao tem que ficar entre parenteses apesar de funcionar sem e ':' marcar o fim da instrucao e inicio de um bloco 
        if(acertou): 

            # '\n' faz a quebra de linha dentro de uma String, mas lembrar de nao deixar espaco antes ou depois dela, pois a diferenca do espaco e impressa   
            print("\nVoce acertou e fez {} pontos!".format(pontos))
            print("===============") 
            # break sai do laco 'for'
            break 
        else:
            if(maior):
                print("\nVoce Errou! Seu chute foi maior que o numero secreto!")
                print("=======================================================")  
            # Elif seria mesmo que ElseIf       
            elif(menor):                                        
                print("\nVoce Errou! Seu chute foi menor que o numero secreto!")
                print("=======================================================")
            # calcular o numero secreto menos o chute; 'abs()' tras o numero absoluto, mesmo ele sendo negativo ira trazer positivo
            pontos_perdidos = abs(numero_secreto - chute_num)   

            # calcula os pontos que se tem menos os postos_perdidos e adiciona dentro da variavel pontos( decremento )
            pontos = pontos - pontos_perdidos     

        # A incrementacao e decrementacao sao realizadas na mesma identacao de todo processo dentro do 'while'
    # rodada = rodada + 1   comentado pq o 'for' ja faz a incrementacao; diferente do while que precisa incrementar 'manualmente'

    # Print fica na mesma identacao da funcao 'while' para informar que vem apos o termino do while       
    print("Fim do jogo!")

# Para acessar a funcao direto pelo terminal sem precisar acessar o "menu" do jogo.
# Quando rodamos diretamente um arquivo no Python, ele internamente cria uma variÃ¡vel e a preenche.
# E atravÃ©s dessa variÃ¡vel podemos fazer uma consulta, pois se ela estiver preenchida, significa que o arquivo foi executado diretamente, 
# mas se a variÃ¡vel nÃ£o estiver preenchida, entÃ£o significa que o arquivo sÃ³ foi importado.
# Essa variÃ¡vel Ã© a __name__, e ela Ã© preenchida com o valor __main__ caso o arquivo seja executado diretamente. 
if(__name__ == "__main__"):
    jogar()