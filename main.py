from Graph import Graph
from labirinto import Labinto
import time


while True:
    # exibe o menu
    print("Iniciando Programa......")
    print("Lembre-se -> aperte 0 para Sair")
    print("*************************************************")
    arquivo=input("Digite o nome do arquivo:")
    # verifica o arquivo 
    if arquivo != "0":
        print("Processando o arquivo...")
        start_time = time.time()
        L1=Labinto()
        Busca=L1.busca_profundidagem(L1.Matgrafo(arquivo),arquivo)
        print("Caminho:")
        print (L1.Converte(Busca,arquivo))
        print("Tempo gasto: ", time.time() - start_time)
        print("**********************************************")
    elif arquivo == "0":
        print("Encerrando o programa...")
        break
   