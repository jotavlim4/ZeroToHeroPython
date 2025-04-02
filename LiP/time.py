time_in_seconds = int(input())

day = time_in_seconds // 86400 
hour = (time_in_seconds %  86400) // 3600 
minute = ((time_in_seconds %  86400) % 3600) // 60 
second = ((time_in_seconds %  86400) % 3600) % 60 

print(f"{time_in_seconds} segundos = {day} dias, {hour} horas, {minute} minutos e {second} segundos")