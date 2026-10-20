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
