
print("\n")
hora_actual = input("Ingrese hora actual con el siguiente formato HH:MM ")

# Separo horas de minutos
horas = hora_actual[:2]
minutos = hora_actual[3:]

# Convierto horas a segundos
horas_seg = int(horas) *3600

# Convierto minutos en segundos
minutos_seg = int(minutos) * 60

# Cambio formato hora ingresada por usuario para comparativa y modifico STR a INT
hora_actual_f = hora_actual.replace(":", "")
hora_actual_f = int(hora_actual_f)

# Se establece cuantos segundos han pasado desde media noche y muestra mensaje por pantalla
desde_0000 = horas_seg + minutos_seg
print("\n")
print("Han pasado " + str(desde_0000) + " segundos desde medianoche =)")
print("\n")

# Se establecen los saludos para el usuario
if hora_actual_f >= 600 and hora_actual_f <= 1200:
    print("Que tengas una linda MAÑANA")
elif hora_actual_f >= 1201 and hora_actual_f <= 1700:
    print("Que tengas una linda TARDE")
elif hora_actual_f >= 1701 and hora_actual_f < 2000:
    print("Es buen momento para ver el ATARDECER <3")
elif hora_actual_f >= 2001 and hora_actual_f <= 2400 or hora_actual_f > 1 and hora_actual_f < 200:
    print("Ya es de NOCHE, es mejor que te prepares para ir a dormir")
elif hora_actual_f >= 201 and hora_actual_f < 559:
    print("Ve a descansar, ya es de MADRUGADA")
else:
    print("Lo siento, creo que has ingresado un formato invalido. Vuelve a intentarlo")
print("\n")

fecha_actual = input("Ingresa fecha actual en el siguiente formato DD:MM ")
# Separo dia y mes
dia = fecha_actual[:2]
mes = fecha_actual[3:]
print()
hemisferio = input('¿En qué hemisferio te encuentras? "SUR" o "NORTE": ')
h_sur = "SUR"
h_norte = "NORTE"


# determinamos la estacion del año 
if hemisferio ==  h_norte:
    if int(dia) >= 1 and int(dia) <= 31 and int(mes) >= 3 and int(mes) <= 5:
        print("Estas en primavera")
    elif int(dia) >= 1 and int(dia) <= 31 and int(mes) >= 6 and int(mes) <= 8:
        print("Estas en verano")
    elif int(dia) >= 1 and int(dia) <= 31 and int(mes) >= 9 and int(mes) <= 11:
        print("Estas en otoño")
    elif int(dia) >= 1 and int(dia) <= 31 and int(mes) >= 12 and int(mes) <= 2:
        print("Estas en invierno")
    else:
        print("Al parecer ocurrió un error, continuaremos mejorando nuestro programa. Por favor vuelve a intentarlo 'NORTE' ")
elif hemisferio == h_sur:
    if int(dia) >= 1 and int(dia) <= 31 and int(mes) >= 9 and int(mes) <= 11:
        print("Estas en primavera")
    elif int(dia) >= 1 and int(dia) <= 31 and int(mes) >= 12 and int(mes) <= 2:
        print("Estas en verano")
    elif int(dia) >= 1 and int(dia) <= 31 and int(mes) >= 3 and int(mes) <= 5:
        print("Estas en otoño")
    elif int(dia) >= 1 and int(dia) <= 31 and int(mes) >= 6 and int(mes) <= 8:
        print("Estas en invierno")
    else:
        print("Al parecer ocurrió un error, continuaremos mejorando nuestro programa. Por favor vuelve a intentarlo 'SUR' ")
else:
    print("vuelve a intentarlo, ingresa el formato correcto 'ELSE de IF' ")