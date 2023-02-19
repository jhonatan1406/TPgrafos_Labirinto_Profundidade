from Graph import Graph

class Labinto:
    def Matgrafo ( self, arquivo) -> Graph:
        with open(arquivo, 'r') as f: #Pega um arquivo
            lines = f.read().split("\n") #função não o \n
        linhas = len(lines)
        colunas = len(lines[0])
        g1= Graph(linhas * colunas, adj_list=[]) # cria uma lista adjacencia 
        for i in range (linhas):
            for j in range (colunas):
                pos = (i*colunas+j)
                if lines[i][j] !="#":
                    if j !=0 and lines[i][j-1] != "#" : #tras
                        g1.add_directed_edge(pos,(pos-1))
                    if j != (len(lines[i])-1) and lines[i][j+1] !="#": # frente
                        g1.add_directed_edge (pos,pos+1)
                    if i != 0 and lines [i-1][j] != "#":#cima
                        g1.add_directed_edge((pos - (colunas)), pos)
                    if i != (linhas-1) and lines[i+1][j] !="#":#baixo
                        g1.add_directed_edge((pos+(colunas)),pos)
        
        return g1 #retorna uma lista adjacencia com respectivos nos 
    
    def busca_profundidagem (self, g:Graph, arquivo):
        with open(arquivo,'r') as f:
            lines = f.read().split("\n")
        linhas = len(lines)
        colunas = len(lines[0])
        for i in range (linhas):
            for j in range (colunas):
                pos = (i*colunas+j)
                if lines[i][j] == 'S': # pega no arquivo o ponto incial
                    inicio = pos
                if lines [i][j]== 'E':#pega no arquivo o ponto de saida
                    fim = pos   
                    
        F=g.dfs_end(inicio,fim) # realiza a busca de profundidade na lista 
        return F
    #converte os nos do melhor caminho em coordenada 
    # def Converte (self, Q ,arquivo)->None:
    #     with open(arquivo,'r') as f:
    #         lines = f.read().split("\n")
    #     linhas = len(lines)
    #     colunas = len(lines[0])
    #     coordenada=[]
    #     for i in range (linhas):
    #         for j in range (colunas):
    #             pos = (i*colunas+j)
    #             for k in range (len(Q)):
    #                 if pos== Q[k]:
    #                     lin =  str(i)
    #                     col = str(j)
    #                     tupla = (lin,col)
    #                     coordenada.append(tupla)
    #                     #print("caminho: ",pos)
    #                     #print("coordenada:",coordenada[-1])
    #     print(coordenada)
    #uma opção caso queira converter assim

    def Converte (self, Q , arquivo):
        coordenada =[]
        with open(arquivo,'r') as f:
            lines = f.read().split("\n")
        linhas = len(lines)
        colunas = len(lines[0])

        for i in range (len(Q)):
            lin= Q[i] // colunas
            col= Q[i]%colunas
            tupla = (lin,col) # uma tupla
            coordenada.append(tupla)# adicona numa lista 

        print(coordenada)
            
 