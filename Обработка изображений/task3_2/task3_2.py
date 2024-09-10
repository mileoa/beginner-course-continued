from PIL import Image, ImageDraw, ImageFont
from scan_folder import scan_folder, get_extension

COLOR_RED_HEX = "#ff0000"


def change_filename_extension(file_name, new_extension):
    # Если имя файла пусто или новое расширение пусто,
    # то нет смысла обрабатывать.
    if file_name == "" or new_extension == "":
        return
    # Удаляем старое расширение.
    file_name_without_extension = list(file_name)
    try:
        for i in range(len(get_extension(file_name))):
            file_name_without_extension.pop(len(file_name_without_extension) - 1)
    except Exception:
        return
    # Добавляем новое расширение.
    assert len("".join(file_name_without_extension) + new_extension) >= 3
    return "".join(file_name_without_extension) + new_extension


def convert_images(old, new):
    # Ищем в текущей папке файлы с нужным расширением.
    for i in scan_folder(".", old, False)[1]:
        with Image.open(i) as im:
            text_to_draw = "Hello,\nWorld!"
            draw = ImageDraw.Draw(im)

            # Выбераем шрифт.
            font = ImageFont.load_default(7)

            # Центр рисунка.
            image_center = [im.width / 2, im.height / 2]

            # Определяем размеры квадрата.
            if im.width <= im.height:
                square_half_side_len = (im.width / 4) / 2
            else:
                square_half_side_len = (im.height / 4) / 2

            # Определяем размеры текста.
            l, t, text_height, text_width = draw.multiline_textbbox(
                [
                    image_center[0] - square_half_side_len,
                    image_center[1] - square_half_side_len,
                ],
                text_to_draw,
                font,
            )

            # Если изображение слишком маленькое, то нарисовать квадрат
            # и сделать надпись не получится.
            if im.width < text_width or im.height < text_height:
                continue

            # Рисуем квадрат.
            # Смещаемся от центра картинки на половину
            # длинны стороны квадрата.
            draw.rectangle(
                [
                    image_center[0] - square_half_side_len,
                    image_center[1] - square_half_side_len,
                    image_center[0] + square_half_side_len,
                    image_center[1] + square_half_side_len,
                ],
                None,
                COLOR_RED_HEX,
            )

            # Добавляем текст.
            draw.multiline_text(
                [
                    image_center[0] - square_half_side_len,
                    image_center[1] - square_half_side_len,
                ],
                text_to_draw,
                COLOR_RED_HEX,
            )

            im.save(change_filename_extension(i, new))
            del draw


convert_images("jpg", "png")
