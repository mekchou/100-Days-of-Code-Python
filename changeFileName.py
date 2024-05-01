import os

def rename_files_in_folder(folder_path, old_string, new_string):
    """
    Rename files in a folder by replacing a certain string with another string.

    Args:
    - folder_path (str): The path to the folder containing the files.
    - old_string (str): The string you want to replace.
    - new_string (str): The string you want to replace it with.
    """
    for filename in os.listdir(folder_path):
        if old_string in filename:
            new_filename = filename.replace(old_string, new_string)
            old_file_path = os.path.join(folder_path, filename)
            new_file_path = os.path.join(folder_path, new_filename)
            os.rename(old_file_path, new_file_path)
            print(f"File {filename} renamed to {new_filename}")

# Example usage:
folder_path = r"D:\VAVdo\all\AV\Uncensored\香月澪.原版母帶無水印[11.3GB]"
old_string = "bhd1080.com@"
new_string = ""
rename_files_in_folder(folder_path, old_string, new_string)
