import os

class Conta:
    lista_de_clientes = []
    def __init__(self, titular, saldo):
        self.titular = titular.title()
        self.saldo = saldo
        self._ativo = False
        Conta.lista_de_clientes.append(self)

    def __str__(self):
       return f'O {self.titular} tem disponível em conta R${self.saldo:.2f}'
    
    def exibir_nome_do_programa():
        os.system('cls')
        print("""

██████╗░░█████╗░███╗░░██╗░█████╗░░█████╗░  ░█████╗░██╗░░░░░██╗░░░██╗██████╗░░█████╗░
██╔══██╗██╔══██╗████╗░██║██╔══██╗██╔══██╗  ██╔══██╗██║░░░░░██║░░░██║██╔══██╗██╔══██╗
██████╦╝███████║██╔██╗██║██║░░╚═╝██║░░██║  ███████║██║░░░░░██║░░░██║██████╔╝███████║
██╔══██╗██╔══██║██║╚████║██║░░██╗██║░░██║  ██╔══██║██║░░░░░██║░░░██║██╔══██╗██╔══██║
██████╦╝██║░░██║██║░╚███║╚█████╔╝╚█████╔╝  ██║░░██║███████╗╚██████╔╝██║░░██║██║░░██║
╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝░╚════╝░░╚════╝░  ╚═╝░░╚═╝╚══════╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝
""")


#------------

    @classmethod
    def listar_de_clientes(cls):
        print(f'\n{''.ljust(2)}{'Nome do Cliente'.ljust(18)} | {''.ljust(8)}{'Saldo em conta'.ljust(20)} | {''.ljust(2)}{'Status'}\n')
        for lis_cliente in cls.lista_de_clientes:
           print(f'{lis_cliente.titular.ljust(20)} | {''.ljust(2)}{'Saldo em conta: R$'}{lis_cliente.saldo:.2f}{''.ljust(2)} | {''.ljust(4)}{lis_cliente.ativo}')
        Conta.voltar_ao_menu_principal()

    def listar_ativos():
        print(f'\n Lista dos Titulares\n')
        for lis_ativo in Conta.lista_de_clientes:
            print(f'{lis_ativo.titular} esta {lis_ativo.ativo}') 
        Conta.voltar_ao_menu_principal()

    def disponivel_em_conta():
        print(pessoa1)
        print(pessoa2)
        print(pessoa3)
        Conta.voltar_ao_menu_principal()

    @property
    def ativo(self):
        return '- Cadastrado ☑ ' if self._ativo else '- Sem Cadastro ☐'

    def ativar_conta(self):
        self._ativo = not self._ativo

#------------ Somas

    def soma_titular(self):
        soma_cliente = int(input('Qual valor deseja depositar?: '))
        self.saldo = self.saldo + soma_cliente
        print(f'O valor de {soma_cliente} foi adicionado da conta {self.titular} e agora ficou em R$ {self.saldo}')

    def sub_titular(self):
        sub_cliente = int(input('Qual valor deseja depositar?: '))
        self.saldo = self.saldo - sub_cliente
        print(f'O valor de {sub_cliente} foi retirado da conta {self.titular} e agora ficou em R$ {self.saldo}')
    
    def new_titular(self):
        new_cliente = input('Qual valor deseja depositar?: ')
        self.titular = new_cliente
        print(f'O titular {self.titular} foi alterado para {new_cliente}')

#------------

    def voltar_ao_menu_principal():
        input('\nDigite uma tecla para voltar ao menu principal.\n')
        Conta.exibir_nome_do_programa()
        Conta.exibir_opcoes()
        Conta.escolher_opcao()

    def finalizar_app():
        print("""
▒▒▒▒▒▒▒▓
▒▒▒▒▒▒▒▓▓▓
▒▓▓▓▓▓▓░░░▓
▒▓░░░░▓░░░░▓
▓░░░░░░▓░▓░▓
▓░░░░░░▓░░░▓
▓░░▓░░░▓▓▓▓
▒▓░░░░▓▒▒▒▒▓
▒▒▓▓▓▓▒▒▒▒▒▓
▒▒▒▒▒▒▒▒▓▓▓▓
▒▒▒▒▒▓▓▓▒▒▒▒▓
▒▒▒▒▓▒▒▒▒▒▒▒▒▓
▒▒▒▓▒▒▒▒▒▒▒▒▒▓
▒▒▓▒▒▒▒▒▒▒▒▒▒▒▓
▒▓▒▓▒▒▒▒▒▒▒▒▒▓
▒▓▒▓▓▓▓▓▓▓▓▓▓
▒▓▒▒▒▒▒▒▒▓
▒▒▓▒▒▒▒▒▓
              """)
        print('Finalizando o app')

    def opcao_invalida():
        print('\nOpção Inválida!\n')
        Conta.voltar_ao_menu_principal()

#------------

    def exibir_opcoes():
        print('1. Listar Clientes')
        print('2. Listar Titulares')
        print('3. Disponível em conta')
        print('4. Mudar Status de conta')
        print('5. Atualizar Cadastro')
        print('6. Sair\n')

    def escolher_opcao():
        try:
            opcao_escolhida = int(input('Escolha uma das opções: '))

            if opcao_escolhida == 1:
                Conta.listar_de_clientes()
            elif opcao_escolhida == 2:
                Conta.listar_ativos()
            elif opcao_escolhida == 3:
                Conta.disponivel_em_conta()
            elif opcao_escolhida == 4:
                Conta.opcoes_Status()
                Conta.mudar_status()
            elif opcao_escolhida == 5:
                Conta.opcoes_de_cadastro()
                Conta.opcoes_de_dados()
            elif opcao_escolhida == 6:
                Conta.finalizar_app()
            else:
                Conta.opcao_invalida()
        except:
            Conta.opcao_invalida()

 #------------Ativar ou Desativar Conta

    def opcoes_Status():
        print('')
        print(f'1. {pessoa1.titular} {pessoa1.ativo}') 
        print(f'2. {pessoa2.titular} {pessoa2.ativo}') 
        print(f'3. {pessoa3.titular} {pessoa3.ativo}') 
        print('4. Voltar ao menu principal\n')
    
    def mudar_status():
        try:
            opcao_escolhida = int(input('Escolha uma das opções: '))

            if opcao_escolhida == 1:
                pessoa1.ativar_conta()
                Conta.voltar_ao_menu_principal()
            elif opcao_escolhida == 2:
                pessoa2.ativar_conta()
                Conta.voltar_ao_menu_principal()
            elif opcao_escolhida == 3:
                pessoa3.ativar_conta()
                Conta.voltar_ao_menu_principal()
            elif opcao_escolhida == 4:
                Conta.voltar_ao_menu_principal()
            else:
                Conta.opcao_invalida()
        except:
            Conta.opcao_invalida()

 #------------ Opções de cadastro

    def opcoes_de_cadastro():
        print('')
        print(f'1. Atualizar nome de Titular') 
        print(f'2. Creditar valor') 
        print(f'3. Debitar valor') 
        print('4. Voltar ao menu principal\n')
    
    def opcoes_de_dados():
        try:
            opcao_escolhida = int(input('Escolha um dos titulares opções: '))

            if opcao_escolhida == 1:
                Conta.opcoes_new_titulares()
                Conta.mudar_new_titulares()
            elif opcao_escolhida == 2:
                Conta.opcoes_atualizar_titulares()
                Conta.mudar_dados_titulares()
            elif opcao_escolhida == 3:
                Conta.opcoes_sub_titulares()
                Conta.mudar_sub_titulares()
            elif opcao_escolhida == 4:
                Conta.voltar_ao_menu_principal()
            else:
                Conta.opcao_invalida()
        except:
            Conta.opcao_invalida()

 #------------ Somar

    def opcoes_atualizar_titulares():
        print('')
        print(f'1. {pessoa1.titular} {pessoa1.saldo}') 
        print(f'2. {pessoa2.titular} {pessoa2.saldo}') 
        print(f'3. {pessoa3.titular} {pessoa3.saldo}') 
        print('4. Voltar ao menu principal\n')
    
    def mudar_dados_titulares():
        try:
            opcao_escolhida = int(input('Escolha um dos titulares opções: '))

            if opcao_escolhida == 1:
                pessoa1.soma_titular()
                Conta.voltar_ao_menu_principal()
            elif opcao_escolhida == 2:
                pessoa2.soma_titular()
                Conta.voltar_ao_menu_principal()
            elif opcao_escolhida == 3:
                pessoa3.soma_titular()
                Conta.voltar_ao_menu_principal()
            elif opcao_escolhida == 4:
                Conta.voltar_ao_menu_principal()
            else:
                Conta.opcao_invalida()
        except:
            Conta.opcao_invalida()

 #------------ Subtração

    def opcoes_sub_titulares():
        print('')
        print(f'1. {pessoa1.titular} {pessoa1.saldo}') 
        print(f'2. {pessoa2.titular} {pessoa2.saldo}') 
        print(f'3. {pessoa3.titular} {pessoa3.saldo}') 
        print('4. Voltar ao menu principal\n')
    
    def mudar_sub_titulares():
        try:
            opcao_escolhida = int(input('Escolha um dos titulares opções: '))

            if opcao_escolhida == 1:
                pessoa1.sub_titular()
                Conta.voltar_ao_menu_principal()
            elif opcao_escolhida == 2:
                pessoa2.sub_titular()
                Conta.voltar_ao_menu_principal()
            elif opcao_escolhida == 3:
                pessoa3.sub_titular()
                Conta.voltar_ao_menu_principal()
            elif opcao_escolhida == 4:
                Conta.voltar_ao_menu_principal()
            else:
                Conta.opcao_invalida()
        except:
            Conta.opcao_invalida()

 #------------ New Titular

    def opcoes_new_titulares():
        print('')
        print(f'1. {pessoa1.titular}') 
        print(f'2. {pessoa2.titular}') 
        print(f'3. {pessoa3.titular}') 
        print('4. Voltar ao menu principal\n')
    
    def mudar_new_titulares():
        try:
            opcao_escolhida = int(input('Escolha um dos titulares opções: '))

            if opcao_escolhida == 1:
                pessoa1.new_titular()
                Conta.voltar_ao_menu_principal()
            elif opcao_escolhida == 2:
                pessoa2.new_titular()
                Conta.voltar_ao_menu_principal()
            elif opcao_escolhida == 3:
                pessoa3.new_titular()
                Conta.voltar_ao_menu_principal()
            elif opcao_escolhida == 4:
                Conta.voltar_ao_menu_principal()
            else:
                Conta.opcao_invalida()
        except:
            Conta.opcao_invalida()

 #------------

pessoa1 = Conta('Alice', 125.50)
pessoa2 = Conta('Carlos', 525.01)
pessoa3 = Conta('Anna', 275.99)

#------------

Conta.exibir_nome_do_programa()
Conta.exibir_opcoes()
Conta.escolher_opcao()