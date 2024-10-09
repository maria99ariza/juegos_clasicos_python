import random

def bienvenida():
    nombre_usuario = input("Escriba tu nombre, por favor:") #solicitar el nombre de la usuaria

    print (f"¡🩵Bienvenida {nombre_usuario}🩵, vamos a empezar la diversión con nuestra elección de cada día: 'Despertador⏰ o Café☕ o Siesta😴'!")

    print("------------------------------------------------------")
    
    print(f"¿{nombre_usuario}, estas lista para ver las reglas del juego?🧐")
    print(input("Sí" "/" "No"))

    print("------------------------------------------------------")

    print(f"""🎯Las reglas son:
      * Tú puedes elegir contra quien quieres jugar: 'Python' o una compañera.
      * Hay que decir cuantos partidos es necesario para ser la campeona

    🔊Elementos del juego:
      * Despertador (posiblemente, el objeto más odidado de toda la casa☠️)
      * Siesta (Lo mejor que han inventado los españoles💃, por encima de las persianas).
      * Café (La salvación 🙏 de cada mañana).

    🔓Reglas del juego:
      * Despertador gana a la Siesta (por desgracia). 
      * Siesta gana al Café (porque, a veces, ni el café puede con ese sueño de después de comer...). 
      * Café gana a Despertador (porque después de una noche de maratón de estudios, el café será tu mejor amigo por la mañana).""")
    
    return nombre_usuario

def elegir_oponente():

    oponente = input(f"Quieres jugar contra una compañera? Si es así digita sí.")
    print("------------------------------------------------------")
    if oponente in ["sí","Sí","SÍ","sÍ", "SI", "si", "sI"]:
        oponente = input(f"Digita el nombre de tu compañera:")
    else:
        oponente = "Python"

    print (f"Tu oponente es {oponente}🤭")
    return oponente

def obtener_puntos_target():

    try:
        puntos_target = int(input(f"Cuantos partidos hay que ganar para ser la campeona de este duelo?"))
        print(f"¡OJO! 👀 tienes que ganar {puntos_target} partidas para ser la campeona.🥇")
        return puntos_target
    except:
        print(f"Por favor, hay que poner un número para que los 'puntos_target' sean válidos")
        return None
    
class GameClasico:
    def __init__ (self, nombre_usuario,oponente, puntos_target):
        self.nombre_usuario = nombre_usuario
        self.oponente = oponente
        self.puntos_target = puntos_target
        self.puntos_usuario = 0
        self.puntos_oponente = 0
        self.partidos = 0
        self.juego = ['despertador', 'siesta', 'cafe']

    
    def game(self):
        while self.puntos_usuario < self.puntos_target and self.puntos_oponente < self.puntos_target: 
      
            self.op_usuario = input (f"{self.nombre_usuario}, ⏩elige entre {self.juego}⏪")

            # Validar la elección del jugador
            while self.op_usuario not in self.juego:
                print("❌❌Elección no válida. Inténtalo de nuevo.❌❌")
                self.op_usuario = input (f"{self.nombre_usuario}, ⏩elige entre {self.juego}⏪")
                
            # Validar la elección del oponente
            if self.oponente == "Python": 

                # Generar la elección aleatoria del ordenador(Python)
                self.op_oponente = random.choice(self.juego)  
                
            else:
                self.op_oponente = input (f"{self.oponente}, elige entre {self.juego}")            
                while self.op_oponente not in self.juego:
                    print("❌❌Elección no válida. Inténtalo de nuevo.❌❌")
                    self.op_oponente = input (f"{self.oponente}, ⏩elige entre {self.juego}⏪")      
                
            # Comprobar que cada jugador ha elegido
            print(f"✔️{self.nombre_usuario} ha elegido: {self.op_usuario}")
            print(f"✔️{self.oponente} ha elegido: {self.op_oponente}")  

            # Determinar el ganador del partido
            if self.op_usuario == self.op_oponente:
                print("🟰Empate.🟰")
                self.partidos += 1

                # Mostrar los puntos actuales de cada uno y partidos
                print(f"✅Puntos - Usuario: {self.puntos_usuario}, {self.oponente}: {self.puntos_oponente}")
                print(f"✅Cantidad de partidos hasta ahora:{self.partidos}")
                print("------------------------------------")

            elif (self.op_usuario == "despertador" and self.op_oponente == "siesta") or (self.op_usuario == "siesta" and self.op_oponente == "cafe") or (self.op_usuario == "cafe" and self.op_oponente == "despertador"):
                self.puntos_usuario += 1
                self.partidos += 1
                print(f"🤞¡Ganaste esta ronda, felicidades {self.nombre_usuario}!🤞")

                # Mostrar los puntos actuales de cada uno y partidos
                print(f"✅Puntos - Usuario: {self.puntos_usuario}, {self.oponente}: {self.puntos_oponente}")
                print(f"✅Cantidad de partidos hasta ahora:{self.partidos}")
                print("------------------------------------")
                
            else:
                self.puntos_oponente += 1
                self.partidos += 1
                print(f"{self.oponente} te ha ganado este partido.🫥")

                # Mostrar los puntos actuales de cada uno y partidos
                print(f"✅Puntos - Usuario: {self.puntos_usuario}, {self.oponente}: {self.puntos_oponente}")
                print(f"✅Cantidad de partidos hasta ahora:{self.partidos}")
                print("------------------------------------")

        self.total()
        self.ganador()

    def total(self):
        print(f"""Puntos totales del duelo 🤼‍♀️:
        🔵{self.nombre_usuario}: {self.puntos_usuario}
        🟢{self.oponente}: {self.puntos_oponente}
           en un total de {self.partidos} partidos""")

    def ganador(self):
        if self.puntos_usuario == self.puntos_target:
            print(f"¡🎉🎉Felicidades {self.nombre_usuario}!🎁🏆 Has ganado el juego.🎉🎉")
        else:
            print(f"{self.oponente} te ha ganado el juego. Hay que estudiar más. ⚒️🔦📔")

nombre_usuario = bienvenida()
print("------------------------------------------------------")
oponente = elegir_oponente()
print("------------------------------------------------------")
puntos_target = obtener_puntos_target ()
print("------------------------------------------------------")

duelo1 = GameClasico(nombre_usuario,oponente,puntos_target)

duelo1.game()