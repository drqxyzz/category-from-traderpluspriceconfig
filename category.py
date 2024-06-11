import re

def extract_category_names(input_file, output_file):
    with open(input_file, 'r') as f:
        content = f.read()

    # Use regular expression to find all occurrences of "CategoryName"
    categories = re.findall(r'"CategoryName":\s*"([^"]+)"', content)

    # Convert category names to the desired format
    formatted_categories = ',\n'.join([f'\t\t"{category}"' for category in categories])

    with open(output_file, 'w') as f:
        f.write(formatted_categories)

    print(f"Category names extracted and saved to {output_file}")

# Replace 'input_file.json' with the path to your input file
input_file = 'TraderPlusPriceConfig.json'

# Replace 'output_file.txt' with the desired output file name
output_file = 'TraderPlusPriceConfig.txt'

extract_category_names(input_file, output_file)
