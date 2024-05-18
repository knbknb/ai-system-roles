#!/usr/bin/env python3
# Description: This script scrapes the Anthropic prompt library and saves the data to a JSON file.
# There are ~65 prompts in the library. 
# The script fetches the prompt title, the prompt text, and the prompt header.
# knb 2024-05
# dependencies: 
# pip3 install requests beautifulsoup4

import requests
import re
import json
from bs4 import BeautifulSoup

# Set base URL and path
base_url = 'https://docs.anthropic.com/'
base_path = 'en/prompt-library/'
url = f'{base_url}{base_path}dream-interpreter'
css_selector = 'div h5~li a'

# Fetch and parse the initial page
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
elements = soup.select(css_selector)

prompt_data = [(element.text, element.get('href')) for element in elements]

print(len(prompt_data))
print(prompt_data[0])

prompt_data_processed = []

for title, link in prompt_data:
    response = requests.get(f'{base_url}{link}')
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Process selectors
    elements1 = soup.select('.mt-8 > table:nth-child(2) tbody tr:first-child')
    elements2 = soup.select('header .prose p')
    
    if elements1:
        txt = elements1[0].text.strip()
        txt = re.sub(r'^User\s*|System\s*', '', txt)
        processed_entry = [title, txt]
        
        if elements2:
            header = elements2[0].text.strip()
            processed_entry.append(header)
        
        prompt_data_processed.append(processed_entry)
        print(f'{title} -> {processed_entry}')

print(prompt_data_processed)

with open('anthropic-prompts.json', 'w') as f:
    json.dump(prompt_data_processed, f, indent=2)