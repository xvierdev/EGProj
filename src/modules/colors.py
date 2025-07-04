import sqlite3
import random
points = 0
conexao = sqlite3.connect('database_color.db')
cursor = conexao.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS database_color (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    color_english TEXT,
    color_Portuguese TEXT        
)
""")
def boot():
    colors_english = ["Black", "White", "Red", "Blue", "Yellow", "Green", "Orange", "Pink", "Purple", "Brown", "Gray"]
    colors_portuguese = ["Preto", "Branco", "Vermelho", "Azul", "Amarelo", "Verde", "Laranja", "Rosa", "Roxo", "Marrom", "Cinza"]
    for colors_e, colors_p in zip(colors_english, colors_portuguese):
            cursor.execute("INSERT INTO database_color (color_english,color_Portuguese) values (?,?)",(colors_e, colors_p))  
            conexao.commit()

def completion():
        cursor.execute("DELETE FROM database_color")
        conexao.commit()




def colors():
    while True:
        cursor.execute("SELECT color_english, color_Portuguese FROM database_color")       
        teste = cursor.fetchall()
        print(teste)
        boot()
        print("╔═════════════════════════════════╗")
        print("║          jogo das cores         ║")
        print("╚═════════════════════════════════╝")
        print("(q)sair,(1)iniciar, (2)pontuação")
        menu = input("selecione um opção :")
        if menu == "q" :
            completion()
            break

        elif menu == "1" :
            print("como funciona o jogo ?\nira aparecer uma coe em ingles e voçe deve digitar sua tradução para o portugues \no jogo vai começar")
            while True :
                cursor.execute("SELECT color_english, color_Portuguese FROM database_color")       
                color_r = cursor.fetchall()
                random_colors = random.choice(color_r)
                color_english, color_portuguese = random_colors
                print("qual a tradução dessa cor:",color_english)
                response = str(input(">"))  
                if response.lower() == color_portuguese.lower() :
                    print ("correto +1 ponto")
                    points += 1
                    print("pontos :",points)
                    if points == 10:
                        print("!parabems! voçe completou esse quiz ")
                        break
                else:
                    points -= 1
                    print("resposta incorreta -1 ponto, a resposta correta era :", color_portuguese)
                    

        elif menu == "2" :
            print("como funciona ?\na cada vez que acerta uma pergunta ganha um ponto e a cada vez que erra uma quastão perde um ponto\nsua pontuação atual é de:", points)
            
