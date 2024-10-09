import random
import warnings
warnings.filterwarnings("ignore", category=SyntaxWarning)

lista_random = ["gato", "perro", "casa", "arbol", "montaña", "rio", "cielo", "libro", "coche", "ciudad"]

print('Bienvenida al juego del Ahorcado. Las reglas son simples:')
print('1. Tendrás que adivinar la palabra oculta, letra a letra.')
print('2. Si la letra está en la palabra, se desvelará su posición de la palabra oculta.')
print('3. Si la letra no está en la palabra, aparecerá una parte del cuerpo del ahorcado.')
print('4. El juego termina cuando adivines la palabra o cuando agotes las 7 vidas del ahorcado.')
print('----------------------------------------------------------------------------------------')
print('¡Mucha suerte!')

palabra_random = random.choice(lista_random) 

p_oculta = list('_' * len(palabra_random))

print(f"Palabra oculta: {" ".join(p_oculta)}")

intentos = 7

letras_falladas = []

letras_sugeridas = []

numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 

horca = ('''
      +---+
      |   |
      O   |
     \|/  |
      |   |
     / \  |
          |
    =========''', '''
      +---+
      |   |
      O   |
     \|/  |
      |   |
       \  |
          |
    =========''', '''
      +---+
      |   |
      O   |
     \|/  |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |/  |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
          |
          |
          |
          |
          |
    =========''')

while intentos != 0:
      letra = input('Prueba una letra').lower()

      if letra in numeros:
            print(f'{letra} es un número. Prueba con una letra de verdad.')
            continue
      
      if letra in letras_sugeridas:
            print(f'Ya has probado la letra {letra}, prueba otra distinta.')
            continue

      else:
            letras_sugeridas.append(letra)

      print(f'Probamos la letra "{letra}"')
      if letra in palabra_random:
            for indice in range(len(palabra_random)):
                  if letra == palabra_random[indice]:
                        p_oculta[indice] = letra
            if intentos != 7:
                  print((horca[intentos]))
                  print('Letras erróneas:', ", ".join(letras_falladas))
            else:
                  pass    
            
            print(" ".join(p_oculta))
      else:
                
            intentos -= 1
            print((horca[intentos]))

            letras_falladas.append(letra)
            print('Letras erróneas:', ", ".join(letras_falladas))
            print(" ".join(p_oculta))

      if '_' not in p_oculta:
            print(f'La palabra oculta es: {palabra_random}')
            print("Enhorabuena! Has ganado la partida")
            break
      print("-------------------------------")

else:
    print('Has perdido')
    print('''
      +---+
      |   |
      O   |
     /|\  |
      |   |
     / \  |
          |
    =========''')