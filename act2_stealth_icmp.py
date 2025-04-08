from scapy.all import IP, ICMP, Raw, send
import time

def enviar_stealth_icmp(mensaje, destino="8.8.8.8", retardo=0.5):
    print("\n--- Enviando mensaje en modo stealth ICMP ---")
    
    for i, caracter in enumerate(mensaje):
        paquete = IP(dst=destino)/ICMP()/Raw(load=caracter)
        print(f"[{i+1}] Enviando carácter: '{caracter}' a {destino}")
        paquete.show()  # Muestra los campos del paquete
        send(paquete, verbose=0)
        time.sleep(retardo)  # pequeña pausa para no saturar

    # Enviar 'b' como último carácter de cierre
    paquete_final = IP(dst=destino)/ICMP()/Raw(load='b')
    print(f"[{len(mensaje)+1}] Enviando carácter final: 'b'")
    paquete_final.show()
    send(paquete_final, verbose=0)

    print("--- Mensaje completo enviado ---")

# Ejecutar si se llama directamente
if __name__ == "__main__":
    mensaje = input("Ingresa el mensaje cifrado a enviar: ")
    enviar_stealth_icmp(mensaje)
