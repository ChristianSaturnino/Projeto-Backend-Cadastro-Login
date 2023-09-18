from dataclasses import dataclass, asdict
from getpass import getpass
from hashlib import sha256
import json

@dataclass
class Usuario:
    user: str
    senha: str
    ra: int
    

def cadastra_usuario():
        ra = input("Informe o seu RA: ")
        user = input('Digite o id do usuário: ')
        senha = sha256(getpass('Digite a senha do usuário: ').encode()).hexdigest()
        senha2= sha256(getpass('Confirme a sua senha: ').encode()).hexdigest()
        if senha != senha2:
            print("erro")
        else:
            return Usuario(user, senha, ra)
             

        



usuarios_obj = [
    cadastra_usuario()
]


with open('usuarios.json', 'w') as arquivo:
    usuario = usuarios_obj
    usuarios_dict = None
    if (usuario[0] != None):
        usuarios_dict = list(map(asdict, usuario))
        usuarios_json = json.dumps(usuarios_dict, indent=4)
        arquivo.write(usuarios_json)

def criar_usuario(d):
    return Usuario(**d)
    
usuarios_json = json.dumps(usuarios_dict,sort_keys=True)
