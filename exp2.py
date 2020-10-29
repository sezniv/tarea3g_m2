# modelo de prueba tarea grupal 3 mod2 
# claudio caniullan 

def hora_seg(hora):
	seg = hora*3600
	return seg
	

def minutos_seg(minutos):
	seg = minutos*60
	return seg




def saludos(total_seg):

	s = total_seg

	if s >= 21600 and s < 43200:
		print('Mañana')

	elif s >= 43200 and s < 61200:
		print('Tarde')

	elif s >= 61200 and s < 72000:
		print('Atardecer')

	elif s >= 72000 and s < 86400:
		print('Noche')

	elif s >= 0 and s < 7200:
		print('Noche')

	elif s >= 7200 and s < 21600:
		print('Madrugada')

	else:
		print('ingrese correctamente')


# construir funcion
def estacion():
	pass




# transformar hh:mm en segundos 
print('A continuacion ingrese la hora del dia en formato hh:mm')
hora = int(input('ingrese la hora: '))
minutos = int(input('ingrese los minutos: '))

a = hora_seg(hora)
b = minutos_seg(minutos)
total_seg = a + b 


print('La cantidad de segundos desde las 00:00 hrs son: ')
print(str(total_seg) + ' segundos')

# Emitir Saludos 
c = saludos(total_seg)
print(str(c))

# Falta implementar funcion, preguntar dia, mes y hemisferio
print('A continuacion ingrese la fecha de hoy en formato DD:MM e indique hemisferio')
mes = int(input('ingrese mes: '))
dia = int(input('ingrese dia: '))
hem = int(input('ingrese el hemisferio en el que se encuentra: '))

input()
