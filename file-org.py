import os
import shutil
import argparse

# Dictionary mapping categories to file extensions
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Scripts": [".py", ".js", ".html", ".css"],
}

def get_arguments():
  parser = argparse.ArgumentParser(description='Organize files in a folder by type.')
  parser.add_argument('folder', help='Path to the folder you want to organize')
  return parser.parse_args()

def organize_folder(folder_path):
  for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

    if os.path.isdir(file_path):
      continue

    _, extension = os.path.splitext(filename)

    moved = False
    for category, extensions in FILE_TYPES.items():
      if extension.lower() in extensions:
        move_file(file_path, folder_path, category)
        moved = True
        break

    if not moved:
      move_file(file_path, folder_path, 'Others')
    
def move_file(file_path, folder_path, category):
  category_folder = os.path.join(folder_path, category)
  if not os.path.exists(category_folder):
    os.makedirs(category_folder)

  new_path = os.path.join(category_folder, os.path.basename(file_path))

  shutil.move(file_path, new_path)
  print(f'Moved: {file_path} --> {new_path}')

def main():
  args = get_arguments()
  folder_path = args.folder
  
  if not os.path.exists(folder_path):
    print('❌ The folder does not exist!')
    return

  organize_folder(folder_path)
  print('✅ Organization complete!')

if __name__ == '__main__':
  main()