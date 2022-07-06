
# Importa os modulos das funcoes criadas em outros processos, para executa-las posteriormente
import Forca
import Jogo_adivinhacao

def escolhe_jogo():

    print("***********************************")
    print("****** Escolha um dos jogos! ******")
    print("***********************************")

    print("(1) Forca - (2) Adivinhação")

    jogo = int(input("\nQual é o jogo? "))

    if(jogo == 1):
        print("\nJogo de Forca selecionado com sucesso!")
        print("//////////////////////////////////////\n")
        Forca.jogar()  # Executa os modulos das funcoes criadas em outros processos passando o nome do arquivo referente ao nome da funcao criada dentro dele
    elif(jogo == 2):
        print("\nJogo de Adivinhação selecionado com sucesso!")
        print("////////////////////////////////////////////\n")
        Jogo_adivinhacao.jogar()  # Executa os modulos das funcoes criadas em outros processos passando o nome do arquivo referente ao nome da funcao criada dentro dele
    else:
        print("\nSelecione um jogo válido!")

if(__name__ == "__main__"):
    escolhe_jogo()