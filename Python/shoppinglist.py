shop_list = []
 
print("******************")
print("Shopping List")
print("******************")
print("Type an item to add it, and \nagain to remove it\n")
print("Commands")
print("/cesta - Create a list with a basic food basket\n/limpar - Remove all list items\n/criar - Create a list\n/lista - Show the list you created\n/sair - Leave.")
print()
 
# Main loop
while True:    
    add = input(": ")
    print()
   
    # Decides if the item can be added
    ap = True
    
    # Stop the user from adding an empty item
    if adicionar == "":
        print("Please add something.\n")
        ap = False
 
    # Deletes an item if it already exists in the list
    for item in shop_list:
        if item == add:
            shop_list.remove(add)
            ap = False
  
    if add == "/limpar":
        ap = False
        shop_list.clear()
    # Creates a pre-defined list (food basket)   
    elif add == "/cesta":
        ap = False
        
        shop_list = ["Rice", "Beans", "Oil", "Noodles", "Salt", "Sugar", "Cookie Package", "Milk", "Coffee"]
    elif add == "/criar":
        ap = False
        print("List creation")
        print("/pronto to finish\n")
        li = []
        
        # Loop to allow the user to create the list
        while True:
            cria = input(": ")
            
            if cria == "/pronto":
                break
               
            li.append(cria)
            
    elif add == "/lista":
        ap = False
        try:
            # Adds items from the list created by the user to the main list
            for i in li:
                if i not in shop_list:
                    shop_list.append(i)
        except:
            print("You still need to create a list.\n")
    elif add == "/sair":
        break     
        
    if ap:
        shop_list.append(add)
        
    # Informs you that the list is empty if there are no items in it
    if len(shop_list) == 0:
        print("Empty list.")
    
    # Shows each list item on the screen if it is not empty
    for item in shop_list:
        if item != "":
            print(item)
 
    print()
