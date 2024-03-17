#! python3
# google_searcher.py - Opens several search results using Google Custom Search API.

import requests
import sys
import webbrowser

# Replace 'YOUR_API_KEY' and 'YOUR_SEARCH_ENGINE_ID' with your actual API key and search engine ID
API_KEY = 'API_KEY'
SEARCH_ENGINE_ID = 'SEARCH_ENGINE_ID'

def search_google(query):
    url = f'https://www.googleapis.com/customsearch/v1?q={query}&key={API_KEY}&cx={SEARCH_ENGINE_ID}'
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def open_search_results(query):
    print('Searching...')
    data = search_google(query)
    if 'items' in data:
        num_results = min(5, len(data['items']))
        for i in range(num_results):
            url = data['items'][i]['link']
            print('Opening:', url)
            webbrowser.open(url)
    else:
        print('No results found.')

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python google_searcher.py <query>')
        sys.exit(1)
    query = ' '.join(sys.argv[1:])
    open_search_results(query)
