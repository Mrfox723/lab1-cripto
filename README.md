# Laboratorio 1 - Criptografía y Seguridad

Este repositorio contiene el desarrollo del Laboratorio 1 de la asignatura de Criptografía y Seguridad.

## 🧪 Descripción

El objetivo del laboratorio fue demostrar cómo se puede cifrar un mensaje utilizando el algoritmo de César y luego transmitir dicho mensaje de forma encubierta a través de paquetes ICMP tipo echo-request (ping), simulando tráfico legítimo en la red. Finalmente, se desarrolló un sistema para descifrar el mensaje sin conocer el desplazamiento original, aplicando una lógica de IA basada en procesamiento de lenguaje natural.

## 📁 Contenido del repositorio

- `cesar.py`: Script que cifra un mensaje usando el algoritmo César y lo guarda en un archivo.
- `ping_secreto.py`: Envía cada letra del mensaje cifrado como un paquete ICMP a un servidor externo.
- `descifrar.py`: Lee los paquetes capturados y prueba todas las combinaciones posibles para descifrar el mensaje.
- `README.md`: Este archivo.
- Capturas de pantalla (`.png`) que respaldan el funcionamiento del laboratorio.
- `mensaje_cifrado.txt`: Archivo generado automáticamente con el mensaje cifrado.

## 🧰 Herramientas utilizadas

- Python 3
- Scapy
- NLTK
- Wireshark
- Git y GitHub
- LaTeX para informe final

## 📸 Evidencia del funcionamiento

Algunas de las capturas incluidas en este repositorio:

- Envío de mensaje oculto por ping (`ping_secret.png`)
- Ejecución de consola (`cmd_ping_secret.png`)
- Análisis con Wireshark (`wireshark_ping.png`)
- Resultado del descifrado (`cmd_decifrar.png`)

## 📌 Autor

**Javier González Zapata**  
Estudiante de Ingeniería Civil en Informática y Telecomunicaciones  
Universidad Diego Portales

---

> Este proyecto fue desarrollado con fines educativos, respetando los principios éticos y la legalidad del uso de herramientas de análisis de red.
