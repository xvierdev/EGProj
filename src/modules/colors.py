import sqlite3
# import random
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
def colors():
    while True:
        print("╔═════════════════════════════════╗")
        print("║          jogo das cores         ║")
        print("╚═════════════════════════════════╝")
        print("(q)sair,(1)iniciar, (2)pontuação")
        menu = input("selecione um opção :")
        if menu == "q" :
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
                    if points == 10:
                        print("!parabems! voçe completou esse quiz ")
                        break
                else:
                    print("resposta incorreta -1 ponto, a resposta correta era :", color_portuguese)
                    break

        elif menu == "2" :
            print("como funciona ?\na cada vez que acerta uma pergunta ganha um ponto e a cada vez que erra uma quastão perde um ponto\nsua pontuação atual é de:", points)
