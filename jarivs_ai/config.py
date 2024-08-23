import requests
import subprocess
import sys

def install_module(module_name):
    """
    Install a Python module using pip.
    
    :param module_name: The name of the module to install.
    :return: None or an error message.
    """
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", module_name])
        print(f"Module '{module_name}' installed successfully.")
    except subprocess.CalledProcessError as e:
        return f"Failed to install module '{module_name}'. Error: {e}"



def google_search(query, api_key, search_engine_id):
    """
    Perform a Google search using the Google Custom Search JSON API.
    
    :param query: The search query string.
    :param api_key: Your Google Custom Search API key.
    :param search_engine_id: Your Google Custom Search Engine ID.
    :return: List of search results (titles and links).
    """
    url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={api_key}&cx={search_engine_id}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        results = response.json().get('items', [])
        search_results = [(item['title'], item['link']) for item in results]
        return search_results
    else:
        return f"Error: {response.status_code} - {response.text}"