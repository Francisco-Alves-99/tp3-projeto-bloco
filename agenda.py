# Função para adicionar um novo contato
def adicionar_contato(agenda, nome, data_nascimento, endereco, telefones, emails):
    # Verifica se o contato já existe
    if nome in agenda:
        print(f"O contato {nome} já existe na agenda.")
    else:
        # Adiciona o novo contato ao dicionário
        agenda[nome] = {
            "Data de Nascimento": data_nascimento,
            "Endereço": endereco,
            "Telefones": telefones,
            "Emails": emails
        }
        print(f"Contato {nome} adicionado com sucesso!")

# Função para exibir as informações de um contato
def exibir_contato(agenda, nome):
    # Verifica se o contato existe
    if nome in agenda:
        contato = agenda[nome]
        print(f"\nContato: {nome}")
        print(f"Data de Nascimento: {contato['Data de Nascimento']}")
        print("Endereço:")
        for chave, valor in contato["Endereço"].items():
            print(f"  {chave}: {valor}")
        print("Telefones:")
        for telefone in contato["Telefones"]:
            print(f"  {telefone}")
        print("Emails:")
        for email in contato["Emails"]:
            print(f"  {email}")
    else:
        print(f"Contato {nome} não encontrado.")

# Função para editar um contato
def editar_contato(agenda, nome):
    if nome in agenda:
        print(f"Editando informações para {nome}...")
        contato = agenda[nome]
        
        # Editando a data de nascimento
        nova_data_nascimento = input(f"Nova data de nascimento (atual: {contato['Data de Nascimento']}): ")
        contato['Data de Nascimento'] = nova_data_nascimento
        
        # Editando o endereço
        print("Editando endereço:")
        rua = input(f"Rua (atual: {contato['Endereço']['Rua']}): ")
        numero = input(f"Número (atual: {contato['Endereço']['Número']}): ")
        bairro = input(f"Bairro (atual: {contato['Endereço']['Bairro']}): ")
        municipio = input(f"Município (atual: {contato['Endereço']['Município']}): ")
        estado = input(f"Estado (atual: {contato['Endereço']['Estado']}): ")
        cep = input(f"CEP (atual: {contato['Endereço']['CEP']}): ")
        
        contato['Endereço'] = {
            "Rua": rua,
            "Número": numero,
            "Bairro": bairro,
            "Município": municipio,
            "Estado": estado,
            "CEP": cep
        }
        
        # Editando telefones
        novo_telefone = input("Digite o novo telefone (ou pressione Enter para manter): ")
        if novo_telefone:
            contato['Telefones'].append(novo_telefone)
        
        # Editando e-mails
        novo_email = input("Digite o novo e-mail (ou pressione Enter para manter): ")
        if novo_email:
            contato['Emails'].append(novo_email)

        print(f"Informações de {nome} atualizadas com sucesso!")
    else:
        print(f"Contato {nome} não encontrado.")

# Função para excluir um contato
def excluir_contato(agenda, nome):
    if nome in agenda:
        del agenda[nome]
        print(f"Contato {nome} excluído com sucesso!")
    else:
        print(f"Contato {nome} não encontrado.")

# Função principal que manipula a agenda
def main():
    agenda = {}

    while True:
        print("\nAgenda de Contatos")
        print("1. Adicionar contato")
        print("2. Exibir contato")
        print("3. Editar contato")
        print("4. Excluir contato")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            nome = input("Digite o nome do contato: ")
            data_nascimento = input("Digite a data de nascimento (DD/MM/AAAA): ")
            
            endereco = {}
            endereco['Rua'] = input("Digite a rua: ")
            endereco['Número'] = input("Digite o número: ")
            endereco['Bairro'] = input("Digite o bairro: ")
            endereco['Município'] = input("Digite o município: ")
            endereco['Estado'] = input("Digite o estado: ")
            endereco['CEP'] = input("Digite o CEP: ")
            
            telefones = []
            while True:
                telefone = input("Digite o número de telefone (ou 'sair' para parar): ")
                if telefone.lower() == "sair":
                    break
                telefones.append(telefone)
            
            emails = []
            while True:
                email = input("Digite o e-mail (ou 'sair' para parar): ")
                if email.lower() == "sair":
                    break
                emails.append(email)
            
            adicionar_contato(agenda, nome, data_nascimento, endereco, telefones, emails)

        elif opcao == "2":
            nome = input("Digite o nome do contato para exibir: ")
            exibir_contato(agenda, nome)

        elif opcao == "3":
            nome = input("Digite o nome do contato para editar: ")
            editar_contato(agenda, nome)

        elif opcao == "4":
            nome = input("Digite o nome do contato para excluir: ")
            excluir_contato(agenda, nome)

        elif opcao == "5":
            print("Saindo da agenda...")
            break

        else:
            print("Opção inválida, tente novamente.")

# Executando o programa
main()
