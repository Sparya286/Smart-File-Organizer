"""
SMART FILE ORGANIZER
Author: Sparya Arora

Description:
This program automatically organizes files in a folder
based on their existing file extensions.

It creates folders like:
Images
Documents
Videos
Music
Archives
Programs
and many more

further, moving the files accordingly.
"""


import os
import shutil
folder_path = r"TestFolder"
print("Current working directory:", os.getcwd())
print("TestFolder path:", os.path.abspath(folder_path))
print("Contents of TestFolder:", os.listdir(folder_path))
FILE_TYPES = {
    "Images": [
        ".jpg", ".jpeg", ".png", ".gif",
        ".bmp", ".svg", ".webp"
    ],

    "Documents": [
        ".pdf", ".doc", ".docx",
        ".txt", ".ppt", ".pptx",
        ".xls", ".xlsx", ".csv"
    ],

    "Videos": [
        ".mp4", ".mkv", ".mov",
        ".avi", ".flv"
    ],

    "Music": [
        ".mp3", ".wav",
        ".aac", ".ogg"
    ],

    "Archives": [
        ".zip", ".rar",
        ".7z", ".tar", ".gz"
    ],

    "Programs": [
        ".exe", ".msi",
        ".apk", ".py"
    ]
}

# Function to create folders if they don't exist

def create_folder(folder_name):

    destination = os.path.join(folder_path, folder_name)

    if not os.path.exists(destination):
        os.makedirs(destination)

    return destination

# Function to identify category

def get_category(extension):

    extension = extension.lower()

    for category, extensions in FILE_TYPES.items():

        if extension in extensions:
            return category

    return "Others"


# Main Function

def organize_files():

    moved_files = 0

    skipped_files = 0

    print("=" * 45)
    print("SMART FILE ORGANIZER")
    print("=" * 45)

    
    for file in os.listdir(folder_path):

        source = os.path.join(folder_path, file)

        # Ignore folders

        if os.path.isdir(source):
            continue

        filename, extension = os.path.splitext(file)

        category = get_category(extension)

        destination_folder = create_folder(category)

        destination = os.path.join(destination_folder, file)

        # Skip if file already exists

        if os.path.exists(destination):

            print(f"Skipped: {file} (already exists)")
            skipped_files += 1
            continue

        try:

            shutil.move(source, destination)

            print(f"Moved: {file}  --->  {category}")

            moved_files += 1

        except Exception as e:

            print(f"Error moving {file}")

            print(e)

    print("\n")

    print("=" * 45)
    print("SUMMARY")
    print("=" * 45)

    print(f"Files Moved   : {moved_files}")

    print(f"Files Skipped : {skipped_files}")

    print("Finished Successfully.")


# Program 
if __name__ == "__main__":

    organize_files()