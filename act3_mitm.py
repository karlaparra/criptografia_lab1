from scapy.all import rdpcap, ICMP, Raw
from scapy.layers.inet import IP

def descifrado_cesar(texto, desplazamiento):
    resultado = ""
    for c in texto:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            resultado += chr((ord(c) - base - desplazamiento) % 26 + base)
        elif c.isdigit():
            resultado += chr((ord(c) - ord('0') - desplazamiento) % 10 + ord('0'))
        else:
            resultado += c
    return resultado

def reconstruir_mensaje_desde_payload_icmp(archivo_pcap):
    paquetes = rdpcap(archivo_pcap)
    mensaje = ""

    for pkt in paquetes:
        if IP in pkt and ICMP in pkt and pkt[ICMP].type == 8 and Raw in pkt:
            data = pkt[Raw].load
            if len(data) > 16:
                caracter = chr(data[16])  # Byte 0x10 del payload ICMP
                mensaje += caracter

    return mensaje

def mostrar_opciones_descifrado(mensaje_cifrado):
    print("\nMensaje interceptado desde ICMP:\n", mensaje_cifrado)
    print("\n--- Posibles desplazamientos César (0 a 25) ---\n")

    palabras_clave = ["hello", "mundo", "mensaje", "criptografia", "seguridad", "redes", "en", "y", "la"]
    mejores_opciones = []
    mejor_puntaje = 0

    # Generar las 26 opciones en orden
    for d in range(26):
        descifrado = descifrado_cesar(mensaje_cifrado, d)
        contenido = descifrado.lower()
        puntuacion = sum(1 for palabra in palabras_clave if palabra in contenido)
        mejores_opciones.append((d, descifrado, puntuacion))
        mejor_puntaje = max(mejor_puntaje, puntuacion)

    # Imprimir resultados en orden ascendente por desplazamiento
    for d, mensaje, score in mejores_opciones:
        if score == mejor_puntaje and score > 0:
            print(f"\033[92m{d:02d}: {mensaje}  ← Posible descifrado (score: {score})\033[0m")
        else:
            print(f"{d:02d}: {mensaje}")

if __name__ == "__main__":
    archivo = input("Ruta del archivo .pcap o .pcapng: ")
    mensaje = reconstruir_mensaje_desde_payload_icmp(archivo)
    mostrar_opciones_descifrado(mensaje)
