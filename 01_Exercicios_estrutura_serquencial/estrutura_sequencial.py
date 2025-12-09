3
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
# Faça um programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

def formatar_valores(valor):
    if valor == int(valor):
        return f"{int(valor)}"
    else:
        return f"{valor:.2f}"

metro_quadrado = float(input("Informe o valor do metro quadrado: "))
calculo_area = metro_quadrado**2
dobro = calculo_area *2
print(f"Valor informado: {formatar_valores(metro_quadrado)}m²\n Área do quadrado: {formatar_valores(calculo_area)} cm²\n Dobro do resultado: {formatar_valores(dobro)} cm²")
# %%    
#Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

valor_por_hora = float(input("Calculadora salarial!\nValor por hora: "))
horas_mes = float(input("Informe suas horas trabalhadas no mês atual: "))

calculo_total_pagamento = valor_por_hora * horas_mes

print(f"Pagamento final: R$ {calculo_total_pagamento:.2f}")
# %%

#Faça um programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

def conversao_fahrenheit_para_celsius(valor):
    try:
        if isinstance(valor,(int,float)):
            valor_convertido = 5*((valor-32)/9)
            return valor_convertido
        else:
            print("Apenas números!")
    except (ValueError,TypeError):
        print(f"Digite apenas números inteiros ou Float!")
temperatura_em_f = float(input("Temperatura em Fahrenheit: "))
print(f"{conversao_fahrenheit_para_celsius(temperatura_em_f):.2f} f°")


# %%
#Faça um programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

def conversao_celsius_para_fahrenheit(valor):
    try:
        if isinstance(valor,(int,float)):
            valor_convertido = (valor * (9/5)) + 32
            return valor_convertido
        else:
            print("Apenas números!")
    except (ValueError,TypeError):
        print(f"Digite apenas números inteiros ou Float!")

temperatura_em_c = float(input("Temperatura em C°: "))
print(f"{conversao_celsius_para_fahrenheit(temperatura_em_c):.2f} f°")

# %%
'''Faça um programa que peça 2 números inteiros e um número real. Calcule e mostre:
- O produto do dobro do primeiro com metade do segundo .
- A soma do triplo do primeiro com o terceiro.
- O terceiro elevado ao cubo.'''

def conversao_str_para_float (valor):
    try:
        if not isinstance(valor,(str)):
            print(f" Valor não é um STR!\n Valor atual: {type(valor)}")
        else:
            tratamento = valor.strip().replace(",",".").split()
            uniao = ''.join(tratamento)
            print(uniao)

            transformado = float(uniao)
            return(transformado)
    except ValueError or SyntaxError as E: 
        print(f"Error: {E}")

teste_numero: int = 1
teste_str : str = "2,3"
type(conversao_str_para_float(teste_str))


#%%
numero_01: int = int(input("Informe um valor INT: "))
numero_02: int = int(input("Informe outro valor INT: "))
numero_03  = str(input("Informe um número Real: "))

calculo_produto = (numero_01 * 2) * (numero_02/2) 
calculo_soma = (numero_01 * 3) + numero_03
calculo_area_cubo = numero_03 ** 3

print(calculo_produto, calculo_soma, calculo_area_cubo)
# %%
