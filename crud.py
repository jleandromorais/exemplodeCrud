import os
usuarios=[]


def adc_user(nome,idade,sexo):
    usuario= {"nome":nome,"idade":idade,"sexo":sexo}
    usuarios.append(usuario)
    print(f"Parabens {nome} foi adicionado com sucesso,sua idade de {idade} tambem,seu {sexo} é esse")
    
    
def leruser():
    for i, usuario in enumerate(usuarios,start=1):
        print(f"{i}. Nome: {usuario['nome']}, Idade: {usuario['idade']} ,sexo:{usuario['sexo']}")
def edit(index):
    usuario=usuarios[index]
    print(f"Voce ira modificar {usuario['nome']}")
    print("1.Editar nome")
    print("2.eEditar idade")
    print("3.Editar sexo")
    opcao=int(input("Qual voce escolhe?"))
    match(opcao):
        case 1:
            novo_nome=input("escolha um novo nome")
            usuario['nome']=novo_nome
            print("Nome atualizado com sucesso!")
        case 2:
            nova_idade=input("Escolha uma nova idade:")
            usuario['idade']=nova_idade
            print("Idade atualizada com sucesso")
        case 3:
            novo_sexo=input("novo sexo por favor")
            usuario['sexo']=novo_sexo
            print("Sexo mudado com sucesso!")
        
def delet(index):
    usuarios.pop(index)
    print("O usuario foi deletado com sucesso")
    
while True:
    print("+===Menu=========+")
    print("1.Insira um usuario")
    print("2.Mostrar usuario")
    print("3.Delete um usuario")
    print("4.editar")
    print("5.sair")
    print("+=================+")

    escolha=int(input("Escolha uma opção:"))
    os.system('cls')
    match(escolha):
        case 1:
            nome=(input("Qual nome adicionado?"))
            idade=(input( "qual sua idade?" ))
            sexo=(input("Qual seu sexo?"))
            adc_user(nome,idade,sexo)
        case 2:
            if usuarios:
                leruser()
            else:
                print("nenhum usuario cadastrado")
        case 3:
            leruser()
            index=int(input("Qual voce deseja apagar?"))-1
            delet(index)
        case 4:
                leruser()
                index=int(input("Qual usuario voce quer editar??"))-1
                edit(index)
        case 5:
            print("Voce vai sair ,tchau")
            break