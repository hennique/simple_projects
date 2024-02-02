# Cria uma lista vazia para armazenar os itens da lista de compras
lista = []
 
print("******************")
print("Lista de compras")
print("******************")
print("Digite o nome de um item para adicioná-lo na lista, e \nnovamente para removê-lo\n")
print("Comandos")
print("/cesta - Cria uma lista com uma cesta básica\n/limpar - Elimina todos os itens da lista\n/criar - Cria uma lista\n/lista - Mostra a lista que você criou\n/sair - Sai da lista de compras")
print()
 
# Loop principal para interação contínua
while True:    
    adicionar = input(": ")
    print()
   
    # Variável de controle para decidir se o item pode ser adicionado à lista
    ap = True
    
    # Impede que o usuário adicione um item vazio
    if adicionar == "":
        print("Por favor insira algo.\n")
        ap = False
 
    # Deleta um item se ele já existir na lista
    for item in lista:
        if item == adicionar:
            lista.remove(adicionar)
            ap = False
  
    if adicionar == "/limpar":
        ap = False
        lista.clear()
    # Cria uma lista pré-definida (cesta básica)    
    elif adicionar == "/cesta":
        ap = False
        
        lista = ["Arroz", "Feijao", "Oleo", "Macarrao", "Sal", "Açucar", "Pacote de bolacha", "Leite", "Cafe"]
    elif adicionar == "/criar":
        ap = False
        print("Criação de lista")
        print("/pronto para terminar\n")
        li = []
        
        # Loop para permitir a criação da lista pelo usuário
        while True:
            cria = input(": ")
            
            if cria == "/pronto":
                break
               
            li.append(cria)
            
    elif adicionar == "/lista":
        ap = False
        try:
            # Adiciona itens da lista criada pelo usuário à lista principal
            for i in li:
                if i not in lista:
                    lista.append(i)
        except:
            print("Você ainda não criou uma lista.\n")
    elif adicionar == "/sair":
        break     
        
    # Adiciona um item na lista de acordo com a variavel de controle
    if ap:
        lista.append(adicionar)
        
    # Informa que a lista está vazia se não houver itens nela
    if len(lista) == 0:
        print("Lista vazia.")
    
    # Mostra cada item da lista na tela se não for vazio
    for item in lista:
        if item != "":
            print(item)
 
    print()
