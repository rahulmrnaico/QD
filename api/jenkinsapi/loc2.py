import subprocess

# Replace "path/to/directory" with the actual directory path you want to check
directory_path = "F:\Others\works\html"

# Run the cloc command and capture its output
output = subprocess.check_output(["cloc", directory_path],shell=True, cwd=r"F:\Others\works\html" )

# Convert the output to a string
output_str = output.decode("utf-8")
print(output_str)

# # Find the line that contains the "SUM" keyword
# sum_line = [line for line in output_str.split("\n") if "SUM" in line][0]

# # # Extract the number of lines of code from the "SUM" line
# num_lines_of_code = int(sum_line.split()[-1])

# print(f"Number of lines of code: {num_lines_of_code}")