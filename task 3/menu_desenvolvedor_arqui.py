import principal

def menu_desenvolvedor():
    from principal import senha1, cardapio, remover_item_cardapio, adicionar_item_caradapio
    senha2 = int(input("qual a senha ?"))
    while True :
        if senha1 == senha2 :
            print("╔══════════════════════════════════════════════════════════════════════╗")
            print("║                          menu de desenvolvedor                       ║")
            print("╚══════════════════════════════════════════════════════════════════════╝")
            print("(q)sair, (1)alterar preços, (2)adicionar item, (3)retiar item do menur")
            menu_desenvolvedor = input("selecione uma opção :")
            if menu_desenvolvedor == 'q' :
                break
            elif menu_desenvolvedor == "1":
                while True:
                    print("lanches disponiveis",list(cardapio.keys()))
                    alt = str(input(">"))
                    if alt == "sair":
                        break
                    elif alt in cardapio.keys():
                        print("esse e o valor atual",cardapio[alt],"do", alt)
                        print("para qual valor deseja alterar:")
                        alt_valor = float(input(">"))
                        cardapio[alt] = alt_valor
                        break
                    else :
                        print("lanche inexistente")
            elif menu_desenvolvedor == "2":
                while True:
                    print("qual lanche voçe quer adiciona:")
                    add = str(input(">"))
                    if add == "sair":
                        break
                    if add not in cardapio.keys():
                        print("qual o valor do", add)
                        valor_add = float(input(">"))
                        adicionar_item_caradapio(add,valor_add)
                    else:
                        print("lanche ja existe")

            elif menu_desenvolvedor == "3" :
                while True:
                    print("qual lanche deseja remover:")
                    remove = str(input(">"))
                    if remove == "sair":
                        break
                    elif remove in cardapio.keys():
                        print("tem certeza que deseja remover o ", remove ,"\n s/n")
                        cert = str(input(">"))
                        if cert == "s":
                            remover_item_cardapio(remove)
                            break
                        elif cert == "n" :
                            break
                        else:
                            print("opção invalida")
                    
            

