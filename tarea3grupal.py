## Escribir hora y día ##


#Intentar implementar if para acotar valores de entrada de los input anteriores#

def funcion1(min):
    min_seg = min*60
    return min_seg


def funcion2(hora):
    hora_seg = hora*3600
    return hora_seg

min = int(input('indique los minutos: '))
hora = int(input('indique la hora: ')) 


a = funcion1(min)
print(a)    

b = funcion2(hora)
print(b) 