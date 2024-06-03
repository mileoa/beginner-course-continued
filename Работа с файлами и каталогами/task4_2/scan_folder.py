import os.path
from typing import List

# Функция нахождения последнего вхождения элемента.
def last_char_occurrence(string: str, char: str) -> int:
    for i in range(len(string) - 1, -1, -1):
        if string[i] == char:
            assert i >= 0
            return i
    return -1

def get_extension(file_name: str) -> str | None:
    # Если файл начинается или заканчивается на '.'
    # или не имеет '.', то у него нет расширения.
    offset:int = last_char_occurrence(file_name, '.')
    if offset <= 0 or offset == len(file_name) - 1:
        return None
    extension: List[str] = []
    for i in range(offset + 1, len(file_name)):
        extension.append(file_name[i])
    assert len("".join(extension)) >= 1
    return "".join(extension)

# Функция проверки имеет ли файл нужное расширение.
def has_right_extension(file_name: str, extension: str) -> bool:
    if get_extension(file_name) != extension:
        return False
    return True

def scan_folder(folder_path: str, extension: str, scan_subfolders: bool) -> List[List[str]]:
    if not os.path.isdir(folder_path):
        return []
    folders_list: List[str] = []
    files_list: List[str] = []
    current_dir_list: List[str] = os.listdir(folder_path)

    for i in current_dir_list:
        # Если файл с нужным расширением, то добавляем в список.
        if os.path.isfile(os.path.join(folder_path, i)):
            if has_right_extension(i, extension) or extension == "*":
                files_list.append(i)
            continue

        # Если это папка, то добавляем в список.
        folders_list.append(i)

        # Проваливаемся в папку, если надо.
        if not scan_subfolders:
            continue
        subfolder_list: List[List[str]] = scan_folder(os.path.join(folder_path, i),
                                                             extension, False)
        for j in range(len(subfolder_list[0])):
            folders_list.append(subfolder_list[0][j])
        for j in range(len(subfolder_list[1])):
            files_list.append(subfolder_list[1][j])

    return [folders_list, files_list]
