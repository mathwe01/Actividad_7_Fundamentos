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
        
        
if __name__ == "__main__":
    mostrar_entregas(entregas)

    