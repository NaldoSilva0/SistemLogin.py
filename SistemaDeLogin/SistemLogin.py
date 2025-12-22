import os
from datetime import date, datetime

if not os.path.exists('LogEntrada.txt'):
    with open('LogEntrada.txt', 'w', encoding='utf-8') as log:
        log.write('\n---CADASTRO DE USUARIOS---\n')

def usuarioReg(usuario, senha):
    with open('LogEntrada.txt','a', encoding='utf-8') as log:
        log.write(f'{usuario};{senha}\n')

def listaReg():
    print('-=-'*20)
    print('[1]-REGISTRAR CONTA')
    print('[2]-LOGAR CONTA')
    print('[3]-SAIR')
    resposta = input('Digite sua opção: ')
    return resposta

def listaPlogin():
    print('[1]-ALTERAR SENHA')
    print('[2]-INFORMAÇÔES DA CONTA')
    print('[3]-LOGOUT')
    resposta = input('Digite a opção: ')
    return resposta

def mudarSenha(nomeAlvo, novaSenha):
    with open('LogEntrada.txt', 'r', encoding='utf-8') as log:
        linhas = log.readlines()

    with open('LogEntrada.txt', 'w', encoding='utf-8') as log:
        for linha in linhas:
            if ';' in linha:
                usuarioRegistro, senhaRegistro = linha.strip().split(';')
                if usuario == nomeAlvo:
                    log.write(f'{usuario};{novaSenha}\n')
                else:
                    log.write(linha)
            else:
                log.write(linha)

def usuarioExiste(usuario):
    with open('LogEntrada.txt', 'r', encoding='utf-8') as log:
        for linha in log:
            if ';' in linha:
                usuarioRegistro, _ = linha.strip().split(';')
                if usuarioRegistro == usuario:
                    return True
    return False

def RetornoPmenu():
    global contadorSenha

    while True:
        menuConfig = listaPlogin()
        
        if menuConfig == '1':
            contadorSenha = 5
            while contadorSenha > 0: 
                confirmarSenha = input('Digite a senha atual: ')
                print('-=-'*20)
                if confirmarSenha != senha:
                    contadorSenha -= 1
                    
                    print(f'Senha diferente da atual, restam {contadorSenha} antes de bloquearmos as tentativas pela segurança de sua conta.')
                    if contadorSenha == 0:
                        print('Você atingiu o limite de tentativas do sistema, Tente novamente mais tarde!!')
                        break
                else:
                        senhaNova = input('Digite a nova senha: ')
                        repSenhaNova = input('Digite a nova senha novamente: ')

                        if senhaNova != repSenhaNova:
                            contadorSenha -= 1
                            print(f'As senhas não são iguais, você tem {contadorSenha} Chances antes de bloquearmos suas tentativas.')
                            if contadorSenha == 0:
                                print('Você atingiu o limite de tentativas!!')
                                break
                        else:
                            print('Senha trocada com sucesso!!')
                            newSenha = mudarSenha(usuario, senhaNova)
                            break
            continue
                        
        elif menuConfig == '2':
            print('---INFORMAÇÔES DA CONTA---\n')
            print('-=-'*20)
            print(f'Você logou na conta: {usuario}')
            print(f'Você logou na conta pela ultima vez em: {data} - {hora}')
            input(f'Pressione ENTER para voltar ao menu')
            continue
        
        elif menuConfig == '3':
            confirmar = input('Tem certeza que deseja dar logout da conta? [S/N] ').lower()
            if confirmar == 's':
                print('Obrigado por usar nossos serviços!!')

                dataLogout = date.today()
                horaLogout = datetime.now().strftime('%H:%M:%S')


                with open('LogLogout.txt', 'a', encoding='utf-8') as regLL:
                    regLL.write(f'{usuario} Logout - {dataLogout} - {horaLogout}\n')
                    break

            elif confirmar == 'n':
                print('Então continue aproveitando nossos serviços!!')
                continue
            else:
                print('Essa função não existe!! Voltando para o menu!!')
                continue


with open('LogEntrada.txt', 'r', encoding='utf-8') as log:
    linhas = log.readlines()

contaExiste = False

while True:
    respostaLista = listaReg()

    if respostaLista == '1':
        print('Menu de registro\n')
        print('-=-'*20)
        usuario = input('Digite o usuário: ')
        if usuarioExiste(usuario):
            print('Esse usuário já existe!!')
        else:
            senha = input('Digite a senha: ')
            repSenha = input('Repita a senha: ')
            if senha != repSenha:
                print('As senhas não são iguais!!')
            else:
                usuarioReg(usuario, senha)
                print('Registro feito com sucesso!!')
            

    elif respostaLista == '2': 
        usuario = input('Usuário: ')
        senha = input('Senha: ')
        print('-=-'*20)
        with open('LogEntrada.txt', 'r', encoding='utf-8') as log:
            linhas = log.readlines()
        
        contaExiste = False
        
        for linha in linhas:
            if ';' in linha:
                usuarioRegistro, senhaRegistro = linha.strip().split(';')

                if usuario == usuarioRegistro and senha == senhaRegistro:
                    contaExiste = True
                    break
        
        if contaExiste:

            contadorSenha = 5
            data = date.today()
            hora = datetime.now().strftime('%H:%M:%S')

            if not os.path.exists('LogLogout.txt'):
             with open('LogLogout.txt', 'w', encoding='utf-8') as regLL:
                print('---INÍCIO DE LOG---')

            with open('LogLogout.txt', 'a', encoding='utf-8') as regLL:
                regLL.write(f'{usuario} Logou - {data} - {hora}\n')

            loginCompleto = print('Login Completo!!')

            RetornoPmenu()
            break
        else:
            if usuario != usuarioRegistro or senha != senhaRegistro:
                print('Informações incorretas!! tente novamente.\n')

    elif respostaLista == '3': 
        print('Obrigado por usar nossos serviços!!')
        exit()
    else:
        print('Opção inválida\n')




                        



  


        