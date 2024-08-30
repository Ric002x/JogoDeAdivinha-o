import random as rd

print("Vamos Jogar? Pense em um número de 1 a 100,"
      " e eu terei 10 tentativas para acertá-lo")

attempts = range(1, 12)
range_inital = 1
range_final = 100

for attenpt in attempts:
    if attenpt == 11:
        print('Minhas tentativas acabaram. Você ganhou 😭')
        break

    try:
        guess = rd.choice(range(range_inital, range_final+1))
    except IndexError:
        print('Teste de novo e se atente as suas resposta!')
        break

    print("\nDeixar eu ver... Você está"
          f" pensando no número: {guess}. Acertei?")
    print("\n1. Sim \n2. Não, é um valor maior"
          " que esse \n3. Não, é um valor menor que esse")

    player_input = input()

    if player_input == '1':
        print("Acertei? Obaa 😁. Vamos de novo?")
        break

    elif player_input == '2':
        range_inital = guess + 1
        if range_inital > range_final:
            print("Opa, a máquina ficou sem possibilidade de acertos. "
                  "Será que você deu alguma resposta errada?")
            break

    elif player_input == '3':
        range_final = guess - 1
        if range_final < range_inital:
            print("Opa, a máquina ficou sem possibilidade de acertos. "
                  "Será que você deu alguma resposta errada?")
            break

    else:
        print('Opção inválida, tente novamente')
        continue
