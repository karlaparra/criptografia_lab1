def cifrado_cesar(texto, desplazamiento):
    resultado = ""

    for caracter in texto:
        if caracter.isalpha():
            base = ord('A') if caracter.isupper() else ord('a')
            nuevo = chr((ord(caracter) - base + desplazamiento) % 26 + base)
            resultado += nuevo
        elif caracter.isdigit():
            nuevo = chr((ord(caracter) - ord('0') + desplazamiento) % 10 + ord('0'))
            resultado += nuevo
        else:
            resultado += caracter  # Espacios, símbolos, etc.

    return resultado


# Entrada desde el usuario
mensaje = input("Ingresa el texto a cifrar: ")
while True:
    try:
        desplazamiento = int(input("Ingresa el desplazamiento (número entero): "))
        break
    except ValueError:
        print("Por favor, ingresa un número válido.")

# Aplicar cifrado
cifrado = cifrado_cesar(mensaje, desplazamiento)

# Mostrar resultado
print(f"\nTexto original: {mensaje}")
print(f"Texto cifrado : {cifrado}")
