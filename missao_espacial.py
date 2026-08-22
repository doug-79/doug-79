# Douglas Leonardo dos Santos

"""Você foi recrutado pela Agência Espacial Brasileira para participar de uma simulação de voo espacial. O objetivo é treinar cálculos básicos da missão usando Python, aplicando boas práticas de codificação.

O que você deve fazer:

Crie um arquivo Python chamado missao_espacial.py.
O programa deve:
Pedir ao usuário para digitar seu nome completo (astronauta da missão).
Ler (entrada de dados) a distância da viagem em quilômetros.
Ler (entrada de dados) a velocidade média da nave em km/h.
Calcular o tempo da viagem em horas e em dias, utilizando as fórmulas:
Tempo em horas = distância / velocidade
Tempo em dias = tempo em horas / 24
Exibir uma saudação personalizada e o resultado, conforme o exemplo.
Astronauta João Silva, bem-vindo à simulação!
A viagem terá uma distância de 384400 km (até a Lua).
Com velocidade média de 28000 km/h, o tempo estimado é:
13.73 horas (0.57 dias).
Boa sorte na missão!"""


#variaveis utilizadas 

nome = input("Digite o nome completo do astronauta: ")
distancia = float(input("Digite a distância da viagem em quilômetros: "))
velocidade = float(input("Digite a velocidade média da nave em km/h: "))
tempo_horas = float(distancia / velocidade)
tempo_dias = float(tempo_horas / 24)

#resultados obtidos
print(f"Astronauta {nome}, bem-vindo à simulação!")
print(f"A viagem terá uma distância de {distancia} km.")
print(f"Com velocidade média de {velocidade} km/h, o tempo estimado é:")
print(f"{tempo_horas:.2f} horas ({tempo_dias:.2f} dias).")
print("Boa sorte na missão!")   
