def calcular_curtosis(datos):
    n = len(datos)
    media = sum(datos) / n
    varianza = sum((x - media) ** 2 for x in datos) / (n - 1)
    desviacion_estandar = varianza ** 0.5

    curtosis = sum((x - media) ** 4 for x in datos) / ((n - 1)* desviacion_estandar ** 4)
    
    # Ajuste de Fisher para obtener la curtosis con sesgo corregido
    curtosis_final =  curtosis - 3 

    if curtosis_final > 0:
        tipo_curtosis= "Leptocúrtica"
    elif curtosis_final == 0:
        tipo_curtosis = "Mezzocúrtica"
    else:
        tipo_curtosis= "Platicúrtica"
    
    curtosis_redondeada= round(curtosis_final,4)
    return curtosis_redondeada, tipo_curtosis

# Ejemplo de uso
datos = [-1000, 2, 38, 4000]
curtosis_redondeada, tipo_curtosis = calcular_curtosis(datos)
print("El coeficiente de curtosis es: ",curtosis_redondeada," y según su resultado es: ", tipo_curtosis)