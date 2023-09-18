import json
from dataclasses import dataclass , asdict
from getpass import getpass
from hashlib import sha256



def load_database():
    with open("usuarios.json", "r") as arquivo:
        return json.load(arquivo)

def login():
    database = load_database()
    
    ra_login = input("Digite o seu RA: ")
    senha_login = sha256(getpass('Digite a senha: ').encode()).hexdigest()
    
    for i in database:
        if i["ra"] == ra_login and i["senha"] == senha_login:
            print("Login realizado com sucesso!")
        else:
            print("Usuário ou senha incorreto(s).")


login()
