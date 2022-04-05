from pdf2image import convert_from_path
import os


def convert_pdf_to_img(input_path, output_path):
    print("start convert from pdf to img")
    for input_file in os.listdir(input_path):
        os.mkdir(output_path + input_file[:-4] + "/")
        pages = convert_from_path(input_path + input_file)
        for i, page in enumerate(pages):
            output_file = f'{output_path}{input_file[:-4]}/{i + 1}.jpg'
            page.save(output_file, "JPEG")
    print("finish convert from pdf to img")


class Converter:
    def __init__(self):
        pass

