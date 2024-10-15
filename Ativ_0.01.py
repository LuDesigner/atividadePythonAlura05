import os

class Pessoa:
    def __init__(self, nome='', idade=0, profissao=''):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        return f'{self.nome} tem a idade de {self.idade} e tem a profissão de {self.profissao}'

    def exibir_nome_do_programa():
        os.system('cls')
        print("""
█▀▄ ▄▀█ █▀▄ █▀█ █▀   █▀▄ █▀▀   █▀▀ █░█ █▄░█ █▀▀ █ █▀█ █▄░█ ▄▀█ █▀█ █ █▀█ █▀
█▄▀ █▀█ █▄▀ █▄█ ▄█   █▄▀ ██▄   █▀░ █▄█ █░▀█ █▄▄ █ █▄█ █░▀█ █▀█ █▀▄ █ █▄█ ▄█
""")

#------------

    def info_inicial():
        print("\nInformações Iniciais:")
        print(pessoa1)
        print(pessoa2)
        print(pessoa3)
        Pessoa.voltar_ao_menu_principal()
        print()

    def aniver():   
        pessoa1.aniversario()
        pessoa3.aniversario()

        print("Informações após aniversário:")
        print(pessoa1)
        print(pessoa3)
        Pessoa.voltar_ao_menu_principal()
        print()
        
    def job():
        print("Informações de trabalho:")
        print(pessoa1.saudacao)
        print(pessoa2.saudacao)
        print(pessoa3.saudacao)
        Pessoa.voltar_ao_menu_principal()   

 #------------

    def voltar_ao_menu_principal():
        input('\nDigite uma tecla para voltar ao menu principal.\n')
        Pessoa.exibir_nome_do_programa()
        Pessoa.exibir_opcoes()
        Pessoa.escolher_opcao()

    def finalizar_app():
        print('Finalizando o app')

    def opcao_invalida(cls):
        print('Opção Inválida!\n')
        Pessoa.voltar_ao_menu_principal()

 #------------

    def exibir_opcoes():
        print('1. Informações Iniciais')
        print('2. Informações após aniversário')
        print('3. Informações de trabalho')
        print('4. Sair\n')

    def escolher_opcao():
        try:
            opcao_escolhida = int(input('Escolha uma das opções: '))

            if opcao_escolhida == 1:
                Pessoa.info_inicial()
            elif opcao_escolhida == 2:
                Pessoa.aniver()
            elif opcao_escolhida == 3:
                Pessoa.job()
            elif opcao_escolhida == 4:
                Pessoa.finalizar_app()
            else:
                Pessoa.opcao_invalida()
        except:
            Pessoa.opcao_invalida()

 #------------

    @property
    def saudacao(self):
        if self.profissao:
            return f'Olá, sou {self.nome}! Trabalho como {self.profissao}.'
        else:
            return f'Olá, sou {self.nome}!'
    
    def aniversario(self):
        self.idade += 1

#------------

pessoa1 = Pessoa(nome='Alice', idade=25, profissao='Engenheira')
pessoa2 = Pessoa(nome='Luiza', idade=30, profissao='Desenvolvedor')
pessoa3 = Pessoa(nome='Jaque', idade=22)

#------------

Pessoa.exibir_nome_do_programa()
Pessoa.exibir_opcoes()
Pessoa.escolher_opcao()