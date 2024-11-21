input("Нажмите Enter для запуска программы")

import os
import re
from collections import defaultdict

def rename_video_files():
    # Get the current directory
    current_directory = os.getcwd()
    
    # Track occurrences of base filenames
    counter = defaultdict(int)
    
    # List all files in the current directory
    for filename in os.listdir(current_directory):
        # Check if the file is an .mp4 file
        if filename.endswith('.mp4'):
            # Strip the .mp4 extension for processing
            base_filename = filename[:-4]
            new_filename = base_filename
            
            # Remove "(1)" to "(999)" from the filename
            new_filename = re.sub(r'\(\d{1,3}\)', '', new_filename)
            
            # Remove dates in the specified formats
            new_filename = re.sub(r'\b(202[4-9]|203[0-9]|204[0-9]|205[0-9]|206[0-9]|207[0-9]|208[0-9]|209[0-9]|21[0-1][0-9])[-_\s]?(\d{1,2})?[-_\s]?(\d{1,2})?\b', '', new_filename)
            
            # Remove all alphabets and special characters except specific allowed ones
            new_filename = re.sub(r'[^0-9_\.]', '', new_filename)

            # Remove spaces
            new_filename = new_filename.replace(" ", "")
            
            # Add underscore to suffix if necessary
            # Increment the counter for the base filename
            if new_filename:
                counter[new_filename] += 1
                
                # Append suffix if this filename has been seen before
                if counter[new_filename] > 1:
                    new_filename += f"_{counter[new_filename]}"
                
                # Reattach the .mp4 extension
                new_filename += '.mp4'

                # If the new filename is modified, rename the file
                if new_filename != filename:
                    original_file_path = os.path.join(current_directory, filename)
                    new_file_path = os.path.join(current_directory, new_filename)

                    # Rename the file
                    os.rename(original_file_path, new_file_path)
                    print(f'Renamed: "{filename}" to "{new_filename}"')

# Run the function
rename_video_files()

input("Структура видеофайлов создана. Нажмите Enter для закрытия окна")

# softy_plug