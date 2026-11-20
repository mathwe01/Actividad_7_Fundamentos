entregas = [
    ("U2026001", "tarea1_final.pdf", 1, 18, "entrega completa"),
    ("U2026002", "tarea1_v2.docx", 2, 15, "Corrigio formato"),
    ("U2026003", "informe.pdf", 1, 12, "Falta conclusion"),
    ("U2026004", "proyecto_final.zip", 3, 20, "Excelente"),
    ("U2026005", "tarea1_v2_final.pdf", 2, 17, "Segunda version"),
    ("U2026006", "borrador.docx", 1, 10, "Incompleto"),
    ("U2026007", "laboratorio.py", 4, 14, "Muchos intentos"),
    ("U2026008", "tarea1_v1.pdf", 1, 16, "Correcto"),
    ("U2026009", "resumen_final.docx", 2, 19, "Bien redactado"),
]

def mostrar_entregas(lista):
    print(f"{'Codigo':<10}{'Archivo':<22}{'Intentos':<10}{'Puntaje':<9}Observacion")
    print("-" * 70)
    for codigo, archivo, intentos, puntaje, obs in lista:
        print(f"{codigo:<10}{archivo:<22}{intentos:<10}{puntaje:<9}{obs}")
        
def sumar_puntajes(lista, indice=0):
    if indice == len(lista):
        return 0
    return lista[indice][3] + sumar_puntajes(lista, indice + 1)

def total_puntajes(lista):
    for entrega in lista:
        if entrega[3] < 0:
            raise ValueError("El puntaje no puede ser negativo")
        return sumar_puntajes(lista)
    
def buscar_codigo(lista, codigo, indice=0):
    if indice == len(lista):
        return None
    if lista[indice][0] == codigo:
        return lista[indice]
    return buscar_codigo(lista, codigo, indice + 1)

def buscar_entrega(lista, codigo):
    codigo = codigo.strip().upper()
    if codigo == "":
        raise ValueError("El codigo de busqueda no puede estar vacío")
    return buscar_codigo(lista, codigo)

def contar_archivos(lista, palabra, indice=0):
    if indice == len(lista):
        return 0
    suma = 1 if palabra in lista[indice][1].lower() else 0
    return suma + contar_archivos(lista, palabra, indice + 1)

def contar_palabra_clave(lista, palabra):
    palabra = palabra.strip().lower()
    if palabra == "":
        raise ValueError("La palabra clave no puede estar vacía")
    return contar_archivos(lista, palabra)

def potencia(base, exponente):
    if exponente < 0:
        raise ValueError("El exponente no puede ser negativo")
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)

def sumar_puntajes_iterativo(lista):
    total = 0
    for entrega in lista:
        total += entrega[3]
    return total

def buscar_codigo_iterativo(lista, codigo):
    for entrega in lista:
        if entrega[0] == codigo:
            return entrega
    return None

def contar_archivos_iterativo(lista, palabra):
    contador = 0
    for entrega in lista:
        if palabra in entrega[1].lower():
            contador += 1
    return contador

def ejecutar_pruebas():
    pruebas = [
        ("Caso base", "potencia(0, 5)", 1, potencia(5, 0)),
        ("Caso recursivo simple", "potencia(2, 3)", 8, potencia(2, 3)),
        ("Lista vacía", "buscar_codigo([], 'U2026001')", None, buscar_codigo([], "U2026001")),
        ("Codigo existente", "buscar_codigo(entregas, 'U2026003')", "informe.pdf", buscar_codigo(entregas, "U2026003")[1]),
        ("Codigo inexistente", "buscar_codigo(entregas, 'U2026099')", None, buscar_codigo(entregas, "U2026099")),
        ("Comparacion iterativa", "sumar_puntajes vs iterativa", sumar_puntajes_iterativo(entregas), sumar_puntajes(entregas)),
    ]
    print(f"{'Prueba':<24}{'Esperado':<14}{'Obtenido':<14}Resultado")
    print("-" * 62)
    for nombre, entrada, esperado, obtenido in pruebas:
        estado = "OK" if esperado == obtenido else "FALLO"
        print(f"{nombre:<24}{str(esperado):<14}{str(obtenido):<14}{estado}")
        
    
def menu():
    while True:
        print()
        print("1. Mostrar entregas")
        print("2. Suma total de puntajes")
        print("3. Buscar codigo de estudiante")
        print("4. Contar archivos por palabra clave")
        print("5. Calcular potencia")
        print("6. Comparar recursivo e iterativo")
        print("7. Ejecutar pruebas")
        print("0. Salir")
        opcion = input("Opcion: ")
        print()
        try:
            if opcion == "1":
                mostrar_entregas(entregas)
            elif opcion == "2":
                print("Suma total de puntajes:", total_puntajes(entregas))
            elif opcion == "3":
                codigo = input("Codigo a buscar: ")
                resultado = buscar_entrega(entregas, codigo)
                if resultado is None:
                    print("Codigo no encontrado")
                else:
                    print("Encontrado", resultado)
            elif opcion == "4":
                palabra = input("Palabra clave: ")
                print("Archivos encontrados:", contar_palabra_clave(entregas, palabra))
            elif opcion == "5":
                try:
                    base = int(input("Base: "))
                    exponente = int(input("Exponente: "))
                except ValueError:
                    raise ValueError("Debe ingresar numeros enteros")
                print("Resultado:", potencia(base, exponente))
            elif opcion == "6":
                print("Sumatoria recursiva", sumar_puntajes(entregas))
                print("Sumatoria iterativa", sumar_puntajes_iterativo(entregas))
                print("Conteo recursivo 'final':", contar_archivos(entregas, "final"))
                print("Conteo iterativo 'final':", contar_archivos_iterativo(entregas, "final"))
            elif opcion == "7":
                ejecutar_pruebas()
            elif opcion == "0":
                print("Programa finalizado")
                break
            else:
                print("Opcion no valida")
        except ValueError as error:
            print("Error:", error)
            
        
    
if __name__ == "__main__":
    menu()