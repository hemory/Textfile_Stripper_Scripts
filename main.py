import re

# Removes any numbers from the line in the text file

def remove_numbers_from_line(line):
    return re.sub(r'\d+', '', line)

def filter_numbers_from_file(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            filtered_line = remove_numbers_from_line(line)
            outfile.write(filtered_line)


def remove_pattern_and_blank_lines(line):
    # Remove the pattern "::."
    filtered_line = line.replace('::.', '')
    
    # Remove leading and trailing whitespaces, then check if the line is empty
    if not filtered_line.strip():
        return None

    return filtered_line



def filter_file(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            filtered_line = remove_pattern_and_blank_lines(line)
            if filtered_line is not None:
                outfile.write(filtered_line)

# Removes any text from the line in the text file

def remove_text_from_line(line, str_to_remove):
    return line.replace(str_to_remove, '')

def filter_file(input_file, output_file, str_to_remove):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            filtered_line = remove_text_from_line(line, str_to_remove)
            outfile.write(filtered_line)



if __name__ == "__main__":
    input_file = 'textv3.txt'  # Replace with the path to your input file
    output_file = 'output.txt'  # Replace with the path to your output file
    


