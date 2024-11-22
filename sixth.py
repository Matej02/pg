import requests
import re

def download_url_and_get_all_hrefs(url):
    """
    Stáhne obsah zadané URL stránky a vrátí všechny odkazy (href) na dané stránce.

    Args:
        url (str): URL stránky, kterou chcete analyzovat.

    Returns:
        list: Seznam všech odkazů nalezených na stránce.
    """
    try:
        # Stáhneme obsah stránky
        response = requests.get(url)
        response.raise_for_status()  # Ověříme, že request byl úspěšný
        
        # Obsah stránky
        html_content = response.text
        
        # Regulární výraz pro extrakci href
        href_pattern = r'href="(https?://[^"]+)"'
        links = re.findall(href_pattern, html_content)
        
        return links
    except requests.RequestException as e:
        print(f"Chyba při stahování stránky: {e}")
        return []

# Test funkce
if __name__ == "__main__":
    url = "https://www.jcu.cz"
    links = download_url_and_get_all_hrefs(url)
    print(f"Nalezené odkazy: {links}")
