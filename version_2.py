import random as rd

print("Olá! Vamos jogar? Estou pensando em um número de 1 a 100."
      " Consigue adivinhar qual é?\n Você tem 10 tentativas")

range_inital = 1
range_final = 100
possible_numbers = range(range_inital, range_final+1)
machine_number = rd.choice(possible_numbers)
attempts = range(1, 6)

for attempt in attempts:

    print(f"\nTentativa {attempt} \nQual número estou pensando?")
    player_guess = input()
    player_guess = int(player_guess)

    if player_guess == machine_number:
        print('Uau, muito bem. Você acertou!')
        break

    elif player_guess > machine_number:
        if attempt == 5:
            print("Você perdeu!")
            break
        print("Pensei em um número menor que esse,"
              " mas você pode tentar de novo!")
        range_final = player_guess - 1
        print("\nPorém agora você pode tentar"
              f" um número entre {range_inital} e {range_final}")

    elif player_guess < machine_number:
        if attempt == 5:
            print("Você perdeu!")
            break
        print("\nPensei em um número maior que "
              "esse, mas você pode tentar de novo!")
        range_inital = player_guess + 1
        print("Porém agora você pode tentar um número "
              f"entre {range_inital} e {range_final}")
