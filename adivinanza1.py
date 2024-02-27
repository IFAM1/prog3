import random
print('=================================')
print('Bienvenido Al Juego de Adivinanza')
print('=================================')

numero_secreto=random.randrange(1,101)

print('Seleccione el nivel de dificultad')
print('(1) Facil (2) Medio (3) Dificil')

nivel = int(input('Ingrese nivel de dificultad: '))

if(nivel==1):
  total_intentos = 20
elif(nivel==2):
  total_intentos = 10
else:
  total_intentos = 5


for iteracion in range(1,total_intentos+1):
  print('Intento: {} de {} '.format(iteracion,total_intentos))
  entrada= input('Digite un Numero: ')
  entrada= int(entrada)
  print('Digitaste...', entrada)
  if(entrada<1 or entrada>100):
    print('Ingresa un numero entre 1 y 100')
    continue

  acertaste = entrada == numero_secreto #iguales
  mayor = entrada > numero_secreto #entrada es MAYOR
  menor = entrada < numero_secreto #entrada es MENOR


  if(acertaste):
    print('Felicitaciones !!! ... adivinaste el numero')
  elif(mayor):
    print('Lo siento ... el numero que ingresaste es mayor que el numero secreto')
  else:
    print('Lo siento ... el numero que ingresaste es menor que el numero secreto')

  iteracion = iteracion+1

print('Fin del juego')