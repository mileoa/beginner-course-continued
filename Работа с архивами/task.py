from zipfile import ZipFile
import os.path

def zip_files_with_extension(zip_name, extension):
    with ZipFile(zip_name, "a") as zip:
        for i in os.listdir("."):
            if os.path.isfile(i) and i.endswith(extension):
                zip.write(i)

zip_files_with_extension("test.zip", "txt")