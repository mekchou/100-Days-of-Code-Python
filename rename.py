import os
import re
from datetime import datetime

def remove_number_substrings(filename):
    # Remove any substrings of the form "(number)"
    return re.sub(r'\(\d+\)', '', filename)

def rename_files_by_creation_date(folder_path):
    # Get a list of all files in the folder
    files = os.listdir(folder_path)
    
    # Create a list of tuples with file names and their creation dates
    file_dates = [(file, os.path.getctime(os.path.join(folder_path, file))) for file in files]
    
    # Sort the list of file dates by creation date
    file_dates.sort(key=lambda x: x[1])
    
    # Iterate over the sorted list and rename the files sequentially
    for i, (file, _) in enumerate(file_dates):
        # Remove number substrings from the file name
        file_no_numbers = remove_number_substrings(file)
        
        # Remove leading or trailing spaces
        file_cleaned = file_no_numbers.strip()
        
        # Generate the new file name
        new_name = f"{i+1}_{file_cleaned}"
        
        # Rename the file
        os.rename(os.path.join(folder_path, file), os.path.join(folder_path, new_name))
        print(f"Renamed {file} to {new_name}")

# Example usage
folder_path = r'D:\VAVdo\all\TG'
rename_files_by_creation_date(folder_path)
