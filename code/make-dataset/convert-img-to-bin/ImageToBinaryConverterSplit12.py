import cv2, io
import os
import numpy as np
from tqdm import tqdm

def image_to_binary_split(input_path, output_path):
    input_folders = os.listdir(input_path)
    row = 4
    col = 3
    for input_folder in tqdm(input_folders, desc="convert jpg -> bin"):
        output_folder = output_path + input_folder
        os.mkdir(output_folder)
        for i in range(2, 10):
            path = input_path+input_folder+"/"+str(i)+".jpg"
            img_cv = cv2.imread(path)
            if img_cv is None:
                img_cv = cv2.imread("../../../white.jpg")
            img_cv = img_cv[160:, :]
            h, w, _ = img_cv.shape
            h_split = h//row
            w_split = w//col
            for r in range(row):
                for c in range(col):
                    split_cv = img_cv[h_split*r:h_split*(r+1), w_split*c:w_split*(c+1)]
                    resized_cv = cv2.resize(split_cv, dsize=(224, 224), interpolation=cv2.INTER_AREA)
                    binary_cv = cv2.imencode('.PNG', resized_cv)[1].tobytes()
                    order = r*col+c+1
                    binary_file = f'{output_folder}/{i}_{order}.bin'
                    with open(binary_file, "wb") as f:
                        f.write(binary_cv)
