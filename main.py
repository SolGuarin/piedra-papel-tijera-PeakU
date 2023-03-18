import random
import time


def piedra_papel_tijera(name):

    options = ['piedra', 'papel', 'tijera']
    options_emoji = {
        "piedra": "✊",
        "papel": "🖐",
        "tijera": "🤞"
    }

    cont_machine = 0
    cont_human = 0

    while (cont_human < 3) and (cont_machine < 3):
        machine = random.choice(options)
        human = input(f'{name}, elige una opción: \n ✊ piedra \n 🖐 papel \n 🤞 tijera \n Escribe tu elección: ')
        result = ''

        if human in options:
            if machine == human:
                result = 'Restulado: 🙊 Empate '
            elif (machine == "piedra" and human == 'tijera') or (machine == "papel" and human == 'piedra') or (machine == "tijera" and human == 'papel'):
                result = 'Resultado: ❌ Ganó la máquina'
                cont_machine += 1
            else:
                result = f'Resultado: ✅ Ganó {name}'
                cont_human += 1
            print(" ")
            print(f'Máquina:   {options_emoji[machine]} {machine}')
            print(f'{name}: {(7 - len(name)) * " "}  {options_emoji[human]} {human}')
            print(result)
            print(f"---------------------")
            time.sleep(3)
            print(f'      MARCADOR \nMáquina: {cont_machine} <--> {name}: {cont_human}')
            time.sleep(2)
            print(" ")

        else:
            print("🚨🚨🚨 Ingresa una opción válida  🚨🚨🚨")

    if cont_machine > cont_human:
        print(f'{name} PERDISTE!!! La máquina ya llegó a 3 puntos 😭😭😭😭😭😭😭😭😭' )
    else:
        print(f'{name} GANASTEEEEEEE!!!!! Ya llegaste a 3 puntos 🏆🎉🎉🏆🥳🏆🏆🥳')

    print(" ")


if __name__ == '__main__':
    print("¡ 🙌 Bienvenido al juego de PIEDRA ✊, PAPEL 🖐 O TIJERA 🤞 🙌! ")
    print("🔸En esta ocasión vas a jugar contra la máquina 🤖. El primero que complete tres puntos gana la ronda")
    print("")
    name = input('digite su nombre: ')
    print(" ")
    piedra_papel_tijera(name=name)

    while True:
        keep_playing = input("Quires volver a jugar?: s/n: ")
        if keep_playing == 's':
            piedra_papel_tijera(name=name)
        else:
            print('Gracias por jugar! 😘')
            break

