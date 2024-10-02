import requests

# Función que itera sobre un archivo de texto, línea por línea, y aplica una función sobre cada línea.
def iterar_archivo(path, funcion):
    try:
        with open(path, "r") as archivo:
            # Itera sobre cada línea del archivo
            for linea in archivo:
                # Elimina espacios en blanco o saltos de línea
                limpio = linea.strip()
                # Aplica la función pasada como parámetro a la línea procesada
                funcion(limpio)
    # Captura un error si el archivo no existe
    except FileNotFoundError:
        print("Ese archivo no existe")
    # Captura cualquier otro tipo de excepción y la imprime
    except Exception as error:
        print("[Error] " + error)

# Función que verifica el estado de una URL, haciendo una solicitud HTTP
def check_status(url):
    # Asegura que la URL tenga el prefijo "http://" o "https://"
    url = add_http(url)
    try:
        # Hace una solicitud GET a la URL con un tiempo de espera de 5 segundos
        respuesta = requests.get(url, timeout=5)
        # Imprime el código de estado si la solicitud fue exitosa
        print(f"[OK] {respuesta.status_code} - {url}")
        # Escribe el código de estado y la URL en un archivo de resultados
        write_file(respuesta.status_code, url)
    # Captura cualquier error relacionado con la solicitud y lo imprime
    except requests.exceptions.RequestException as error:
        print(f"[Error] {error}")

# Función que agrega "https://" al inicio de la URL si no tiene "http://" o "https://"
def add_http(url):
    if not url.startswith("http://") and not url.startswith("https://"):
        # Si no empieza con "http://" o "https://", agrega "https://"
        url = "https://" + url
        return url
    else:
        # Si ya tiene el prefijo correcto, regresa la URL sin cambios
        return url

# Función que escribe en un archivo el código de estado y la URL
def write_file(code, url, file="resultados.txt"):
    # Abre el archivo en modo "a" (agregar) para no sobreescribir el contenido
    with open(file, "a") as f:
        # Escribe el código de estado y la URL en una nueva línea del archivo
        f.write(f"[{code}] - {url}\n")

# Llama a la función iterar_archivo, pasando el nombre del archivo con las URLs y la función check_status para verificar cada una
iterar_archivo("domains", check_status)
