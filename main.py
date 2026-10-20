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
