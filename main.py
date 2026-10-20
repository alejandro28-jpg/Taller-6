comentarios = []

def registrar_comentario():
    texto = input('Escriba el comentario: ').strip()
    if texto != '':
        comentarios.append(texto)
        print('Comentario registrado')
    else:
        print('No es posible registrar el comentario.')

def mostrar_comentarios():
    if len(comentarios) == 0:
        print('No hay comentarios registrados.')
    else:
        for i in range (len(comentarios)):
            print(i + 1, comentarios[i])

def buscar_comentarios():
    if len(comentarios) == 0:
        print('No hay comentarios relacionados.')
        return

    palabra = input('Palabra que se debe buscar: ').strip().lower()
    if palabra == '':
        print('Debe ingresar una palabra.')
        return

    encontrados = 0
    for i in range(len(comentarios)):
        if palabra in comentarios[i].lower():
            print(i + 1, comentarios[i])
            encontrados += 1
    
    if encontrados == 0:
        print('No se encontro ningun relacionamiento')
    else:
        print(f'Coincidencias encontradas: {encontrados}')

def mostrar_cantidad_palabras():
    if len(comentarios) == 0:
        print('No hay comentarios registrados.')
        return
    
    for i in range(len(comentarios)):
        cantidad = len(comentarios[i].split())
        print('Comentario' + str(i + 1) + ":" + str(cantidad) + 'palabras')

def seleccionar_comentario():
    mostrar_comentarios()
    numero = input('Numero del comentario: ').strip()
    
    if not numero.isdigit():
        print('Debe escribir un número valido.')
        return -1
    
    numero = int (numero)
    if numero < 1 or numero > len(comentarios):
         print('El comentario no existe en este momento.')
         return -1
    
    return numero -1 

def contar_palabra():
    if len(comentarios) == 0:
        print('No hay comentarios registrados.')
        return

    indice = seleccionar_comentario()
    if indice == -1:
        return
    
    palabra = input('Palabra a contar: ').strip().lower()
    if palabra == '':
        print('Debe escribir una palabra.')
        return

    apariciones = comentarios[indice].lower().count(palabra)
    print("La palabra '" + palabra + "' aparece " + str(apariciones) + " veces en el comentario " + str(indice + 1) + ".")

def resumen_comentario():
    if len(comentarios) == 0:
        print("No hay comentarios registrados.")
        return

    indice = seleccionar_comentario()
    if indice == -1:
        return

    palabra = input("Palabra a buscar en el resumen: ").strip().lower()
    if palabra == "":
        print("Debe escribir una palabra.")
        return

    texto = comentarios[indice]
    resumen = (len(texto), len(texto.split()), texto.lower().count(palabra))

    caracteres, palabras, apariciones = resumen
    print("Resumen del comentario " + str(indice + 1) + ":")
    print("Caracteres:", caracteres)
    print("Palabras:", palabras)
    print("Apariciones de '" + palabra + "':", apariciones)

def seleccionar_comentario():
    """Pide al usuario un número de comentario y devuelve su índice (o None si es inválido)."""
    if len(comentarios) == 0:
        print('No hay comentarios registrados.')
        return None

    mostrar_comentarios()
    seleccion = input('Seleccione el número del comentario: ').strip()

    if not seleccion.isdigit():
        print('Debe ingresar un número válido.')
        return None

    indice = int(seleccion) - 1
    if indice < 0 or indice >= len(comentarios):
        print('El comentario seleccionado no existe.')
        return None

    return indice

def contar_apariciones(texto, palabra):
    """Cuenta cuántas veces aparece una palabra completa en un texto."""
    palabras = texto.lower().split()
    veces = 0
    for p in palabras:
        if p.strip('.,;:!?¿¡()"\'') == palabra:
            veces += 1
    return veces

def contar_palabra_en_comentario():
    indice = seleccionar_comentario()
    if indice is None:
        return

    palabra = input('Palabra que se debe contar: ').strip().lower()
    if palabra == '':
        print('Debe ingresar una palabra.')
        return

    veces = contar_apariciones(comentarios[indice], palabra)
    print(f'La palabra "{palabra}" aparece {veces} vez/veces en el comentario {indice + 1}.')

def mostrar_resumen_comentario():
    indice = seleccionar_comentario()
    if indice is None:
        return

    palabra = input('Palabra que se debe buscar: ').strip().lower()
    if palabra == '':
        print('Debe ingresar una palabra.')
        return

    texto = comentarios[indice]
    caracteres = len(texto)
    palabras = len(texto.split())
    apariciones = contar_apariciones(texto, palabra)

    # El resumen se almacena en una tupla
    resumen = (caracteres, palabras, apariciones)

    print(f'\n--- Resumen del comentario {indice + 1} ---')
    print('Número de caracteres:', resumen[0])
    print('Número de palabras:', resumen[1])
    print(f'Apariciones de "{palabra}":', resumen[2])

def menu():
    opcion = ''
    while opcion != '7':
        print('\n===== MENÚ PRINCIPAL =====')
        print('1. Registrar un comentario')
        print('2. Mostrar todos los comentarios registrados')
        print('3. Buscar comentarios que contengan una palabra')
        print('4. Mostrar la cantidad de palabras de cada comentario')
        print('5. Contar apariciones de una palabra en un comentario')
        print('6. Mostrar resumen de un comentario')
        print('7. Salir')

        opcion = input('Seleccione una opción: ').strip()

        if opcion == '1':
            registrar_comentario()
        elif opcion == '2':
            mostrar_comentarios()
        elif opcion == '3':
            buscar_comentarios()
        elif opcion == '4':
            mostrar_cantidad_palabras()
        elif opcion == '5':
            contar_palabra_en_comentario()
        elif opcion == '6':
            mostrar_resumen_comentario()
        elif opcion == '7':
            print('Saliendo del programa...')
        else:
            print('Opción no válida. Intente de nuevo.')

menu()
