#: a dias, b horas, c minutos e d segundos
seg = int(input("Por favor, entre com o número de segundos que deseja converter: "))

dia = seg // 86400
seg = seg % 86400
hr = seg // 3600
seg = seg % 3600
min = seg // 60
seg = seg % 60

print (dia, "dias,", hr, "horas,", min, "minutos e", seg, "segundos.")
