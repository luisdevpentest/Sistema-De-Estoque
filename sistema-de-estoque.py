"""
SISTEMA DE ESTOQUE
Projeto Integrado Inovação - ADS

Aluno: Luis Eduardo de Melo Barros Santos Ribeiro

"""

estoque = []          
categorias = []       
movimentos = []       


def limpar_tela():
    """Limpa a tela"""
    print("\n" * 50)


def mostrar_menu():
    """Mostra as opções para o usuário escolher"""
    limpar_tela()
    print("=" * 40)
    print("""                                                                                          
                                              --                                          
                                            ----                                          
                                            ------                                        
                                          --------                                        
                                          ----    ..                                      
                                        --    ::::::::                                    
                                          ::::::::::::                                    
                                      ::::::::::::::::::                                  
                                    ..::::::::::                                          
                                    ::::          ++++++++                                
                                  ::    ::::      ++++++++                                
                                    ++++++          ++++++++                              
                                ::++++++                                                  
                                ++++++++        ::++++++++++++                            
                              ::      ++++++++++++++++++++++++++                          
                              --++++++++++++++++++++++++++++++++                          
                            ++++++++++++++++++++++++++++++++++++++                        
                                                                                          
                                                                                          
      MM              ..--                                                                
      @@MM            ..--                                                                
      MMMM    @@MMMM  ..@@MMMM  MMMMMM  @@MMMMMM  @@MMMM@@MM    MM  MMMMMM  @@MMMMMMMMMM++
    MM  MM    MM    MM..--  MM      MM  MM    MM  @@  ..@@MM    MM  MM    mmMM          MM
    MM    MM  MM    MM..--  MM  MMMMMM  MM    MM  @@  ..@@MM    MM  MM@@MM  MM    ::@@MMMM
    @@    MM  MM    MM..--  MM  MM  MM  MM    MM  MM  ..@@MM    MM  MM      MM    MM    MM
  --mm    MM  MM    MM..--  MM  MM  MM  MM    MM  MM@@MM@@--MM..MM  MM@@MM  MM    MM::::MM
                                                      ++..                                
                                                      MM                                  
                                                  MMMM                                    """)
    print("      SISTEMA DE ESTOQUE ")
    print("    Projeto Integrado ADS")
    print("=" * 40)
    print("1. Cadastrar Categoria")
    print("2. Cadastrar Produto")
    print("3. Dar Entrada no Produto")
    print("4. Dar Saída do Produto")
    print("5. Ver Estoque Baixo")
    print("6. Ver Todo o Estoque")
    print("7. Ver Movimentos")
    print("0. Sair")
    print("-" * 40)


def cadastrar_categoria():
    """Pergunta o nome e guarda na lista de categorias"""
    print("\n=== NOVA CATEGORIA ===")
    nome = input("Digite o nome da categoria: ").strip()
    if nome == "":
        print("Nome não pode ficar vazio!")
        return
    
    categoria = {"id": len(categorias) + 1, "nome": nome.upper()}
    categorias.append(categoria)
    print(f"✓ Categoria '{nome}' criada com ID {categoria['id']}")


def cadastrar_produto():
    """Cadastra um produto novo"""
    print("\n=== NOVO PRODUTO ===")
    
    if not categorias:
        print("Cadastre uma categoria primeiro!")
        return
    print("Categorias disponíveis:")
    for cat in categorias:
        print(f"  {cat['id']} - {cat['nome']}")
    
    nome = input("Nome do produto: ").strip()
    if nome == "":
        print("Nome não pode ficar vazio!")
        return
    
    try:
        cat_id = int(input("ID da categoria: "))
        quantidade = int(input("Quantidade inicial: "))
        preco = float(input("Preço (ex: 29.90): "))
    except:
        print("Digite números válidos!")
        return
    
    cat_encontrada = None
    for cat in categorias:
        if cat['id'] == cat_id:
            cat_encontrada = cat
            break
    if not cat_encontrada:
        print("Categoria não encontrada!")
        return
    
    
    produto = {
        "id": len(estoque) + 1,
        "nome": nome.title(),
        "categoria": cat_encontrada['nome'],
        "quantidade": quantidade,
        "preco": preco,
        "local": input("Onde guarda? (ex: Prateleira A): ").strip()
    }
    
    estoque.append(produto)
    print(f"✓ Produto '{nome}' cadastrado com ID {produto['id']}")


def entrada_produto():
    """Adiciona mais unidades de um produto"""
    if not estoque:
        print("Nenhum produto cadastrado!")
        return
    
    ver_estoque()
    try:
        id_prod = int(input("\nID do produto: "))
        qtd = int(input("Quantas unidades entraram? "))
    except:
        print("Digite números!")
        return
    
    for prod in estoque:
        if prod['id'] == id_prod:
            prod['quantidade'] += qtd
            registrar_movimento(prod, "ENTRADA", qtd)
            print(f"✓ Entrada de {qtd} unidades de {prod['nome']}")
            return
    print("Produto não encontrado!")


def saida_produto():
    """Remove unidades do estoque"""
    if not estoque:
        print("Nenhum produto cadastrado!")
        return
    
    ver_estoque()
    try:
        id_prod = int(input("\nID do produto: "))
        qtd = int(input("Quantas unidades saíram? "))
    except:
        print("Digite números!")
        return
    
    for prod in estoque:
        if prod['id'] == id_prod:
            if prod['quantidade'] < qtd:
                print(f"Não tem estoque suficiente! Só tem {prod['quantidade']}")
                return
            prod['quantidade'] -= qtd
            registrar_movimento(prod, "SAÍDA", qtd)
            print(f"✓ Saída de {qtd} unidades de {prod['nome']}")
            return
    print("Produto não encontrado!")


def registrar_movimento(produto, tipo, quantidade):
    """Guarda no histórico o que aconteceu"""
    from datetime import datetime
    agora = datetime.now().strftime("%d/%m/%Y %H:%M")
    mov = {
        "data": agora,
        "tipo": tipo,
        "produto": produto['nome'],
        "quantidade": quantidade
    }
    movimentos.append(mov)


def ver_estoque_baixo():
    """Mostra produtos com pouco estoque"""
    print("\n=== ESTOQUE BAIXO (menos de 10) ===")
    encontrou = False
    for prod in estoque:
        if prod['quantidade'] <= 10:
            print(f"⚠ {prod['nome']} → só tem {prod['quantidade']} unidades")
            encontrou = True
    if not encontrou:
        print("Todos os produtos estão bem!")


def ver_estoque():
    """Mostra todos os produtos"""
    print("\n=== TODOS OS PRODUTOS ===")
    if not estoque:
        print("Nenhum produto cadastrado ainda.")
        return
    
    print(f"{'ID':<3} {'NOME':<20} {'QTD':<5} {'PREÇO':<8} {'LOCAL'}")
    print("-" * 55)
    for prod in estoque:
        print(f"{prod['id']:<3} {prod['nome']:<20} {prod['quantidade']:<5} R${prod['preco']:<7.2f} {prod['local']}")


def ver_movimentos():
    """Mostra o que entrou e saiu"""
    print("\n=== ÚLTIMOS MOVIMENTOS ===")
    if not movimentos:
        print("Nenhum movimento ainda.")
        return
    
    for mov in movimentos[-10:]:
        print(f"{mov['data']} | {mov['tipo']} | {mov['quantidade']} × {mov['produto']}")



print("Bem-vindo ao Sistema de Estoque para Iniciantes!")
print("Feito com carinho para o Projeto Integrado ADS")

while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ").strip()
    
    if opcao == "1":
        cadastrar_categoria()
    elif opcao == "2":
        cadastrar_produto()
    elif opcao == "3":
        entrada_produto()
    elif opcao == "4":
        saida_produto()
    elif opcao == "5":
        ver_estoque_baixo()
    elif opcao == "6":
        ver_estoque()
    elif opcao == "7":
        ver_movimentos()
    elif opcao == "0":
        print("\nObrigado por usar o sistema! Até logo! ")
        break
    else:
        print("Opção inválida! Tente novamente.")
    
    input("\nPressione ENTER para continuar...")