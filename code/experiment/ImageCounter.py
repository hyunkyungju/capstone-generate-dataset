

import fitz
import io
from PIL import Image
import os
from tqdm import tqdm
import PyPDF2
from collections import defaultdict
import json


def count_image(file_path):
    pdf_file = fitz.open(file_path)
    cnt = 0

    for page_number in range(min(len(pdf_file), 9)):
        page = pdf_file[page_number]
        list_image = page.get_images()
        cnt += len(list_image)
        print("page number:", page_number, "image number:", len(list_image))

    return cnt

def count_image_by_text(file_path):
    temp = open(file_path, 'rb')
    PDF_read = PyPDF2.PdfFileReader(temp)
    for page_number in range(min(len(PDF_read.pages)-1, 8), -1, -1):
        page = PDF_read.pages[page_number]
        idx = page.extractText().rfind("Figure ")
        if idx != -1:
            txt = page.extractText()[idx+7:idx+10]
            if txt[-1]==':':
                if txt[:-1].isnumeric():
                    return int(txt[:-1])
            elif txt[-2]==':':
                if txt[:-2].isnumeric():
                    return int(txt[:-2])
    return 0

def count_image_all_pdf():
    input_path = "../../../dataset/pdf/iclr2021/"
    input_files = os.listdir(input_path)
    metadata = []
    for input_file in tqdm(input_files, desc="Count number of Images"):
        try:
            pdf = input_path + input_file
            cnt = count_image_by_text(pdf)
            pdf_metadata = {
                'forum': input_file[:-4],
                'cnt': cnt
            }
            metadata.append(pdf_metadata)
        except:
            print(f"[error] pdf: {pdf}")

    print('writing metadata to file')
    with open(os.path.join("../../", f'cnt.jsonl'), 'w') as file_handle:
        for pdf_metadata in metadata:
            file_handle.write(json.dumps(pdf_metadata) + '\n')

