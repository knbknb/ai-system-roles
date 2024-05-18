import requests
import re
import json
from bs4 import BeautifulSoup
# set base url
base_url = 'https://docs.anthropic.com/'
base_path = 'en/prompt-library/'
url = base_url + base_path + 'dream-interpreter'
css_selector = 'div h5~li a'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
elements = soup.select(css_selector)
prompt_data = []
for element in elements:
    prompt_data.append([element.text, element.get('href')])

print(len(prompt_data))
print(prompt_data[0])

prompt_data_processed = []
for title, link in prompt_data:
    response = requests.get(base_url + link)
    soup = BeautifulSoup(response.text, 'html.parser')
    selector1 = '.mt-8 > table:nth-child(2) tbody tr:first-child'
    selector2 = 'header .prose p'
    # process both these selectors at the same time
    elements1 = soup.select(selector1)
    elements2 = soup.select(selector2)
    for element1 in elements1:
        txt = element1.text.strip()
        txt = re.sub(r'^User\s*|System\s*', '', txt)
        prompt_data_processed.append([title, txt ])
    i = 0
    for element2 in elements2:
        header = element2.text.strip()
        prompt_data_processed[-1].append(header)
    print(f'{title} -> {prompt_data_processed[-1]}') if len(prompt_data_processed) > 0 else None

print(prompt_data_processed)

#reorder the data: 0 -> 0, 1-> 2, 2 -> 1
#prompt_data_processed = [ [x[0] , x[2] , x[1]  ] for x in prompt_data_processed]
#
# save to JSON file
with open('anthropic-prompts.json', 'w') as f:
    json.dump(prompt_data_processed, f, indent=2)