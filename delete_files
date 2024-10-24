import os
import glob

# 定義隨身碟掛載路徑
base_path = r"F:\VOICE"

# 需要處理的資料夾名稱
folders = ['FOLDER01', 'FOLDER02', 'FOLDER03', 'FOLDER04', 'FOLDER05', 'FOLDER06']

# 遍歷每個資料夾
for folder in folders:
    folder_path = os.path.join(base_path, folder)
    
    # 使用 glob 模組搜尋資料夾中的所有 MP3 檔案
    mp3_files = glob.glob(os.path.join(folder_path, '*.mp3'))
    
    # 刪除每個 MP3 檔案
    for mp3_file in mp3_files:
        try:
            os.remove(mp3_file)
            print(f"刪除檔案: {mp3_file}")
        except Exception as e:
            print(f"無法刪除 {mp3_file}: {e}")

print("檔案刪除完成，資料夾已保留。")
