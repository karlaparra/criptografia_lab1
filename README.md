# Laboratorio1 de Criptografía - Actividades 1, 2 y 3

Este repositorio contiene el desarrollo completo de un laboratorio práctico de criptografía y seguridad de redes. A través de tres actividades, se implementa el cifrado César, el envío sigiloso de datos mediante paquetes ICMP y el análisis de captura de red para simular un ataque tipo MitM (Man-in-the-Middle).

---

## Estructura del proyecto

```
criptografia_lab1/
├── scripts/
│   ├── act1_cifrado_cesar.py       # Cifrado César interactivo
│   ├── act2_stealth_icmp.py        # Envío sigiloso de mensaje en ICMP
│   └── act3_mitm.py                # Descifrado desde captura ICMP (MitM)
├── captura/
│   └── msj_cifrado_ICMP.pcapng     # Captura de tráfico ICMP generado
├── README.md
```

---

## Actividad 1: Cifrado César

**`scripts/act1_cifrado_cesar.py`**
- Solicita al usuario un texto y un desplazamiento.
- Aplica el cifrado César a letras y números.
- Respeta espacios y símbolos.
- Imprime el resultado cifrado.

**Ejemplo de uso:**
```bash
python3 scripts/act1_cifrado_cesar.py
```

---

## Actividad 2: Envío ICMP Stealth

**`scripts/act2_stealth_icmp.py`**
- Envía el mensaje cifrado carácter por carácter en paquetes ICMP tipo echo-request.
- Inserta cada carácter en el byte 0x10 del campo `data`.
- Simula tráfico real con secuencias coherentes y payload estructurado.

**Ejemplo de uso:**
```bash
sudo python3 scripts/act2_stealth_icmp.py
```

> ⚠️ Se recomienda capturar el tráfico con Wireshark mientras se ejecuta el script.

---

## Actividad 3: MitM - Análisis de Captura

**`scripts/act3_mitm.py`**
- Lee una captura `.pcapng` de paquetes ICMP.
- Extrae el carácter del byte 0x10 de cada paquete ICMP tipo request.
- Reconstruye el mensaje cifrado.
- Aplica fuerza bruta al cifrado César (0–25).
- Resalta en verde la opción más probable.

**Ejemplo de uso:**
```bash
python3 scripts/act3_mitm.py
```
```
Ruta del archivo .pcap o .pcapng: captura/msj_cifrado_ICMP.pcapng
```

---

## Requisitos
- Python 3
- Scapy
- Permisos `sudo` para enviar paquetes ICMP

Instalar Scapy:
```bash
sudo pip3 install scapy --break-system-packages
```

---

## Recomendaciones
- Utilizar **Wireshark** para comparar pings reales con los generados.
- Verificar en los paquetes ICMP:
  - Timestamp
  - ID
  - Sequence number
  - Byte 0x10 del campo data (donde viaja el carácter)

---

##  Autoría
- **Nombre:** Karla Parra
- **Curso:** Criptografía y Seguridad
- **Universidad:** Universidad Diego Portales

---

##  Licencia
Este proyecto se entrega como parte de un laboratorio académico. Uso educativo únicamente.
