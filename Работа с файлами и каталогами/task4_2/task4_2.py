import os.path
from typing import List
from scan_folder import scan_folder

def delete_folder_without_subfolders(path: str) -> bool:
    dir_list: List[List[str]] = scan_folder(path, "*", False)
    if dir_list == []:
        return False
    if len(dir_list[1]) == 0:
        return False
    for i in dir_list[0]:
        try:
            os.remove(os.path.join(path, i))
        except Exception:
            return False
    return True

print(delete_folder_without_subfolders("./folder"))