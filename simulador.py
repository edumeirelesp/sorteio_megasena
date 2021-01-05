from random import randint


class Sorteio:
    def __init__(self):
        self._numeros_ordem_sorteio = ['10', '53', '5', '33', '23', '42', '04', '27', '37', '28', '54', '30', '24',
                                       '34', '43', '17', '16', '35', '36', '41', '06', '29', '44', '51', '02', '11',
                                       '52', '56', '13', '32', '38', '18', '49', '50', '08', '01', '46', '58', '12',
                                       '45', '59',' 20', '40', '47', '14', '57', '07', '39', '31', '19', '60', '25',
                                       '09', '03', '48', '15', '21', '22', '55', '26']
        self._lista_de_resultado = []

    def tratamento(self):
        while len(self._lista_de_resultado) < 6:
            sorteio = self._numeros_ordem_sorteio[randint(0, 59)]
            if self._lista_de_resultado.count(sorteio) == 0:
                self._lista_de_resultado.append(sorteio)
        num = ''
        for i, numero in enumerate(sorted(self._lista_de_resultado)):
            if len(self._lista_de_resultado)-1 == i:
                num += numero
            else:
                num += numero+"-"

        print()

        print(f'Jogo -> [\33[34m{num}\33[m] pode apostar, BOA SORTE !!')


if __name__ == '__main__':
    t = Sorteio()
    t.tratamento()
