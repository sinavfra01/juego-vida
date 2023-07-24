import random


def main():
    B = "."
    color_rojo = '\033[91m'
    color_reset = '\033[0m'
    pare = color_rojo + "+" + color_reset
#   ------------------------------------------------------------
#   Definir los alcances del progrmama
    n = 20       #Tamaño total de la matriz
    menor = 8     #Tamano de la matriz a mostrar dentro de (n)
    epocas = 100   #Define el rango de epocas a calcular
    steps = 2      #Define el avance de casillas hacia cualquier direccion una vez seleccionada la epoca
    cvi = 3        #Define aproximadamente el porcentaje de celulas vivas iniciales // porcent≈[100/(cvi+1)]%
#   ------------------------------------------------------------
    coordenadas_limite = [[0, 0], [menor-1, 0], [0, menor-1], [menor-1, menor-1]]
    direcciones = ["w", "a", "s", "d", "e", "n"]
    imagenes = []

    coo = [[k, i] for k in range(n) for i in range(n)]
    punt_cruz = [B for m in range(cvi)]
    punt_cruz.append(pare)

    matrix = [punt_cruz[random.randint(0, cvi)] for km in range(n**2)]

    e = len(matrix)
    for i in range(n):
        cara = ""
        temp = matrix[e-n:e]
        temp = temp[::-1]
        for celula in temp:
            cara += celula
            cara += " "
        print(cara)
        e -= n

    copia = list(matrix)
    imagenes.append(copia)

    cont = 1
    rango = range(n**2)
    for contPrincipal in range(epocas):
        if cont != 0:
            cont = 0
            eliminar = []
            agregar = []
            for i in coo:
                cercanas = [(i[0]+1, i[1]-1), (i[0]+1, i[1]), (i[0]+1, i[1]+1), (i[0], i[1]+1), (i[0]-1, i[1]+1),
                            (i[0]-1, i[1]), (i[0]-1, i[1]-1), (i[0], i[1]-1)]
                coordenada_i = matrix[conversor_coordenadas(i, n)]
                if coordenada_i == pare:
                    cruces = 0
                    for k in cercanas:
                        coordenada_k = conversor_coordenadas(k, n)
                        if (k[0] >= 0 and k[1] >= 0) and (coordenada_k in rango):
                            if matrix[coordenada_k] == pare:
                                cruces += 1

                    if cruces not in range(2, 4):
                        eliminar.append(i)
                        cont += 1
                else:
                    cruces = 0
                    for k in cercanas:
                        coordenada_k = conversor_coordenadas(k, n)
                        if (k[0] >= 0 and k[1] >= 0) and coordenada_k in rango:
                            if matrix[coordenada_k] == pare:
                                cruces += 1
                    if cruces == 3:
                        agregar.append(i)
                        cont += 1

            if len(eliminar) > 0:
                for k in eliminar:
                    matrix[conversor_coordenadas(k, n)] = B
            if len(agregar) > 0:
                for j in agregar:
                    matrix[conversor_coordenadas(j, n)] = pare

#           Agrega la imagen generda a la lista de epocas
            copia = list(matrix)
            imagenes.append(copia)

        else:
            break
    while True:
        epoca = input("Introduce la epoca requerida: ")
        try:
            epoca = int(epoca)
        except:
            print("Solo puedes introducir nuemros enteros, intenta de nuevo")
            continue

        try:
            if epoca not in range(len(imagenes)):
                raise ValueError("La epoca seleccionada esta fuera del rango disponible, intenta de nuevo")
        except ValueError as Ve:
            while True:
                print(Ve)
                epoca = int(input(f"Introduce una epoca valida (0, {len(imagenes)-1}):  "))

                try:
                    if epoca in range(len(imagenes)):
                        break
                except:
                    continue

        proceso(coordenadas_limite, n, imagenes[epoca], menor)

        while True:
            direccion = input("Direccion (e/ exit, n/ seleccionar epoca): ").lower()

            try:
                if direccion not in direcciones:
                    raise ValueError("La direccion proporcionada no se encuentra dentro de las opciones")
            except ValueError as ve:
                print(ve)
                print("Direcciones validas (w/a/s/d/e/n)")
                continue

            if direccion == "w":
                mover_arrib(coordenadas_limite, n, steps)
                proceso(coordenadas_limite, n, imagenes[epoca], menor)

            elif direccion == "a":
                mover_izquierda(coordenadas_limite, n, steps)
                proceso(coordenadas_limite, n, imagenes[epoca], menor)

            elif direccion == "s":
                mover_abaj(coordenadas_limite, steps)
                proceso(coordenadas_limite, n, imagenes[epoca], menor)

            elif direccion == "d":
                mover_derecha(coordenadas_limite, steps)
                proceso(coordenadas_limite, n, imagenes[epoca], menor)

            elif direccion == "e":
                exit()

            elif direccion == "n":
                break


def mover_abaj(coordenadas_limite, steps):
    if coordenadas_limite[0][0] >= steps:
        coordenadas_limite[0][0] = (coordenadas_limite[0][0])-steps
        coordenadas_limite[1][0] = (coordenadas_limite[1][0])-steps
        coordenadas_limite[2][0] = (coordenadas_limite[2][0])-steps
        coordenadas_limite[3][0] = (coordenadas_limite[3][0])-steps


def mover_arrib(coordenadas_limite, n, steps):
    if coordenadas_limite[3][0] <= n-1-steps:
        coordenadas_limite[0][0] = (coordenadas_limite[0][0])+steps
        coordenadas_limite[1][0] = (coordenadas_limite[1][0])+steps
        coordenadas_limite[2][0] = (coordenadas_limite[2][0])+steps
        coordenadas_limite[3][0] = (coordenadas_limite[3][0])+steps


def mover_derecha(coordenadas_limite, steps):
    if coordenadas_limite[1][1] >= steps:
        coordenadas_limite[0][1] = (coordenadas_limite[0][1])-steps
        coordenadas_limite[1][1] = (coordenadas_limite[1][1])-steps
        coordenadas_limite[2][1] = (coordenadas_limite[2][1])-steps
        coordenadas_limite[3][1] = (coordenadas_limite[3][1])-steps


def mover_izquierda(coordenadas_limite, n, steps):
    if coordenadas_limite[3][1] <= n-1-steps:
        coordenadas_limite[0][1] = (coordenadas_limite[0][1])+steps
        coordenadas_limite[1][1] = (coordenadas_limite[1][1])+steps
        coordenadas_limite[2][1] = (coordenadas_limite[2][1])+steps
        coordenadas_limite[3][1] = (coordenadas_limite[3][1])+steps


def limites(coordenadas_limite):
    lim1 = []
    lim2 = []
    for i in range(coordenadas_limite[0][0], (coordenadas_limite[1][0])+1):
        lim1.append([i, coordenadas_limite[0][1]])
        lim2.append([i, coordenadas_limite[2][1]])
    return lim1, lim2


def imagen_mostrar(lim1, lim2, menor, n, matrix):
    img = []
    for i in range(menor):
        for k in range(lim1[i][1], (lim2[i][1])+1):
            coordenadas = ([lim1[i][0], k])
            img.append(matrix[conversor_coordenadas(coordenadas, n)])
    return img


def conversor_coordenadas(coordenada, n):
    indice = ((n*coordenada[0])+coordenada[1])
    return indice


def proceso(coordenadas_limite, n, matrix, menor):
    lim1, lim2 = limites(coordenadas_limite)
    img = imagen_mostrar(lim1, lim2, menor, n, matrix)

    l = menor ** 2
    for i in range(menor):
        cara = ""
        temp = img[l-menor:l]
        temp = temp[::-1]
        for celula in temp:
            cara += celula
            cara += " "
        print(cara)
        l -= menor


if __name__ == '__main__':
    main()
