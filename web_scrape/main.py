from data_retrieval.web_client import get_html_content
from data_parsing.generic_parser import parse_html

def main():
    # Take URL input from the user
    target_url = input("Enter the URL of the web page to scrape: ")

    # Fetch the raw HTML data using the web_client module
    html_content = get_html_content(target_url)

    if html_content:
        # Extract all headings from the HTML content using the generic parser
        tags_to_extract = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']
        extracted_data = parse_html(html_content, tags_to_extract)

        # Print the extracted data as a dictionary
        print("Extracted headings")
        for tag, data_list in extracted_data.items():
            print(f"{tag}:")
            for heading in data_list:
                print(f" - {heading}")

    else:
        print("Failed to fetch HTML content.")


if __name__ == "__main__":
    main()
