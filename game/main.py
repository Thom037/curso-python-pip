#PROYECTO
#Juego de piedra, papel o tijera

#Funciones útiles, mantenibilidad en el código, separar responsabilidades
import random

#Primera función se encarga de pedir al usuario la opción, comprobar que esté bien, y que el computador tenga su propia opción. Hasta que ambos tengan opción

def choose_options ():
  
  options = ('piedra', 'papel', 'tijera')
  user_option = input('piedra, papel o tijera =>')
  user_option = user_option.lower()
  
  if not user_option in options:
    print('Opción de juego no válida ')
    #continue
    return None, None

  computer_option = random.choice(options)
  print('Computer option =>', computer_option)
  return user_option, computer_option

#Correr las reglas del juego, segunda función, necesita principalmente de las opciones que hayan tomado el usuario y el computador, devuelve el contador de los puntos de los jugadores

def check_rules(user_option, computer_option, user_wins, computer_wins):
  if user_option == computer_option :
    print ('Empate, vuelve a jugar')
    
  elif user_option == 'piedra':
    if computer_option == 'tijera': 
      print('piedra gana a tijera')
      print('User gana')
      user_wins += 1
    else:  #Computer tiene papel
      print('Papel gana a piedra')
      print('Computer gana')
      computer_wins += 1
      
  elif user_option == 'papel':
    if computer_option == 'tijera': 
      print('Tijera gana a papel')
      print('computer gana')
      computer_wins += 1
    else:  #Computer tiene piedra
      print('Papel gana a piedra')
      print('User gana')
      user_wins += 1
  elif user_option == 'tijera':
    if computer_option == 'papel': 
      print('tijera gana a papel')
      print('User gana')
      user_wins += 1
    else:  #Computer tiene piedra
      print('Piedra gana a tijera')
      print('Computer gana')
      computer_wins += 1
  return user_wins, computer_wins

#Función 03, la función es de definir al ganador teniendo en cuenta los contadores de los puntos de los jugadores

def winner(user_wins, computer_wins):
  if computer_wins == 2:
    print('El ganador es la computadora')
    return 'finish'
    
  if user_wins == 2:
    print('El ganador es el usuario')
    return 'finish'
  
def run_game():
  computer_wins = 0
  user_wins = 0
  rounds = 1
  finish = ''
  while True: #hasta que alguno de los dos gane dos veces
  
    print('*'*10)
    print('ROUNDS', rounds)
    print('*'*10)
  
    print('Puntos computadora =>', computer_wins)
    print('Puntos usuario =>', user_wins)
    rounds += 1
    
    user_option, computer_option = choose_options()
    if user_option == None:
      continue
    user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)
    finish = winner(user_wins, computer_wins)
    if finish == 'finish':
      break
run_game()