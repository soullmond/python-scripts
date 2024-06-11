import os, shutil

def copy_files(src_folder, dest_folder):
    if not os.path.exists(dest_folder):
        os.mkdir(dest_folder)

    video = ['.mp4', '.mp3', '.mkv', '.avi', '.mov']
    images = [".jpg", '.jpeg', '.png', '.gif']
    docs = ['.pdf', '.7z', '.word', '.zip', '.rar', '.xps', '.txt', '.rtf']
    allowed_ext = video + images + docs

    for root, dirs, files in os.walk(src_folder):

        for file in files:
            file_path = os.path.join(root, file)
            file_ext = os.path.splitext(file_path)[1].lower()

            if file_ext in allowed_ext:
                shutil.copy(file_path, os.path.join(dest_folder, file))

        for folder in dirs:
            folder_path = os.path.join(root, folder)
            for sub_root, sub_dirs, sub_files in os.walk(folder_path):
                for sub_file in sub_files:
                    sub_file_path = os.path.join(sub_root, sub_file)
                    sub_file_ext = os.path.splitext(sub_file_path)[1].lower()

                    if sub_file_ext in allowed_ext:
                        shutil.copy(sub_file_path, os.path.join(dest_folder, sub_file))

source_folder = r"D:\الصور\iphone photo 2024"
destination_directory = r'D:\الصور\iphone photo 2024\all'
copy_files(source_folder, destination_directory)
