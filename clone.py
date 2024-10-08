Nome = input('Escreva qual o seu nome: ')
Idade = input('Qual sua idade: ')
if Nome and Idade:
    print(f'Seu nome é: {Nome}')
    print(f'Seu nome invertido é: {Nome[::-1]}')
    print(f'Seu nome tem',len(Nome),' letras')
    print(f'A primeira letra do seu nome é: {Nome[0]}')
    print(f'A última letra do seu nome é: {Nome[-1]}')
    if ' ' in Nome:
        print('Seu nome tem espaços')
    else:
        print('Seu nome não tem espaços')
