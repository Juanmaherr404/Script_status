Verificador de Estado de URLs
Este script de Python realiza solicitudes HTTP a una lista de dominios almacenados en un archivo de texto y verifica el estado de cada URL. El resultado se guarda en un archivo resultados.txt con el código de estado HTTP y la URL correspondiente.

Requisitos
Este script utiliza la librería requests para realizar las solicitudes HTTP. Asegúrate de tenerla instalada. Si no la tienes, puedes instalarla utilizando pip:
pip install requests

Descripción
El script contiene varias funciones que permiten:

iterar_archivo: Lee un archivo línea por línea y aplica una función a cada línea.
check_status: Verifica el estado de una URL enviando una solicitud HTTP y guarda el resultado.
add_http: Asegura que las URLs tengan el prefijo correcto (http:// o https://).
write_file: Escribe los resultados de las solicitudes en un archivo de texto llamado resultados.txt.

Funcionamiento
Entrada: El script toma un archivo llamado domains que contiene una lista de URLs o dominios. Cada línea será procesada para verificar si el sitio es accesible.

Verificación de Estado: Para cada URL, el script utiliza la función requests.get() para realizar una solicitud HTTP. Si la solicitud es exitosa, registra el código de estado. Si hay un error, lo captura y lo muestra.

Salida: Los resultados de cada solicitud se almacenan en un archivo de texto resultados.txt. Cada línea en este archivo contiene el código de estado HTTP y la URL procesada.