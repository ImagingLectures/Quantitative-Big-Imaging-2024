from collections import defaultdict
import os
import re
import argparse
import requests
import json
from tqdm import tqdm
from pprint import pprint

"""
Check URLs in markdown files for validity.

This script checks all URLs in markdown files in a given directory for validity.

Args:
    directory (str): The directory containing markdown files

Example:

    ```bash
    python check_urls.py path/to/directory
    ```
    
"""

def extract_urls_from_markdown_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        urls = re.findall(r'\[.*?\]\((.*?)\)', content)  # Extract URLs from markdown links
        return [url for url in urls if "http" in url]

def parse_markdown_files_in_directory(directory):
    markdown_files = [os.path.join(root, file) for root, dirs, files in os.walk(directory) for file in files if file.endswith('.md')]
    all_urls = {}
    for file_path in markdown_files:
        all_urls[file_path] = extract_urls_from_markdown_file(file_path)
    return all_urls

def is_url_valid(url):
    try:
        response = requests.head(url, allow_redirects=True)
        return response.status_code == 200
    except requests.RequestException:
        return False

def main(args):
    directory = args.directory
    files_urls = parse_markdown_files_in_directory(directory)
    print(f"Checking URLs in {len(files_urls)} files...")
    invalid_urls = defaultdict(list)    
    for file in tqdm(files_urls):
        for url in files_urls[file]:
            if not is_url_valid(url):
                invalid_urls[file].append(url)
    pprint(invalid_urls)
    total_invalid_urls = sum(len(urls) for urls in invalid_urls.values())
    print(f"Found {total_invalid_urls} invalid URLs in {directory}. Saved log to invalid_urls.json")

    with open('invalid_urls.json', 'w') as f:
        f.write(json.dumps(invalid_urls, indent=4))



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('directory', help='Path to the directory containing markdown files')
    args = parser.parse_args()

    main(args)