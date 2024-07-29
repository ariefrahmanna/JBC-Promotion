import re

def extractNoWA(no_path):
    a = '\\'
    no_path = no_path.replace('\\', a)
    with open(no_path, 'r', encoding='utf-8') as file:
        content = file.read()
    match = re.search(r'"(.*?)"', content)
    extracted_text = match.group(1) 
    modified_text = extracted_text.replace(" ", "").replace("-", "")
    phone_numbers = modified_text.split(',')
    phone_numbers = [number for number in phone_numbers if not re.search(r'[a-zA-Z]', number)]
    return phone_numbers