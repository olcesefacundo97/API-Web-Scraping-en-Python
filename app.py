from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def scrape_metadata(url):
    try:
        # Realiza una solicitud HTTP a la URL proporcionada
        response = requests.get(url)
        response.raise_for_status()
        
        # Utiliza BeautifulSoup para analizar el HTML de la página
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extrae metadatos clave (título, descripción, URL)
        title = soup.title.string if soup.title else None
        description = soup.find('meta', attrs={'name': 'description'})['content'] if soup.find('meta', attrs={'name': 'description'}) else None
        
        return {'title': title, 'description': description, 'url': url}
    
    except Exception as e:
        return {'error': str(e)}
    
@app.route('/scrape', methods=['GET'])
def scrape_endpoint():
    url = request.args.get('url')
    
    if not url:
        return jsonify({'error': 'Debes proporcionar una URL válida'}), 400
    
    metadata = scrape_metadata(url)
    return jsonify(metadata)

if __name__ == '__main__':
    app.run(debug=True)