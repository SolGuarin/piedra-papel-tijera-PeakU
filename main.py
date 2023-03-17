import random

def piedra_papel_tijera():
    nombre = input('digite su nombre: ')
    opciones_maquina = ['piedra', 'papel', 'tijera']
    maquina = random.choice(opciones_maquina)

    humano = input('Debes elegir \n 1.piedra \n 2.papel \n 3.tijera \n Escribe tu elección: ')
    resultado = ''

    if maquina == humano:
        resultado = 'Empate'
    elif (maquina == "piedra" and humano == '3') or (maquina == "papel" and humano == '1') or (maquina == "tijera" and humano == '2'):
        resultado = 'Ganó la máquina'
    else:
        resultado = 'Ganó el humano'

    print(f'la máquina eligió: {maquina} \n{nombre} eligió: {humano}')
    return resultado


if __name__ == '__main__':

    print(piedra_papel_tijera())
