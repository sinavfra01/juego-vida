from sense_hat import SenseHat
import random
import time


def main():
    sense = SenseHat()
    sense.clear()

    white = (255, 255, 255)
    red = (255, 0, 0)
    black = (0, 0, 0)

    matriz = [black for i in range(8**2)]
    reseteador = list(matriz)
    gusano = [[0, 2], [0, 1], [0, 0]]
    r = 0

    for coordenada in gusano:
        matriz[conversor(coordenada)] = white

    sense.set_pixels(matriz)
    matriz = list(reseteador)
    time.sleep(0.65)

    while True:
        while True:
            if r == 0:
                xe = [random.randint(0, 6), random.randint(0, 6)]
                if xe not in gusano:
                    r = 1
                    matriz[conversor(xe)] = red
                    reseteador[conversor(xe)] = red
            else:
                break

        x, y, z = sense.get_accelerometer_raw().values()
        x = round(x, 0)
        y = round(y, 0)

        if x == -1:
            direccion = [0, -1]
        elif y == 1:
            direccion = [1, 1]
        elif y == -1:
            direccion = [1, -1]
        else:
            direccion = [0, 1]

        if direccion[0] == 1:
            cas_sig = [gusano[0][0], gusano[0][1] + direccion[1]]
            if cas_sig in gusano[2:]:
                break
            if (cas_sig == gusano[0] or cas_sig == gusano[1]) or (cas_sig[1] < 0 or cas_sig[1] > 7):
                continue
            else:
                if reseteador[conversor(cas_sig)] == red:
                    r = 0
                    reseteador[conversor(cas_sig)] = black
                    gusano.append('especio de relleno')
                    for i in range(len(gusano) - 1, 0, -1):
                        gusano[i], gusano[i - 1] = gusano[i - 1], gusano[i]
                        matriz[conversor(gusano[i])] = white
                    gusano[0] = cas_sig
                    matriz[conversor(gusano[0])] = white
                else:
                    for i in range(len(gusano) - 1, 0, -1):
                        gusano[i], gusano[i - 1] = gusano[i - 1], gusano[i]
                        matriz[conversor(gusano[i])] = white
                    gusano[0] = cas_sig
                    matriz[conversor(gusano[0])] = white
        else:
            cas_sig = [gusano[0][0] + direccion[1], gusano[0][1]]
            if cas_sig in gusano[2:]:
                break
            if (cas_sig == gusano[0] or cas_sig == gusano[1]) or (cas_sig[0] < 0 or cas_sig[0] > 7):
                continue
            else:
                if reseteador[conversor(cas_sig)] == red:
                    r = 0
                    reseteador[conversor(cas_sig)] = black
                    gusano.append('especio de relleno')
                    for i in range(len(gusano) - 1, 0, -1):
                        gusano[i], gusano[i - 1] = gusano[i - 1], gusano[i]
                        matriz[conversor(gusano[i])] = white
                    gusano[0] = cas_sig
                    matriz[conversor(gusano[0])] = white
                else:
                    for i in range(len(gusano) - 1, 0, -1):
                        gusano[i], gusano[i - 1] = gusano[i - 1], gusano[i]
                        matriz[conversor(gusano[i])] = white
                    gusano[0] = cas_sig
                    matriz[conversor(gusano[0])] = white

        sense.set_pixels(matriz)
        matriz = list(reseteador)
        time.sleep(0.65)


def conversor(coordenada):
    indice = (8*coordenada[0])+coordenada[1]
    return indice


if __name__ == "__main__":
    main()
    print("Fin del programa")
