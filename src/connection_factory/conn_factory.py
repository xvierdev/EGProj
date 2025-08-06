from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# --- 1. Configuração e Conexão ---

# Substitua com seus detalhes de conexão
USUARIO = "user"
SENHA = "egproj"
HOST = "localhost"
BANCO_DE_DADOS = "egproj"

# String de conexão
STRING_DE_CONEXAO = f"mysql+pymysql://{USUARIO}:{SENHA}@{HOST}/{BANCO_DE_DADOS}"

# Cria a engine de conexão com o banco de dados
engine = create_engine(STRING_DE_CONEXAO, echo=True)

# Base para as classes ORM
Base = declarative_base()


# --- 2. Definição do Modelo (Tabela) ---

class Usuario(Base):
    __tablename__ = 'usuarios'  # Nome da tabela no banco de dados

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)

    def __repr__(self):
        return f"<Usuario(nome='{self.nome}', email='{self.email}')>"


# --- 3. Criação da Tabela ---

# Cria a tabela no banco de dados, se ela não existir
Base.metadata.create_all(engine)


# --- 4. Inserindo Dados ---

# Cria uma sessão para interagir com o banco de dados
Session = sessionmaker(bind=engine)
session = Session()

# Cria instâncias da classe Usuario
novo_usuario1 = Usuario(nome='João Silva', email='joao.silva@example.com')
novo_usuario2 = Usuario(nome='Maria Souza', email='maria.souza@example.com')

# Adiciona os novos usuários à sessão
session.add(novo_usuario1)
session.add(novo_usuario2)

# Efetiva (commita) as alterações no banco de dados
session.commit()

print("\n--- Usuários inseridos com sucesso! ---\n")


# --- 5. Consultando Dados ---

print("--- Consultando todos os usuários: ---")
# Faz uma consulta para buscar todos os usuários
todos_os_usuarios = session.query(Usuario).all()

for usuario in todos_os_usuarios:
    print(f"ID: {usuario.id}, Nome: {usuario.nome}, Email: {usuario.email}")

# Fecha a sessão
session.close()
