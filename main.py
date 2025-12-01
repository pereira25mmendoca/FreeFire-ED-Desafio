class Jogador:
    def __init__(self, nickname, kills, tempo):
        self.nickname = nickname
        self.kills = kills
        self.tempo = tempo
        self.pontuacao = (kills * 20) + (tempo * 5)
        self.next = None


class ListaEncadeada:
    def __init__(self):
        self.head = None

    def cadastrar(self, nickname, kills, tempo):
        novo = Jogador(nickname, kills, tempo)
        if self.head is None:
            self.head = novo
        else:
            atual = self.head
            while atual.next:
                atual = atual.next
            atual.next = novo
        print(f"✓ Jogador '{nickname}' cadastrado com sucesso!")

    def buscar(self, nickname):
        atual = self.head
        while atual:
            if atual.nickname == nickname:
                return atual
            atual = atual.next
        return None

    def atualizar(self, nickname, kills, tempo):
        jogador = self.buscar(nickname)
        if jogador:
            jogador.kills = kills
            jogador.tempo = tempo
            jogador.pontuacao = (kills * 20) + (tempo * 5)
            print(f"✓ Dados atualizados para '{nickname}'!")
        else:
            print("✗ Jogador não encontrado.")

    def remover(self, nickname):
        atual = self.head
        anterior = None

        while atual and atual.nickname != nickname:
            anterior = atual
            atual = atual.next

        if atual is None:
            print("✗ Jogador não encontrado.")
            return

        if anterior is None:
            self.head = atual.next
        else:
            anterior.next = atual.next

        print(f"✓ Jogador '{nickname}' removido!")

    def exibir_ranking(self):
        if self.head is None:
            print("Nenhum jogador cadastrado.")
            return

        jogadores = []
        atual = self.head

        while atual:
            jogadores.append(atual)
            atual = atual.next

        jogadores.sort(key=lambda x: x.pontuacao, reverse=True)

        print("\n🏆 Ranking Free Fire:")
        for i, j in enumerate(jogadores, start=1):
            print(f"{i}. {j.nickname} - {j.pontuacao} pontos (Kills: {j.kills}, Tempo: {j.tempo})")
        print()


def menu():
    lista = ListaEncadeada()

    while True:
        print("\n===== MENU FREE FIRE =====")
        print("1 - Cad

