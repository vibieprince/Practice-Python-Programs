from num2words import num2words  # Import num2words library to convert numbers to words
import re  # Import regular expressions

def replace_numbers_with_words(text):
    """Replaces all numbers in the text with their word equivalents."""
    def number_to_word(match):
        number = int(match.group())  # Extract the matched number
        return num2words(number)  # Convert number to words
    
    # Replace all numbers in the text using regex
    updated_text = re.sub(r'\d+', number_to_word, text)
    return updated_text

def process_file(input_file, output_file):
    """Reads the file, replaces numbers with words, and writes the updated content."""
    try:
        # Read the input file
        with open(input_file, 'r') as file:
            content = file.read()

        # Replace numbers with words
        updated_content = replace_numbers_with_words(content)

        # Write the updated content to a new file
        with open(output_file, 'w') as file:
            file.write(updated_content)
        
        print("File processed successfully! Updated content saved in", output_file)

    except FileNotFoundError:
        print("Error: The file does not exist!")

# Example Usage
input_filename = "input.txt"   # Replace with your actual input file name
output_filename = "output.txt" # Replace with your desired output file name

process_file(input_filename, output_filename)
