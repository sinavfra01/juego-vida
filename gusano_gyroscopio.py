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
    gusano = [[1, 1] for i in range(64)]
    gusano[0] = [3, 3]
    long_gus = 1
    r = 0

    matriz[conversor(gusano[0])] = white
    sense.set_pixels(matriz)
    matriz = list(reseteador)
    time.sleep(0.8)

    while True:
        if r == 0:
            r = 1
            xe = [random.randint(0, 7), random.randint(0, 7)]
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
            cas_sig = [gusano[0][0], gusano[0][1]+direccion[1]]
            print(cas_sig)
            if cas_sig in gusano and (cas_sig[1] < 0 or cas_sig[1] > 7):
                break
            else:
                for i in range(long_gus):
                    coor = [gusano[i][0], gusano[i][1]+direccion[1]]
                    gusano[i] = coor
                    matriz[conversor(coor)] = white

                if matriz[conversor(cas_sig)] == red:
                    gusano[long_gus] = cas_sig
                    r = 0
                    reseteador[conversor(xe)] = black
                    for i in range(long_gus):
                        gusano[i], gusano[i+1] = gusano[i+1], gusano[i]
                    long_gus += 1
        else:
            cas_sig = [gusano[0][0]+direccion[1], gusano[0][1]]
            print(cas_sig)
            if cas_sig in gusano and (cas_sig[0] < 0 or cas_sig[0] > 7):
                break
            else:
                for i in range(long_gus):
                    coor = [gusano[i][0] + direccion[1], gusano[i][1]]
                    gusano[i] = coor
                    matriz[conversor(coor)] = white

                if matriz[conversor(cas_sig)] == red:
                    gusano[long_gus] = cas_sig
                    r = 0
                    reseteador[conversor(xe)] = black
                    for i in range(long_gus):
                        gusano[i], gusano[i + 1] = gusano[i + 1], gusano[i]
                    long_gus += 1

        sense.set_pixels(matriz)
        matriz = list(reseteador)
        time.sleep(0.8)


def conversor(coordenada):
    indice = (8*coordenada[0])+coordenada[1]
    return indice


if __name__ == "__main__":
    main()
    print("Fin del programa")
