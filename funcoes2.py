
# A. Definir a função 'login_usuario' que recebe o parâmetro 'perfil'
def login_usuario(perfil):
    # B. Verificar se o valor do parâmetro é igual a 'admin', ignorando maiúsculas/minúsculas
    if perfil.lower() == 'admin':
        print('Bem-vindo, administrador')
    else:  # C. Caso contrário
        print('Bem-vindo, usuário')


# D. Chamadas da função com diferentes valores
print("I.", end="")
login_usuario('Admin')

print("II.", end="")
login_usuario('admin')

print("III.", end="")
login_usuario('user')

print("IV.", end="")
login_usuario('usuário')

print("V.", end="")
login_usuario('etc')
