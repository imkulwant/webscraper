from bs4 import BeautifulSoup

def parse_html(html_content, tag_names):
    """
    Parses the HTML content and extracts data from specified tags.

    Parameters:
        html_content (str): The HTML content of the web page.
        tag_names (list): A list of tag names to extract data from.

    Returns:
        dict: A dictionary with tag names as keys and lists of extracted data as values.
    """    
    extracted_data = {tag: [] for tag in tag_names}

    try:
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Find HTML elements and extract data for each specified tag
        for tag in tag_names:
            for element in soup.find_all(tag): # Extract all tag elements
                data = element.text.strip()
                extracted_data[tag].append(data)

    except Exception as e:
        # Handle parsing errors
        print(f"Error parsing HTML content: {e}")

    return extracted_data

# Example usage:
if __name__ == "__main__":
    
    html_content = "<html><body><h2>Item 1</h2><p>Some text</p><a href='https://example.com'>Link</a></body></html>"
    
    tags_to_extract = ['h2', 'p']
    
    extracted_data = parse_html(html_content, tags_to_extract)
    
    print(extracted_data)