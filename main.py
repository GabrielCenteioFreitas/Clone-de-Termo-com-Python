import pandas
import os
from unidecode import unidecode
import random
os.system('cls')
lista_palavras = pandas.read_csv('lista_palavras.txt')
numero = random.randint(0, 7628)
palavra_escolhida = ''
tentativas_feitas = [[['[ ]',37], ['[ ]',37], ['[ ]',37], ['[ ]',37], ['[ ]',37]] for _ in range(6)]
teclado = ['Q','W','E','R','T','Y','U','I','O','P',
           'A','S','D','F','G','H','J','K','L',
           'Z','X','C','V','B','N','M']
cores = [37 for _ in range(26)]

def layout(tentativas_feitas, teclado, cores):
    print(f" \033[1m>{'=-'*10}=<\033[0m")
    print(" \033[1m|      T E R M O      |\033[0m")
    print(f" \033[1m>{'=-'*10}=<\033[0m")
    print("\n", end="")
    for palavra in range(6):
        for letra in range(5):
             print(f"\033[1;{tentativas_feitas[palavra][letra][1]}m {tentativas_feitas[palavra][letra][0]} \033[0m", end="")
        if palavra == 1:
            print(f"\n{' '*35} ", end="")
            for i in range(0, 10):
                if i != 9:
                    print(f"\033[1;{cores[i]}m{teclado[i]} ", end="")
                else: print(f"\033[1;{cores[i]}m{teclado[i]} ")
        elif palavra == 2:
            print(f"\n{' '*35}  ", end="")
            for i in range(10, 19):
                if i != 18:
                    print(f"\033[1;{cores[i]}m{teclado[i]} ", end="")
                else: print(f"\033[1;{cores[i]}m{teclado[i]} ")
        elif palavra == 3:
            print(f"\n{' '*35}    ", end="")
            for i in range(19, 26):
                if i != 25:
                    print(f"\033[1;{cores[i]}m{teclado[i]} ", end="")
                else: print(f"\033[1;{cores[i]}m{teclado[i]} ")
        else: 
            print("\n")
    print(f" \033[1m>{'=-'*10}=<\033[0m", end="")

def avaliar_palpite(tentativa, tentativas_feitas, qntd_tentativas, palavra_escolhida, teclado, cores):
    tentativa_letras = list(tentativa)
    palavra_escolhida_letras = list(palavra_escolhida)
    palavra_escolhida_letras_temp = list(palavra_escolhida)
    for index_tentativa, letra_tentativa in enumerate(tentativa_letras):
        if letra_tentativa in palavra_escolhida_letras_temp:
            if palavra_escolhida_letras.count(letra_tentativa) != 1:
                palavra_escolhida_letras_temp.remove(letra_tentativa)
            if palavra_escolhida_letras[index_tentativa] == letra_tentativa:
                tentativas_feitas[qntd_tentativas][index_tentativa][0] = f" {letra_tentativa.upper()} "
                tentativas_feitas[qntd_tentativas][index_tentativa][1] = 32
                cores[teclado.index(letra_tentativa.upper())] = 32
            else:
                tentativas_feitas[qntd_tentativas][index_tentativa][0] = f" {letra_tentativa.upper()} "
                if palavra_escolhida_letras_temp.count(letra_tentativa) != 0:
                    if palavra_escolhida_letras[palavra_escolhida_letras.index(letra_tentativa)] == tentativa[palavra_escolhida_letras.index(letra_tentativa)]:
                        tentativas_feitas[qntd_tentativas][index_tentativa][1] = 30
                    else:
                        tentativas_feitas[qntd_tentativas][index_tentativa][1] = 33
                else: tentativas_feitas[qntd_tentativas][index_tentativa][1] = 33
                if cores[teclado.index(letra_tentativa.upper())] != 32:
                    cores[teclado.index(letra_tentativa.upper())] = 33
        else:
            tentativas_feitas[qntd_tentativas][index_tentativa][0] = f" {letra_tentativa.upper()} "
            tentativas_feitas[qntd_tentativas][index_tentativa][1] = 30
            if cores[teclado.index(letra_tentativa.upper())] == 37:
                cores[teclado.index(letra_tentativa.upper())] = 30

vitoria = []
def pedir_palpite(tentativas_feitas, palavra_escolhida, teclado, cores):
    for qntd_tentativas in range(6):
        tentativa = input('\n\n\033[1mInsira uma palavra de 5 letras: \033[0m')
        while len(tentativa) != 5 or not tentativa.isalpha() or unidecode(tentativa).lower() not in lista_palavras.columns[:]:
            os.system('cls')
            layout(tentativas_feitas, teclado, cores)
            tentativa = input('\n\n\033[1mInsira uma palavra de 5 letras: \033[0m')
        avaliar_palpite(tentativa, tentativas_feitas, qntd_tentativas, palavra_escolhida, teclado, cores)
        if tentativa == palavra_escolhida:
            vitoria.append("")
            break
        os.system('cls')
        layout(tentativas_feitas, teclado, cores)

def main():
    numero = random.randint(0, int(str(lista_palavras.count)[-14:-10]))
    palavra_escolhida = lista_palavras.columns[numero][:5]
    tentativas_feitas = [[['[ ]',37] for _ in range(5)] for _ in range(6)]
    teclado = ['Q','W','E','R','T','Y','U','I','O','P',
            'A','S','D','F','G','H','J','K','L',
            'Z','X','C','V','B','N','M']
    cores = [37 for _ in range(26)]
    layout(tentativas_feitas, teclado, cores)
    qntd_tentativas = pedir_palpite(tentativas_feitas, palavra_escolhida, teclado, cores)
    if len(vitoria) > 0:
        os.system('cls')
        layout(tentativas_feitas, teclado, cores)
        print('\n')
        print(f"\033[1;32mParabéns!\033[1;37m Você acertou a palavra \033[1;32m{palavra_escolhida}\033[1;37m em \033[1;32m{qntd_tentativas+1}\033[1;37m tentativa(s).")
    else:
        os.system('cls')
        layout(tentativas_feitas, teclado, cores)
        print('\n')
        print(f"\033[1;31mTriste...\033[1;37m A palavra era \033[1;31m{palavra_escolhida}\033[1;37m.")
    

main()
while True:
    vitoria = []
    iniciar_ou_sair = input('\n\033[1;37mDeseja jogar novamente? [S/N]: \033[0m')
    if iniciar_ou_sair in ['s','S']:
        os.system('cls')
        main()
    elif iniciar_ou_sair in ['n','N']:
        break
    else:
        pass
