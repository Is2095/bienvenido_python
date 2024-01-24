
# Día


# datetime ---> proporciona clase para manipular fechas y horas

from datetime import datetime

actual = datetime.now() # inicializa a datetime.now, lo que vamos a poder acceder a todo lo que es la fecha actual

def imprime_fecha(dia):
    print(dia.year)
    print(dia.month)
    print(dia.day)
    print(dia.hour)
    print(dia.minute)
    print(dia.second)
    print(dia.timestamp())

imprime_fecha(actual)

timestamp = actual.timestamp() # nos da la representación única de tiempo
print(timestamp)
fecha = datetime.fromtimestamp(timestamp) # acá transformamos el timestamp en AA/MM/DD HH/MM/SS
print(fecha)

meter_fecha = datetime(2024, 1, 20) # lo mínimo para definir una fecha es AA/MM/DD
imprime_fecha(meter_fecha)
print()

# time  ----> proporciona funcionalidades para el tiempo, es un objeto para encapsular tiempo - hay que rellenarlo

from datetime import time

tiempo_actual = time(22, 8, 0)
print(tiempo_actual)
print()

# date

from datetime import date

dia_actual = date.today() # accede a la fecha actual

print(dia_actual.year)
print(dia_actual.month)
print(dia_actual.day)
print(dia_actual)
print()

dia_actual = date(1988, 1, 28) # le inyectamos AA/MM/DD
print(dia_actual.year)
print(dia_actual.month)
print(dia_actual.day)
print(dia_actual)
print()

dia_actual = date(dia_actual.year, dia_actual.month + 6, dia_actual.day)  # de esta manera podemos modificar la fecha
print(dia_actual)

# timedelta ----->   nos permite hacer operaciones como diferencias con fechas especialmente franjas de fecha

diferencia = actual - meter_fecha # se puede restar fechas pero del mismo tipo, en este caso las dos fechas son del tipo datetime
print(diferencia)
print(type(diferencia))

dife = meter_fecha.date() - dia_actual
print(dife)
print(type(dife))

from datetime import timedelta

tiempo_delta_inicio = timedelta(200, 100, 100, weeks = 10)
tiempo_delta_final = timedelta(300, 100, 100, weeks = 13)
print(tiempo_delta_final - tiempo_delta_inicio)
print(tiempo_delta_final + tiempo_delta_inicio)
