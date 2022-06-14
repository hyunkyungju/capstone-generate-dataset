from pdf2image import convert_from_path
import os
from tqdm import tqdm



def convert_pdf_to_img(input_path, output_path):
    print("start convert from pdf to img")
    print("input path: ", input_path)
    input_files = os.listdir(input_path)
    # os.makedirs(output_path)
    for input_file in tqdm(input_files, desc="convert pdf -> image"):
        try:
            os.mkdir(output_path + input_file[:-4] + "/")
            pages = convert_from_path(input_path + input_file)
            for i, page in enumerate(pages):
                output_file = f'{output_path}{input_file[:-4]}/{i + 1}.jpg'
                page.save(output_file, "JPEG")
        except:
            print("[error][convert pdf -> img] input file:", input_file)
    print("finish convert from pdf to img")


class Converter:
    def __init__(self):
        pass

