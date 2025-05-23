# Transaccion-Bancaria
Programa que genera un informe minimalista de transacciones bancarias

# 🏦 Informe de Transacciones Bancarias (CLI)

## 📌 Introducción

El presente proyecto consiste en una aplicación de línea de comandos (CLI) que procesa un archivo CSV con transacciones bancarias. El objetivo es generar un reporte con el balance final, la transacción de mayor monto y el conteo de transacciones por tipo. En esta oportunidad, el codigo se realizo en lenguaje python en un sistema operativo Windows con la documentacion necesaria para una facil lectura.

---

## 🚀 Instrucciones de Ejecución

### ✅ Requisitos

- Para poder ejecutarlo correctamente, se requiere tener instalado **Python 3.7 o superior**.
- Tener un entorno de desarrollo, en este ejemplo se uso **Visual Studio Code**.

### 💻 Instalacion del Entorno de Desarrollo

1. **Instalar Visual Studio Code (Al trabar en un OS Windows, se recomienda descargarlo directamente de Microsoft Store por las actuzalizacione automaticas) **  
   Como segunda opcion, se puede descargar desde [https://code.visualstudio.com/](https://code.visualstudio.com/)

2. **Instalacion Python**  
   Descargar e instalar desde [https://www.python.org/downloads/](https://www.python.org/downloads/)  
   Asegúrarse de marcar la casilla **"Add Python to PATH"** durante la instalación.

3. **Abrir VS Code y añadir las siguientes extensiones para una programacion mas amena**:
   - 🐍 **Python** (de Microsoft)
   - 🐍 **Pylance** (intellisense y autocompletado avanzado)
   - 🌈 **Rainbow CSV** (sirve para tener una mejor visualizacion de archivos CSV)

4. **Abrir la carpeta donde se ubica proyecto desde VS Code**:
   La carpeta contiene el codigo, ademas de 2 archivos con extension .csv para hacer pruebas
   Al ya estar dentro de la carpeta, solo es necesario abrir la terminal que se direccionara directamente a la ruta donde se encuentra el proyecto
   Un vez abierta la consola, escribir 'python main.py' para ejecutar el codigo y obtener en consola unos resultados semejantes a los siguientes:

     ```
   Reporte de Transacciones
   ---------------------------------------------
   Balance Final: 325.00
   Transacción de Mayor Monto: ID 3 - 200.00
   Conteo de Transacciones: Crédito: 3  Débito: 2
   ```

