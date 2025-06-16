cardapio = {
    "pastel" : 12,
    "açai" : 11,
    "xburger" : 15
}
pedido = {}

senha1 = 1
import menu_desenvolvedor_arqui 
def adicionar_item_caradapio(nome : str, preço : float):
    cardapio[nome] = preço
    print(nome,"adicionado com sucesso")

def remover_item_cardapio(lanche: str) :
    cardapio.pop(lanche) 
    print(lanche, "removido com sucesso")

def adicionar_item_pedido(item, quantidade):
 if item in cardapio.keys():
     pedido [item] = quantidade
    
def fechar_conta():
    total = 0
    for item, quantidade in pedido.items():
        if item in cardapio:
            preco_unitario = cardapio[item]
            preco_total_item = preco_unitario * quantidade
            print(f"{item} {quantidade} = R$ {preco_total_item:.2f}")
            total += preco_total_item
        else:
            print(f"{item} não está mais no cardápio!")

    print(f"\nTotal a pagar: R$ {total:.2f}")

valor_final = 0
while True:
    print("╔════════════════════════════════════════════════════════════╗")
    print("║                             menu                           ║")
    print("╚════════════════════════════════════════════════════════════╝")
    print("(q)sair,(1) Modo administrador, (2) Fazer pedido")
    menu = input("selecione um opção :")
    if menu == "q":
        fechar_conta()

    elif menu == "1":
        menu_desenvolvedor_arqui.menu_desenvolvedor()
    
    elif menu == "2" :
        while True:
            print("\nlanches disponiveis\n", list(cardapio.keys())," (q)sair\n")
            print("quanl lanche deseja?\n")
            item_escolhido = str(input(">"))
            if item_escolhido == "sair":
                break
            elif item_escolhido in cardapio.keys():               
                print("quantos", item_escolhido,"deseja")
                quantidade = int(input(">"))
                adicionar_item_pedido (item_escolhido, quantidade)
                break

            else :
                print ("lanche não existe")   



