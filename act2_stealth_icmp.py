from scapy.all import IP, ICMP, Raw, send
import time

def generar_payload(personaje):
    # Simula 56 bytes de payload (como en un ping real)
    # Inserta el carácter del mensaje cifrado en el byte 16 (posición 0x10)
    payload = bytearray(b'abcdefghijklmnopqrstuvwxyABCDEFGHIJKLMNOPQRSTUVWX1234567890')
    if len(payload) < 56:
        payload += b' ' * (56 - len(payload))
    payload[16] = ord(personaje)  # Byte 16 (0x10)
    return bytes(payload)

def enviar_stealth_icmp(mensaje, destino="8.8.8.8", retardo=0.2):
    print("\n--- Enviando mensaje ICMP Stealth con estructura realista ---\n")
    
    identificador = 0x1234  # ID ICMP fijo
    secuencia = 1

    for caracter in mensaje:
        payload = generar_payload(caracter)

        paquete = IP(dst=destino)/ICMP(type=8, id=identificador, seq=secuencia)/Raw(load=payload)

        print(f"[{secuencia}] Enviando carácter: '{caracter}'")
        send(paquete, verbose=0)

        secuencia += 1
        time.sleep(retardo)

    print("\n--- Mensaje completo enviado ---")

if __name__ == "__main__":
    mensaje = input("Ingresa el mensaje cifrado a enviar: ")
    enviar_stealth_icmp(mensaje)
