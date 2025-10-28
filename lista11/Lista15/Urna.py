class Urna:
    def __init__(self, nomeLocal, candidatoA = 'A', candidatoB = 'B', candidatoC = 'C'):
        self.candidatoA = candidatoA
        self.candidatoB = candidatoB
        self.candidatoC = candidatoC
        self.nomeLocal = nomeLocal
        self.votos = {
            self.candidatoA : 0,
            self.candidatoB : 0,
            self.candidatoC : 0,
            'Nulo' : 0,
            'Branco' : 0,
        }
    def votar(self, escolha):
        escolha = escolha.upper()
        if escolha in self.votos:
            