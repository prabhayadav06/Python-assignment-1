
input_file = "C:/Users/PRABHA/OneDrive/Documents/New folder/input.txt"
output_file = "C:/Users/PRABHA/OneDrive/Documents/New folder/output.txt"

try:
    with open(input_file, 'r') as file_in:
        file_content = file_in.read()
    with open(output_file, 'w') as file_out:
        file_out.write(file_content)
    
    print(f"Contents from '{input_file}' copied to '{output_file}' successfully.")
    
except FileNotFoundError:
    print("Error: One or both files not found.")
except IOError:
    print("Error: Could not read/write data.")
except Exception as e:
    print(f"An error occurred: {str(e)}")

