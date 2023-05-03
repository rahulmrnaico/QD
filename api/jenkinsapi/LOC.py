import os
import fnmatch

# Replace these values with your own
DIRECTORY_PATH = 'F:\Others\works\Python\QD'
LANGUAGE_EXTENSION = '.json'

print("hello")
total_lines_of_code = 0
language_lines_of_code = 0

# Recursively traverse the directory and count the lines of code
for root, dirnames, filenames in os.walk(DIRECTORY_PATH):
    for filename in fnmatch.filter(filenames, f'*{LANGUAGE_EXTENSION}'):
        with open(os.path.join(root, filename), 'r', encoding='utf-8') as file:
            lines = file.readlines()
            total_lines_of_code += len(lines)
            language_lines_of_code += len([line for line in lines if line.strip() != ''])
            with open ('writeme.txt', 'w') as file:  
                file.write(str(total_lines_of_code)) 
 
# Print the results
print(f'Total lines of code: {total_lines_of_code}')
print(f'Lines of code in {LANGUAGE_EXTENSION}: {language_lines_of_code}')