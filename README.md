# Jogo de Adivinhação

Este repositório contém um jogo de adivinhação de números escrito em Python. Há duas versões para este jogo, permitindo que tanto a máquina quanto o jogador participem da adivinhação.


## Versões do Jogo

### Versão 1: Máquina Adivinhando
Nesta versão, o jogador pensa em um número entre 1 e 100, e a máquina tenta adivinhar o número escolhido. A máquina tem um total de 10 tentativas para acertar. Após cada palpite da máquina, o jogador deve fornecer um feedback informando se o número é maior, menor, ou se está correto. A máquina ajusta seus palpites com base nesse feedback, tornando-se mais precisa a cada tentativa.

### Versão 2: Jogador Adivinhando
Nesta versão, o papel se inverte: a máquina escolhe aleatoriamente um número entre 1 e 100, e o jogador tem que adivinhar. O jogador tem um total de 5 tentativas para acertar o número escolhido pela máquina. A cada palpite, a máquina dirá se o número é maior ou menor que o palpite do jogador.


## 📋 Tecnologias E Bibliotecas Utilizadas

Ambas as versões foram desenvolvidas utilizando apenas Python 3.12.3, sem necessidade de bibliotecas externas, exceto pela biblioteca padrão random do Python, que é utilizada para gerar números aleatórios.


## 📦 Instalação

Para poder utilizar o programa, basta clonar o respositório utlizando:
```bash
git clone git@github.com:Ric002x/PortifolioPython.git
```


## 🚀 Como jogar

### Versão 1: Máquina Adivinhando
Antes de iniciar, pense em um número entre 1 e 100. Em seguida, inicie o programa com o comando:
```bash
python version_1.py
```

O jogo começará, e a máquina dará seu primeiro palpite. A cada tentativa, você terá três opções para responder:

 - 1 - Se a máquia acertar o número que você pensou;

 - 2 - Se o número que você você pensou é **MAIOR** que o palpite da máquina

 - 3 - Se o número que você você pensou é **MENOR** que o palpite da máquina

O jogo termina quando a máquina adivinhar corretamente ou esgotar as 10 tentativas.

### Versão 2: Jogador Adivinhando
Para jogar, inicie o programa com o comando:
```bash
python version_2.py
```

O jogo começará, e a máquina escolherá um número entre 1 e 100. Agora, é a sua vez de fazer palpites.

**Mas atenção**: não faça palpites aleatórios! A máquina informará se o número que você escolheu é maior ou menor que o número dela, e você poderá ajustar seus palpites conforme as dicas.

 > Exemplo: Se você tentar um palpite de 23 e a máquina disser que o número dela é maior, isso significa que o número correto está entre 24 e 100. Se o seu próximo palpite for 50 e a máquina informar que o número dela é menor, então o número estará entre 24 e 49.

O jogo termina quando o jogador acertar o número ou esgotar as 5 tentativas.
