import os
import re
import argparse
import requests
from tqdm import tqdm
from pprint import pprint

def extract_urls_from_markdown_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        urls = re.findall(r'\[.*?\]\((.*?)\)', content)  # Extract URLs from markdown links
        return [url for url in urls if "http" in url]

def parse_markdown_files_in_directory(directory):
    markdown_files = [os.path.join(root, file) for root, dirs, files in os.walk(directory) for file in files if file.endswith('.md')]
    all_urls = []
    for file_path in markdown_files:
        urls_in_file = extract_urls_from_markdown_file(file_path)
        all_urls.extend(urls_in_file)
    return all_urls

def is_url_valid(url):
    try:
        response = requests.head(url, allow_redirects=True)
        return response.status_code == 200
    except requests.RequestException:
        return False

def main(args):
    directory = args.directory
    urls = parse_markdown_files_in_directory(directory)
    print(f"Checking {len(urls)} URLs...")
    invalid_urls = []
    for url in tqdm(urls):
        if not is_url_valid(url):
            invalid_urls.append(url)
    pprint(invalid_urls)
    print(f"Found {len(invalid_urls)} invalid URLs in {directory}. Saved log to invalid_urls.txt")
    with open('invalid_urls.txt', 'w') as f:
        for url in invalid_urls:
            f.write(f"{url}\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('directory', help='Path to the directory containing markdown files')
    args = parser.parse_args()

    main(args)