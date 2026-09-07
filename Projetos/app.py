aparelho = input('Insira o nome do aparelho: ')
potencia = float(input('Qual a potência do aparelho em Watts? '))
horasDia = float(input('Qual o tempo médio de uso diário em horas? '))
valorkWh = 0.80

consumomensal = (potencia * horasDia * 30) / 1000
customensal = consumomensal*valorkWh

print(f'Aparelho: {aparelho}')
print(f'Consumo estimado: {consumomensal:.2f} kWh/mês'.replace('.', ','))
print(f'Custo estimado: R$ {customensal:.2f}'.replace('.', ','))

