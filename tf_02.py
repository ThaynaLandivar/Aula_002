# tf_02.py

# Dicionário para armazenar os produtos
inventario = {}

# Função para adicionar um produto ao inventário
def adicionar_produto(nome, preco, quantidade):
    inventario[nome] = {'preco': preco, 'quantidade': quantidade}
    print(f"Produto {nome} adicionado com sucesso!")

# Função para remover um produto do inventário
def remover_produto(nome):
    if nome in inventario:
        del inventario[nome]
        print(f"Produto {nome} removido com sucesso!")
    else:
        print(f"Produto {nome} não encontrado no inventário.")

# Função para listar todos os produtos do inventário
def listar_produtos():
    if inventario:
        for nome, info in inventario.items():
            print(f"Nome: {nome}, Preço: {info['preco']}, Quantidade: {info['quantidade']}")
    else:
        print("O inventário está vazio.")

# Função principal
def main():
    while True:
        print("\nMenu:")
        print("1. Adicionar produto")
        print("2. Remover produto")
        print("3. Listar produtos")
        print("4. Sair")
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            nome = input("Nome do produto: ")
            preco = float(input("Preço do produto: "))
            quantidade = int(input("Quantidade do produto: "))
            adicionar_produto(nome, preco, quantidade)
        elif escolha == '2':
            nome = input("Nome do produto a ser removido: ")
            remover_produto(nome)
        elif escolha == '3':
            listar_produtos()
        elif escolha == '4':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida, por favor tente novamente.")

if __name__ == "__main__":
    main()
