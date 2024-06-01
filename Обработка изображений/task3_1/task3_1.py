from PIL import Image
from scan_folder import scan_folder, get_extension

def change_extension_for_filename(file_name, new_extension):
    if file_name == "" or new_extension == "":
        return
    file_name_without_extension = list(file_name)
    try:
        for i in range(len(get_extension(file_name))):
            file_name_without_extension.pop(len(file_name_without_extension) - 1)
    except Exception:
        return
    assert len("".join(file_name_without_extension) + new_extension) >= 3
    return "".join(file_name_without_extension) + new_extension

def convert_images(old, new):
    for i in scan_folder(".", old, False)[1]:
        with Image.open(i) as im:
            im.save(change_extension_for_filename(i, new))

convert_images("jpg", "png")
