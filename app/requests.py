import urllib,json
from .models import Quote


base_url = None

def configure_request(app):
  global base_url 
  base_url = app.config['QUOTE_BASE_URL']


def get_random_quote():
  with urllib.request.urlopen(base_url) as url:
        quote_data = url.read()
        quote_response = json.loads(quote_data)

        if quote_response:
            author = quote_response.get('author')
            id = quote_response.get('id')
            quote = quote_response.get('quote')

            quote = Quote(id, author, quote)
            return quote

  return Quote(1, "Rosemary Tajeu", "Protect your peace.")
