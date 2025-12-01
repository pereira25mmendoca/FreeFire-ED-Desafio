class Jogador:
    def __init__(self, nickname, kills, tempo):
        self.nickname = nickname
        self.kills = kills
        self.tempo = tempo
        self.pontuacao = (kills * 20) + (tempo * 5)
        self.next = None
# shortened for space
