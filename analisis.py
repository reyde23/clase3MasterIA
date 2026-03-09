dataset = [10, 25, 37,42, 58, 63, 71, 89]

def calcular_promedio(datod):
    return sum(datos) / len(datos)

def calcular_maximo(datos):
    return max(datos)

def mostrar_resumen(datos):
    print(f"total de registros : {len(datos)}")
    print(f"promedio           : {calcular_promedio(datos):.2f}")
    print(f"maximo             : {calcular_maximo(datos)}")


mostrar_resume(dataset)
