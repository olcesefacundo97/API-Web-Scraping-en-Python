# Web Scraping API

Esta API de Web Scraping acepta una URL como parámetro y devuelve los metadatos clave de la página web correspondiente, incluyendo el título, la descripción y la URL.

## Configuración

Asegúrate de tener Python instalado en tu entorno. Puedes instalar las dependencias utilizando el siguiente comando:

```bash
pip install flask requests beautifulsoup4
```

## Uso

1. Ejecuta la aplicación Flask:

```bash
python app.py
```

1. Realiza una solicitud a la API utilizando tu navegador, `curl` o Postman. Reemplaza `<URL>` con la dirección web que deseas analizar.

```bash
http://127.0.0.1:5000/scrape?url=<URL>
```

1. Recibirás una respuesta en formato JSON con los metadatos clave de la página web.

## Ejemplo

Supongamos que deseas obtener los metadatos de la página de ejemplo "<https://www.example.com>". Puedes realizar la siguiente solicitud:

```bash
http://127.0.0.1:5000/scrape?url=https://www.example.com
```

Y la respuesta podría ser algo como:

```json
{
  "title": "Ejemplo - Página de ejemplo",
  "description": "Esto es una página de ejemplo para ilustrar el uso de la API de Web Scraping.",
  "url": "https://www.example.com"
}
```

## Notas

- Este es un ejemplo básico y local. Asegúrate de cumplir con las políticas de uso de los sitios web que intentes analizar.
- Considera las implicaciones éticas y legales del web scraping antes de implementar en un entorno de producción.
- Este proyecto se proporciona "tal cual" sin garantías.

¡Disfruta usando la API de Web Scraping!

Este README proporciona información básica sobre cómo configurar y utilizar la API. Puedes personalizarlo según tus necesidades y agregar más detalles sobre la funcionalidad, la estructura del código, las consideraciones éticas, etc.
