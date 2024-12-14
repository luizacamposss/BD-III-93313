from services.usuario_service import UsuarioService
from repositories.usuario_repository import UsuarioRepository
from config.database import Session
import os

session = Session()
repository = UsuarioRepository(session)
service = UsuarioService(repository)

# Limpa o terminal.
os.system("cls || clear")

# Solicitando dados para o usuário.
print("\nCadastrando Usuário")
nome = input("Digite o seu nome: ")
email = input("Digite o seu email: ")
senha = input("Digite a sua senha: ")

service.criar_usuario(nome, email, senha)

# Exibindo todos os registros na tabela "usuarios" do banco de dados.
print("\n=== Listando usuários cadastrados ===")
lista_usuario = service.listar_todos_usuarios
for usuario in lista_usuario:
    print(f" Seu Nome: {usuario.nome} \nE-mail: {usuario.email}")

