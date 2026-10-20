# Taller-6
Taller logica de programacion en grupos
Preguntas de análisis
1. ¿Qué diferencia existe entre aplicar lower() y modificar directamente un carácter
de la cadena? RT1: La diferencia es que cuando aplico un .lower en el programa, no cambio la lista original, es decir creo otra lista con la modificación del lower.(minúsculas) y modificar directamente un carácter dentro de una lista de forma directa no se puede.  
2. ¿Por qué split() devuelve una lista y no una tupla? RT2: Porque el split se usa para cambiar un elemento o modificar los elementos existentes, por lo cual devuelve una lista y no una tupla.
3. ¿Qué resultado se obtiene con "Hola hola".lower().count("hola")? RT3: se obtiene un resultado de 2, porque el lower hace que "Hola hola" se vuelta un "hola hola" y el .count lo que hace es contar cuantas veces está repetido "hola".
4. ¿Qué ocurriría si se intentara ejecutar resumen[0] = 100? RT6: El resultado sería un error porque no se puede modificar una tupla.
5. ¿En qué situación del ejercicio sería más conveniente una lista que una tupla? RT5: Cuando los datos se requieren cambiar, en el ejercicio si se quisiera cambiar para que las palabras se fueran acumulando sería mejor una lista en vez de la tupla que hay.
