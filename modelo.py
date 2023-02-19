class Pessoa:
    def __int__(self, cpf, nome, data_nascimento, usa_oculos):
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.usa_oculos = usa_oculos


class Marca:
    def __int__(self, nome, sigla):
        self.id = None
        self.nome = nome
        self.sigla = sigla

class Veiculo:
    def __int__(self, placa, ano, cor, proprietario, marca):
        self.placa = placa
        self.ano = ano
        self.cor = cor
        self.proprietario = proprietario
        self.marca = marca

