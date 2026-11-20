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

    
    
    
if __name__ == "__main__":
    mostrar_entregas(entregas)
    print()
    print("Suma total de puntajes:", total_puntajes(entregas))
    print()
    
    for codigo in ["U2026004", "U2026099"]:
        resultado = buscar_entrega(entregas, codigo)
        if resultado is None:
            print(f"Codigo {codigo}: no encontrado")
        else:
            print(f"Codigo {codigo}: encontrado -> {resultado[1]}, puntaje {resultado[3]}")
            
try:
    buscar_entrega(entregas, "  ")
except ValueError as error:
    print("Error:", error)

print()
for palabra in ["final", "v2", "xyz"]:
    print(f"Archivos con '{palabra}':", contar_palabra_clave(entregas, palabra))
    
try:
    contar_palabra_clave(entregas, "")
except ValueError as error:
    print("Error:", error)

print()
for base, exp in [(2, 0), (2, 5), (3, 4)]:
    print(f"{base} elevado a {exp} =", potencia(base, exp))
    
try:
    potencia(2, -1)
except ValueError as error:
    print("Error:", error)

    
    