def read_file_with_error_handling():
    filename = input("Please enter the filename: ")
    try:
        with open(loises_file, 'r') as file:
            content = file.read()
            print("File content:")
            print(content)
    
    except FileNotFoundError:
        print(f"Error: The file '{loises_file}' does not exist.")
    except PermissionError:
        print(f"Error: You don't have permission to read the file '{loises_file}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

read_file_with_error_handling()
