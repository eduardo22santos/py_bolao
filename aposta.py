from banco import Banco

class Aposta:
    banco = Banco

    def __init__(self, jogo:list,jogador:str,arquivo:str,data:str):        
        self.banco.insert_data(jogador,data,arquivo,jogo[0],jogo[1],jogo[2],jogo[3],jogo[4],jogo[5])

