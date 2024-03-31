# Cria uma lista vazia para armazenar os itens da lista de compras
lista = []
 
print("******************")
print("Shopping List")
print("******************")
print("Type an item to add it, and \nagain to remove it\n")
print("Commands")
print("/cesta - Create a list with a basic food basket\n/limpar - Remove all list items\n/criar - Create a list\n/lista - Show the list you created\n/sair - Leave.")
print()
 
# Loop principal para interação contínua
while True:    
    adicionar = input(": ")
    print()
   
    # Variável de controle para decidir se o item pode ser adicionado à lista
    ap = True
    
    # Impede que o usuário adicione um item vazio
    if adicionar == "":
        print("Please add something.\n")
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
        
        lista = ["Rice", "Beans", "Oil", "Noodles", "Salt", "Sugar", "Cookie Package", "Milk", "Coffee"]
    elif adicionar == "/criar":
        ap = False
        print("List creation")
        print("/pronto to finish\n")
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
            print("You still need to create a list.\n")
    elif adicionar == "/sair":
        break     
        
    # Adiciona um item na lista de acordo com a variavel de controle
    if ap:
        lista.append(adicionar)
        
    # Informa que a lista está vazia se não houver itens nela
    if len(lista) == 0:
        print("Empty list.")
    
    # Mostra cada item da lista na tela se não for vazia
    for item in lista:
        if item != "":
            print(item)
 
    print()
