import os

class ClienteBanco:
    lista_de_clientes = []
    def __init__(self, titular, idade, profissao, contato, endereco):
        self.titular = titular.title()
        self.idade = idade
        self.profissao = profissao.title()
        self.contato = contato
        self.endereco = endereco.title()

        ClienteBanco.lista_de_clientes.append(self)

    def __str__(self):
        return f'O {self.titular} é {self.profissao}' 

    def exibir_nome_do_programa():
        os.system('cls')
        print("""
████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█─▄▄▄─██▀▄─██▄─▄▄▀██▀▄─██─▄▄▄▄█─▄─▄─█▄─▄▄▀█─▄▄─███▄─▄▄▀█▄─▄▄─███─▄▄▄─█▄─▄███▄─▄█▄─▄▄─█▄─▀█▄─▄█─▄─▄─█▄─▄▄─█─▄▄▄▄█
█─███▀██─▀─███─██─██─▀─██▄▄▄▄─███─████─▄─▄█─██─████─██─██─▄█▀███─███▀██─██▀██─███─▄█▀██─█▄▀─████─████─▄█▀█▄▄▄▄─█
▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▀▀▄▄▀▄▄▀▄▄▄▄▄▀▀▄▄▄▀▀▄▄▀▄▄▀▄▄▄▄▀▀▀▄▄▄▄▀▀▄▄▄▄▄▀▀▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▀▄▄▄▄▄▀▄▄▄▀▀▄▄▀▀▄▄▄▀▀▄▄▄▄▄▀▄▄▄▄▄▀
""")
        
#------------

    @classmethod
    def listar_clientes(cls):
        print(f'\n{''.ljust(3)}{'Nome do cliente'.ljust(15)} | {''.ljust(1)}{'Idade'.ljust(6)} | {''.ljust(1)}{'Profissão'.ljust(6)} | {''.ljust(4)}{'Contato'.ljust(10)} | {''.ljust(3)}{'Endereço'.ljust(10)}\n')
        for list_cliente in cls.lista_de_clientes:
           print(f'{list_cliente.titular.capitalize().ljust(18)} | {list_cliente.idade}{' Anos'.ljust(5)} | {list_cliente.profissao.capitalize().ljust(10)} | {list_cliente.contato.ljust(14)} | {list_cliente.endereco.capitalize().ljust(18)}')
        ClienteBanco.voltar_ao_menu_principal()

#------------Atualização de dados

    def atualizar_clientes_titular(self):
        print(f'\nDeseja muda o nome do titular {self.titular}? para qual?')
        new_titular = input('Digite aqui: ')
        self.titular = new_titular
        print('\n(>‿◠)✌')
        print(f'O nome do titular foi alterado para {new_titular}')
        ClienteBanco.voltar_ao_menu_principal()

    def atualizar_clientes_idade(self):
        print(f'\nDeseja muda a idade do titular {self.titular} para qual?')
        new_idade = input('Digite aqui: ')
        self.idade = new_idade
        print('\n(>‿◠)✌')
        print(f'\nA idade do titular {self.titular} foi alterado para {new_idade} anos de idade')
        ClienteBanco.voltar_ao_menu_principal()

    def atualizar_clientes_profissao(self):
        print(f'\nDeseja muda a profissão do titular {self.titular} para qual?')
        new_pro = input('Digite aqui: ')
        self.profissao = new_pro
        print('\n(>‿◠)✌')
        print(f'\nA profissão do titular {self.titular} foi alterado para {new_pro}')
        ClienteBanco.voltar_ao_menu_principal()

    def atualizar_clientes_contato(self):
        print(f'\nDeseja muda o contato do titular {self.titular} para qual?')
        new_contato = input('Digite aqui: ')
        self.contato = new_contato
        print('\n(>‿◠)✌')
        print(f'\nO contato do titular {self.titular} foi alterado para {new_contato}')
        ClienteBanco.voltar_ao_menu_principal()
    
    def atualizar_clientes_endereco(self):
        print(f'\nDeseja muda o endereço do titular {self.titular} para qual?')
        new_endereco = input('Digite aqui: ')
        self.endereco = new_endereco
        print('\n(>‿◠)✌')
        print(f'\nO endereço do titular {self.titular} foi alterado para {new_endereco}')
        ClienteBanco.voltar_ao_menu_principal()

#------------Extras

    def voltar_ao_menu_principal():
        input('\nDigite uma tecla para voltar ao menu principal.\n')
        ClienteBanco.exibir_nome_do_programa()
        ClienteBanco.exibir_opcoes()
        ClienteBanco.escolher_opcao()

    def finalizar_app():
        print("""
            (•◡•) /
              """)
        print('Finalizando o app\n')

    def opcao_invalida():
        print("""
            (≖_≖ )
              """)
        print('\nOpção Inválida!\n')
        ClienteBanco.voltar_ao_menu_principal()


#------------Menu Principal
    def exibir_opcoes():
        print('1. Listar Clientes')
        print('2. Atualizar Cadastro')
        print('3. Sair\n')

    def escolher_opcao():
        try:
            opcao_escolhida = int(input('Escolha uma das opções: '))

            if opcao_escolhida == 1:
                ClienteBanco.listar_clientes()
            elif opcao_escolhida == 2:
                ClienteBanco.opcoes_Status()
                ClienteBanco.mudar_status()
            elif opcao_escolhida == 3:
                ClienteBanco.finalizar_app()
            else:
                ClienteBanco.opcao_invalida()
        except:
            ClienteBanco.opcao_invalida()

#------------Escolha de Clientes

    def opcoes_Status():
        print('')
        print(f'1. {pessoa1.titular}') 
        print(f'2. {pessoa2.titular}') 
        print(f'3. {pessoa3.titular}') 
        print('4. Voltar ao menu principal\n')
    
    def mudar_status():
        try:
            opcao_escolhida = int(input('Escolha uma das opções: '))

            if opcao_escolhida == 1:
                ClienteBanco.atualizar_clientes01()
                ClienteBanco.opcao_atualizar_clientes01()
            elif opcao_escolhida == 2:
                ClienteBanco.atualizar_clientes02()
                ClienteBanco.opcao_atualizar_clientes02()
            elif opcao_escolhida == 3:
                ClienteBanco.atualizar_clientes03()
                ClienteBanco.opcao_atualizar_clientes03()
            elif opcao_escolhida == 4:
                ClienteBanco.voltar_ao_menu_principal()
            else:
                ClienteBanco.opcao_invalida()
        except:
            ClienteBanco.opcao_invalida()

#------------Cliente 01

    def atualizar_clientes01():
        print('')
        print('1. Nome do titular') 
        print('2. Idade') 
        print('3. Profissão')
        print('4. Contato') 
        print('5. Endereço')
        print('6. Voltar ao menu principal\n')

    def opcao_atualizar_clientes01():
        try:
            opcao_escolhida = int(input('Escolha uma das opções: '))

            if opcao_escolhida == 1:
                pessoa1.atualizar_clientes_titular()
            elif opcao_escolhida == 2:
                pessoa1.atualizar_clientes_idade()
            elif opcao_escolhida == 3:
                pessoa1.atualizar_clientes_profissao()
            elif opcao_escolhida == 4:
                pessoa1.atualizar_clientes_contato()
            elif opcao_escolhida == 5:
                pessoa1.atualizar_clientes_endereco()
            elif opcao_escolhida == 6:
                ClienteBanco.voltar_ao_menu_principal()
            else:
                ClienteBanco.opcao_invalida()
        except:
            ClienteBanco.opcao_invalida()

#------------Cliente 02

    def atualizar_clientes02():
        print('')
        print('1. Nome do titular') 
        print('2. Idade') 
        print('3. Profissão')
        print('4. Contato') 
        print('5. Endereço')
        print('6. Voltar ao menu principal\n')

    def opcao_atualizar_clientes02():
        try:
            opcao_escolhida = int(input('Escolha uma das opções: '))

            if opcao_escolhida == 1:
                pessoa2.atualizar_clientes_titular()
            elif opcao_escolhida == 2:
                pessoa2.atualizar_clientes_idade()
            elif opcao_escolhida == 3:
                pessoa2.atualizar_clientes_profissao()
            elif opcao_escolhida == 4:
                pessoa2.atualizar_clientes_contato()
            elif opcao_escolhida == 5:
                pessoa2.atualizar_clientes_endereco()
            elif opcao_escolhida == 6:
                ClienteBanco.voltar_ao_menu_principal()
            else:
                ClienteBanco.opcao_invalida()
        except:
            ClienteBanco.opcao_invalida()

#------------Cliente 03

    def atualizar_clientes03():
        print('')
        print('1. Nome do titular') 
        print('2. Idade') 
        print('3. Profissão')
        print('4. Contato') 
        print('5. Endereço')
        print('6. Voltar ao menu principal\n')

    def opcao_atualizar_clientes03():
        try:
            opcao_escolhida = int(input('Escolha uma das opções: '))

            if opcao_escolhida == 1:
                pessoa3.atualizar_clientes_titular()
            elif opcao_escolhida == 2:
                pessoa3.atualizar_clientes_idade()
            elif opcao_escolhida == 3:
                pessoa3.atualizar_clientes_profissao()
            elif opcao_escolhida == 4:
                pessoa3.atualizar_clientes_contato()
            elif opcao_escolhida == 5:
                pessoa3.atualizar_clientes_endereco()
            elif opcao_escolhida == 6:
                ClienteBanco.voltar_ao_menu_principal()
            else:
                ClienteBanco.opcao_invalida()
        except:
            ClienteBanco.opcao_invalida()

 #------------Clientes

pessoa1 = ClienteBanco('Alice', 18, 'Contadora', '21 0000-0000', 'Rua dos números pi, n235')
pessoa2 = ClienteBanco('Bruna', 36, 'Arquiteta', '21 0000-0000', 'Avenida das plantas, n 123, AP 01')
pessoa3 = ClienteBanco('Carlos', 28, 'Designer', '21 0000-0000', 'Estrada da Arte, loja A113')

#------------Ex

ClienteBanco.exibir_nome_do_programa()
ClienteBanco.exibir_opcoes()
ClienteBanco.escolher_opcao()