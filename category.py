import re

def extract_category_names(input_file, output_file):
    with open(input_file, 'r') as f:
        content = f.read()

    categories = re.findall(r'"CategoryName":\s*"([^"]+)"', content)

    formatted_categories = ',\n'.join([f'\t\t"{category}"' for category in categories])

    with open(output_file, 'w') as f:
        f.write(formatted_categories)

    print(f"Category names extracted and saved to {output_file}")

input_file = 'TraderPlusPriceConfig.json'

output_file = 'TraderPlusPriceConfig.txt'

extract_category_names(input_file, output_file)
