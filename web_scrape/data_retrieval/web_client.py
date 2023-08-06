import requests

def get_html_content(url):
    """
    Fetches the HTML content of a web page.

    Parameters:
        url (str): The URL of the web page to fetch.

    Returns:
        str: The HTML content of the web page.
    """
    try:
        response = requests.get(url)
        response.raise_for_status # Raise an exception for 4xx and 5xx status codes
        return response.text
    
    except requests.exceptions.RequestException as e:
        # Handle connection errors or other exceptions
        print(f"Error fetching content from {url}: {e}")
        return None

# Example usage:
if __name__ == "__main__":
    target_url = "https://news.google.com"
    html_content = get_html_content(target_url)

    if html_content:
        print(html_content)
    else:
        print("Else part")                        
