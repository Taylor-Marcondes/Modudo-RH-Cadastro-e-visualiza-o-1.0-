import funções as f

f.cab()
print("\033[1;33mModulo RH\033[m".center(55))
f.cab()
l = input("Usuário: ").strip()
s = int(input("Senha: "))
while True:
    if l == "taylor" and s == 123:
        break
    else:
        print("\033[31mUsuario ou senha invalido, tente novamente!\33[m")
        f.cab()
        l = input("Usuario: ").upper()
        s = int(input("Senha: "))
f.cab()
f.menuPrincipal("\033[1;36mQual a opção desejada? \033[m")