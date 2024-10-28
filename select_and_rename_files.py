import os
import shutil

def find_largest_mp3(folder):
    largest_file = None
    largest_size = 0

    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith('.MP3'):
                file_path = os.path.join(root, file)
                file_size = os.path.getsize(file_path)

                if file_size > largest_size:
                    largest_size = file_size
                    largest_file = file_path

    return largest_file

def rename_and_copy_files(source_folders, name_file, destination_folder):
    # 讀取名稱列表
    with open(name_file, 'r', encoding='utf-8') as f:
        new_names = [line.strip() for line in f.readlines()]

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for i, folder in enumerate(source_folders):
        largest_mp3 = find_largest_mp3(folder)
        if largest_mp3:
            if i < len(new_names):  # 確保不超出新名稱的數量
                new_name = new_names[i]
                new_path = os.path.join(destination_folder, new_name)
                shutil.copy(largest_mp3, new_path)
                print(f'Copied and renamed: {largest_mp3} to {new_path}')
            else:
                print(f'No new name for folder {folder}, skipping.')
        else:
            print(f'No MP3 found in {folder}')

# 定義隨身碟掛載路徑
usb_mount_path = r'F:\VOICE'  # 根據實際掛載路徑設定
source_folders = [os.path.join(usb_mount_path, f'FOLDER0{i + 1}') for i in range(4)]
name_file = r'F:\names.txt'  # 包含新名稱的檔案路徑
destination_folder = os.path.join(usb_mount_path, 'New_Folder_1030')  # 新資料夾

# 執行程式
rename_and_copy_files(source_folders, name_file, destination_folder)


#### name.txt #########
# EX
# 1026.1.mp3
# 1026.2.mp3
# 1026.3.mp3
# 1026.4.mp3
#########################
