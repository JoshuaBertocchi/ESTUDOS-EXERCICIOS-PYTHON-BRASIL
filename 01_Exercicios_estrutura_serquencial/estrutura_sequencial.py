# %%
# Faça um programa que mostre a mensagem "Alo mundo" na tela:

print("Olá Mundo!")

# %%
#Faça um programa que peça um número e então mostre a mensagem "O número informado foi [número]":

n = int(input("Informe um número: "))
print(f'Número informando {n}')

# %%
#Faça um programa que peça dois números e imprima a soma:

num_01 = int(input("Informe um número: "))
num_02 = int(input("Informe outro número: "))

soma = num_01 + num_02

print(f"{num_01} + {num_02} = {soma}")

# %%
contador = 0
notas_list = []
CONTROLADOR_WHILE = True
try: 
    while CONTROLADOR_WHILE: 
        contador += 1 
        nota = float(input(f'Informe suas Notas({contador}/4): '))
        notas_list.append(nota) 
        if contador == 4:
            media = sum(notas_list)/len(notas_list)
            print(f"Sua média: {media}")
            break
except ValueError as error:
    print(f"Algo deu errado!\n {error}")

# %%
# Faça um programa que converta metros para centímetros:
metros = float(input("Infome o valor em metros para ser convertido: "))
conversao_para_cm = metros * 100
print(f'{conversao_para_cm} cm')
# %%
from math import pi

raio_circulo = float(input('Infomre o raio do circulo:'))
calculo_area_circulo = pi * raio_circulo**2
print(f"Calucolo da Área:{calculo_area_circulo:.2f} cm")
# %%
