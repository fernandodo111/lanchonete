açai = 0
pastel = 0
xburger = 0

while True:
    print("opções :")
    print('(1) pastel')
    print('(2) açaí')
    print('(3) xburger')
    
    menu = input('selecione uma opção: ')
    if menu == 'q' :
        valor_pastel = pastel * 12
        valor_açai = açai * 11
        valor_xburguer = xburger * 15
        valor_final = valor_açai + valor_pastel + valor_xburguer
        print (f'{pastel} pastéis = R$ {valor_pastel:.2f}') 
        print (f'{açai} pastéis = R$ {valor_açai:.2f}') 
        print (f'{xburger} pastéis = R$ {valor_xburguer:.2f}')
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