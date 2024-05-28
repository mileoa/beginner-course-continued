import os.path

def delete_folder_without_subfolders(path):
    if not os.path.isdir(path):
        return False
    dir_list = os.listdir(path)
    for i in range(len(dir_list)):
        if os.path.isdir(os.path.join(path, dir_list[i])):
            return False
    for i in range(len(dir_list)):
        try:
            os.remove(os.path.join(path, dir_list[i]))
        except Exception:
            print("Ошибка удаления.")
            return False
    return True

print(delete_folder_without_subfolders("./folder"))