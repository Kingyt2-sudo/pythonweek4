def modify_file(Loises_file, Timothies_filename):
    try:
        with open(Loises_filename, 'r') as infile:
            content = infile.read()
            modified_content = content.upper()  
        
        with open(Timothies_filename, 'w') as outfile:
            outfile.write(modified_content)
        print(f"Modified content has been written to {Timothies_filename}")
    
    except FileNotFoundError:
        print(f"The file {Loises_filename} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

