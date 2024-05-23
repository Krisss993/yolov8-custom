import os

folder_path = './images/train/'
test_path = './images/test/'

files = os.listdir(folder_path)
for idx, file_name in enumerate(files):
    if os.path.isfile(os.path.join(folder_path, file_name)):
        file_format = os.path.splitext(file_name)[1]
        new_file_name = str(idx+1).zfill(5) + file_format
        os.rename(os.path.join(folder_path, file_name), os.path.join(folder_path, new_file_name))
        print(f"Zmieniono nazwę pliku {file_name} na {new_file_name}")

files = os.listdir(test_path)
for idx, file_name in enumerate(files):
    if os.path.isfile(os.path.join(test_path, file_name)):
        file_format = os.path.splitext(file_name)[1]
        new_file_name = str(idx+1).zfill(5) + file_format
        os.rename(os.path.join(test_path, file_name), os.path.join(test_path, new_file_name))
        print(f"Zmieniono nazwę pliku {file_name} na {new_file_name}")
