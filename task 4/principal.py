import desenvolvedor
import sqlite3
conexao_c = sqlite3.connect('cardapio.db')
cursor_c = conexao_c.cursor()

conexao_p = sqlite3.connect('pedido.db')
cursor_p = conexao_p.cursor()

cursor_c.execute("""
CREATE TABLE IF NOT EXISTS cardapio (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    lanches TEXT,
    preço real
)
""")
cursor_p.execute("""
CREATE TABLE IF NOT EXISTS pedido (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    lanches TEXT,
    quantidade integer,     
    preço real                  
)
""")



def adicionar_item_menu(nome: str, preço: float):
    cursor_c.execute('INSERT INTO cardapio (lanches, preço) VALUES (?, ?)', (nome, preço))
    conexao_c.commit()
    print("Lanche adicionado")

def remove_item_menu(retira_lanche: int):
    cursor_c.execute("DELETE FROM cardapio WHERE id = (?)", (retira_lanche))
    conexao_c.commit()
    print("lanche removido com sucesso")

def menu_desenvolvedor():
    while True :
            print("╔═════════════════════════════════════════════════════════════════╗")
            print("║                        menu de desenvolvedor                    ║")
            print("╚═════════════════════════════════════════════════════════════════╝")
            print("(q)Sair,(1)Adicionar lanche, (2)Remover lanche, (3)Alterar preços")
            menu_desenvolvedor = input("selecione uma opção :")
            if menu_desenvolvedor == 'q' :
                break
            elif menu_desenvolvedor == "1" :
                print("qual lanche voçe deseja adicionar:")
                novo_lanche = str(input(">"))
                print("qual valor desse lanche:")
                preço_novo_lanche = float(input(">"))
                adicionar_item_menu(novo_lanche, preço_novo_lanche)
            
            elif menu_desenvolvedor == "2" :
                
                while True:    
                    cursor_c.execute("SELECT * FROM cardapio")
                    cardapio_remove = cursor_c.fetchall()
                    print(cardapio_remove)
                    print("qual ID do lanche que deseja remover :")
                    cursor_c.execute("SELECT id FROM cardapio")
                    ids = cursor_c.fetchall()
                    remove_lanche = int(input(">"))
                    if remove_lanche in ids :
                        print ("tem verteza que deseja remover esse lanche,(s/n)")
                        certeza = int(input(">"))
                        if certeza == "s" :
                            remove_item_menu(remove_lanche)
                            break
                            
                
                
                            

while True:
    print("╔════════════════════════════════════════════════════════════╗")
    print("║                             menu                           ║")
    print("╚════════════════════════════════════════════════════════════╝")
    print("(q)sair,(1)Fazer pedido, (2)Modo de administrador")
    menu = input("selecione um opção :")
    if menu == "q" :
        break

    elif menu == "1" :
        print

    elif menu == "2" :
        menu_desenvolvedor()



        


