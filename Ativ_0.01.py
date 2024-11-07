import os

class Pessoa:
    opcoes = [
        {"numero": 1, "descricao": "Informações Iniciais"},
        {"numero": 2, "descricao": "Informações após aniversário"},
        {"numero": 3, "descricao": "Informações de trabalho"},
        {"numero": 4, "descricao": "Sair"}
    ]

    def __init__(self, nome='', idade=0, profissao=''):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        return f'{self.nome} tem a idade de {self.idade} e tem a profissão de {self.profissao}'

    @staticmethod
    def exibir_nome_do_programa():
        os.system('cls')  # Limpa a tela, se estiver no Windows
        print("""
█▀▄ ▄▀█ █▀▄ █▀█ █▀   █▀▄ █▀▀   █▀▀ █░█ █▄░█ █▀▀ █ █▀█ █▄░█ ▄▀█ █▀█ █ █▀█ █▀
█▄▀ █▀█ █▄▀ █▄█ ▄█   █▄▀ ██▄   █▀░ █▄█ █░▀█ █▄▄ █ █▄█ █░▀█ █▀█ █▀▄ █ █▄█ ▄█
""")

    def info_inicial(self):
        print("\nInformações Iniciais:")
        print(self)
        print(pessoa2)
        print(pessoa3)
        self.voltar_ao_menu_principal()

    def aniver(self):   
        self.aniversario()
        pessoa3.aniversario()

        print("Informações após aniversário:")
        print(self)
        print(pessoa3)
        self.voltar_ao_menu_principal()
        
    def job(self):
        print("Informações de trabalho:")
        print(self.saudacao)
        print(pessoa2.saudacao)
        print(pessoa3.saudacao)
        self.voltar_ao_menu_principal()

    def voltar_ao_menu_principal(self):
        input('\nDigite uma tecla para voltar ao menu principal.\n')
        Pessoa.exibir_nome_do_programa()
        Pessoa.exibir_opcoes()
        Pessoa.escolher_opcao()

    @staticmethod
    def finalizar_app():
        print('Finalizando o app')

    @staticmethod
    def opcao_invalida():
        print('Opção Inválida!\n')
        Pessoa.voltar_ao_menu_principal()

    @staticmethod
    def exibir_opcoes():
        for opcao in Pessoa.opcoes:
            print(f'{opcao["numero"]}. {opcao["descricao"]}')

    @staticmethod
    def escolher_opcao():
        try:
            opcao_escolhida = int(input('Escolha uma das opções: '))
            if opcao_escolhida == 1:
                pessoa1.info_inicial()
            elif opcao_escolhida == 2:
                pessoa1.aniver()
            elif opcao_escolhida == 3:
                pessoa1.job()
            elif opcao_escolhida == 4:
                Pessoa.finalizar_app()
            else:
                Pessoa.opcao_invalida()
        except ValueError:
            Pessoa.opcao_invalida()

    @property
    def saudacao(self):
        if self.profissao:
            return f'Olá, sou {self.nome}! Trabalho como {self.profissao}.'
        return f'Olá, sou {self.nome}!'

    def aniversario(self):
        self.idade += 1


# Criando as instâncias
pessoa1 = Pessoa(nome='Alice', idade=25, profissao='Engenheira')
pessoa2 = Pessoa(nome='Luiza', idade=30, profissao='Desenvolvedor')
pessoa3 = Pessoa(nome='Jaque', idade=22)
# Executando o programa
Pessoa.exibir_nome_do_programa()
Pessoa.exibir_opcoes()
Pessoa.escolher_opcao()