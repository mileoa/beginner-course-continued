import os.path

# Функция нахождения последнего вхождения элемента.
def last_char_occurrence(string, char):
    for i in range(len(string) - 1, -1, -1):
        if string[i] == char:
            return i
    return -1

def get_extension(file_name):
    # Если файл начинается или заканчивается на '.' 
    # или не имеет '.', то у него нет расширения.
    offset = last_char_occurrence(file_name, '.')
    if offset <= 0 or offset == len(file_name) - 1:
        return
    extension = []
    for i in range(offset + 1, len(file_name)):
        extension.append(file_name[i])
    return "".join(extension)

# Функция проверки имеет ли файл нужное расширение.
def has_right_extension(file_name, extension):
    if get_extension(file_name) != extension:
        return False
    return True

def scan_folder(folder_path, extension, scan_subfolders):
    if not os.path.isdir(folder_path):
        return
    folders_list = []
    files_list = []
    current_dir_list = os.listdir(folder_path)

    for i in range(len(current_dir_list)):
        # Если файл с нужным расширением, то добавляем в список.
        if os.path.isfile(folder_path + '/' + current_dir_list[i]):
            if has_right_extension(current_dir_list[i], extension):
                files_list.append(current_dir_list[i])
            continue
        
        # Если это папка, то добавляем в список.
        folders_list.append(current_dir_list[i])
        
        # Проваливаемся в папку, если надо.
        if not scan_subfolders:
             continue
        subfolder_list = scan_folder(folder_path + '/' + current_dir_list[i],
                                     extension, False)
        for j in range(len(subfolder_list[0])):
                folders_list.append(subfolder_list[0][j])
        for j in range(len(subfolder_list[1])):
                files_list.append(subfolder_list[1][j])

    return [folders_list, files_list]

result = scan_folder(".", "py", True)
print(result[0])
print(result[1])
