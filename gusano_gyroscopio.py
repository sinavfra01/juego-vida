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
    gusano = [[3, 3]]
    r = 0

    matriz[conversor(gusano[0])] = white
    sense.set_pixels(matriz)
    matriz = list(reseteador)
    time.sleep(0.5)

    while True:
        if r == 0:
            r = 1
            xe = [random.randint(0, 6), random.randint(0, 6)]
            if xe not in gusano:
                matriz[conversor(xe)] = red
                reseteador[conversor(xe)] = red
            else:
                continue

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
            #cas_ant = list(gusano[0])
            cas_sig = [gusano[0][0], gusano[0][1]+direccion[1]]

            if cas_sig in gusano or (cas_sig[1] < 0 or cas_sig[1] > 7):
                continue
            else:
                for i in range(len(gusano)):
                    coor = [gusano[i][0], gusano[i][1] + direccion[1]]
                    gusano[i] = coor
                    matriz[conversor(coor)] = white

                if reseteador[conversor(cas_sig)] == red:
                    #gusano.append(cas_ant)
                    reseteador[conversor(cas_sig)] = black
                    r = 0
                #
        else:
            #cas_ant = list(gusano[0])
            cas_sig = [gusano[0][0]+direccion[1], gusano[0][1]]

            if cas_sig in gusano or (cas_sig[0] < 0 or cas_sig[0] > 7):
                continue
            else:
                for i in range(len(gusano)):
                    coor = [gusano[i][0] + direccion[1], gusano[i][1]]
                    gusano[i] = coor
                    matriz[conversor(coor)] = white

                if reseteador[conversor(cas_sig)] == red:
                    #gusano.append(cas_ant)
                    reseteador[conversor(cas_sig)] = black
                    r = 0

        sense.set_pixels(matriz)
        matriz = list(reseteador)
        time.sleep(0.5)


def conversor(coordenada):
    indice = (8*coordenada[0])+coordenada[1]
    return indice


if __name__ == "__main__":
    main()
    print("Fin del programa")
