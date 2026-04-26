import os
import shutil

# Folder you want to clean
SOURCE_FOLDER =r"C:\Users\Raman\Downloads"

# File type categories
FILE_TYPES = {
    "Images": [".png", ".jpg", ".jpeg"],
    "Videos": [".mp4"],
    "Audio": [".mp3"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx"],
    "Archives": [".zip",],
    "Programs": [".exe"]
}

def organize_files(folder_path):
    if not os.path.exists(folder_path):
        print("Folder does not exist!")
        return

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        file_ext = os.path.splitext(filename)[1].lower()

        moved = False

        for folder_name, extensions in FILE_TYPES.items():
            if file_ext in extensions:
                target_folder = os.path.join(folder_path, folder_name)

                # Create folder if it doesn't exist
                os.makedirs(target_folder, exist_ok=True)

                # Move file
                shutil.move(file_path, os.path.join(target_folder, filename))
                print(f"Moved: {filename} → {folder_name}")
                moved = True
                break

        if not moved:
            other_folder = os.path.join(folder_path, "Others")
            os.makedirs(other_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(other_folder, filename))
            print(f"Moved: {filename} → Others")

    print("Cleaning completed!")

if __name__ == "__main__":
    organize_files(SOURCE_FOLDER)