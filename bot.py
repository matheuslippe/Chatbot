import os


def processar_resposta(resposta, name):

    if resposta == '1':
        while True:
            login = input(
                f'{os.linesep}{name} já conferiu seu login e a senha?{os.linesep}'
            )
            if login.lower() == 'sim':
                resolveu = input(f'{os.linesep}Resolveu?{os.linesep}')
                if resolveu.lower() == 'sim':
                    print(f'{os.linesep}Tenha um bom dia.{os.linesep}')
                elif resolveu.lower() == 'não':
                    print(
                        f'{os.linesep}Aguarde um de nossos técnicos{os.linesep}'
                    )
                break
            elif login.lower() == 'não':
                print(
                    f'{os.linesep}Por favor confira os dados e tente novamente.{os.linesep}'
                )

    elif resposta == '2':
        while True:
            internet = input(
                f'{os.linesep}{name}, ja reiniciou a máquina?{os.linesep}')
            if internet.lower() == 'sim':
                resolveu = input(f'{os.linesep}Resolveu?{os.linesep}')
                if resolveu.lower() == 'sim':
                    print(f'{os.linesep}Tenha um bom dia{os.linesep}')
                    break
                elif resolveu == 'não':
                    print(
                        f'{os.linesep}Por favor aguarde um de nosso técnicos{os.linesep}'
                    )
                    break
            elif internet == 'não':
                print(f'{os.linesep}Por favor reinicie a máquina.{os.linesep}')
    elif resposta == '3':
        input(f'{os.linesep}{name}, qual a sua dificuldade?{os.linesep}')
        print('Nossos técnicos entraram em contato em breve.')
    elif resposta == '4':
        print(f'{os.linesep}{name} aguarde alguns instantes.{os.linesep}')
    else:
        print('Digite apenas sim ou não.')


def start():

    name = input(f'Qual seu nome?{os.linesep}')
    # APRESENTAÇÃO

    print(f'Olá {name}, somos do Suporte de tecnologia.')
    # OFERECER MENU DE OPÇÕES

    resposta = input(
        f'Para que possamos acelerar o atendimento por favor digite o número correspondente ao seu problema:{os.linesep}[1] Problemas com o login.{os.linesep}[2] Dificuldade para acesar a internet.{os.linesep}[3] Outras opções.{os.linesep}[4] Falar com um de nossos técnicos.{os.linesep}'
    )

    # ENVIAR RESPOSTA
    processar_resposta(resposta, name)


if __name__ == '__main__':
    start()
