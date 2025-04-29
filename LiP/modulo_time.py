import time

hora_atual = int(time.time())
horas = hora_atual // 3600
minutos = (hora_atual % 3600) // 60
segundos = (hora_atual % 3600) % 60
dias = hora_atual // (3600*24)

print(f'Hora atual: {horas}:{minutos}:{segundos}, ou seja, {dias} dias')