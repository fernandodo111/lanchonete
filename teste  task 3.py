lanches ={
"patel" : 12,
"aça" : 11,
"xburger" : 15
}
senha1 = 1
preço_pastel = 12
preço_açai = 11
preço_xburguer = 15
while True:
    def menu_principal():
        print("╔════════════════════════════════════════════════════════════╗")
        print("║                             menu                           ║")
        print("╚════════════════════════════════════════════════════════════╝")
        print("(q)sair, (1)pastel, (2)açaí, (3)xburger (4)modo administrador")
        
        menu = input('selecione uma opção: ')
        if menu == 'q' :
            valor_pastel = pastel * preço_pastel
            valor_açai = açai * preço_açai
            valor_xburguer = xburger * preço_xburguer
            valor_final = valor_açai + valor_pastel + valor_xburguer
            print (f'{pastel} pastéis = R$ {valor_pastel:.2f}') 
            print (f'{açai} açai = R$ {valor_açai:.2f}') 
            print (f'{xburger} xburguer = R$ {valor_xburguer:.2f}')
            print(f'Valor final R$ {valor_final:.2f}')
            break

        elif menu == '1' :
            quant_pastel = int(input("quantos pasteis deseja?\n> ")) 
            pastel += quant_pastel

        elif menu == '2' :
            quant_açai = int(input("quatos litros de açai deseja?\n> "))
            açai += quant_açai 

        elif menu == '3' :
            quant_xburguer = int(input("quantos xburguers deseja?\n> "))
            xburger += quant_xburguer
        
        elif menu == '4' :
            senha2 = int(input("qual a senha ?"))
            while True :
                if senha1 == senha2 :
                    print("╔══════════════════════════════════════════════════════════════════════╗")
                    print("║                          menu de desenvolvedor                       ║")
                    print("╚══════════════════════════════════════════════════════════════════════╝")
                    print("(q)sair, (1)alterar preços, (2)adicionar item, (4)retiar item do menur")
                    menu_desenvolvedor = input("selecione uma opção :")
                    if menu_desenvolvedor == 'q' :
                        break

                    elif menu_desenvolvedor == '1' :
                        print("qual produto deseja alterar o preço")
                        print("(1)pastel, (2)açaí, (3)xburger ")
                        alt_preço = int(input("escolha uma opção :"))

                        if alt_preço == 1 :
                            print("o valor atual e R$", preço_pastel)
                            alt_preço_pastel = int(input("para qual valor deseja alterar ?"))
                            preço_pastel = alt_preço_pastel

                        elif alt_preço == 2:
                            print("o valor atual do açai e R$", preço_açai) 
                            alt_preço_açai = int(input("para qual valor deseja alterar o açai ?"))
                            preço_açai = alt_preço_açai

                        elif alt_preço == 3 :
                            print("o valor atual do xburguer e R$", preço_xburguer)
                            alt_preço_xburguer = int(input("para qual valor deseja alterar"))
                            preço_xburguer = alt_preço_xburguer

            else :
                print("senha incorreta, acesso negado")
        else :
            print("opção inesxistente")
