
import cv2, io
import os
import numpy as np
from tqdm import tqdm

def image_cut(input_path, output_path):
    input_folders = os.listdir(input_path)
    for paper in tqdm(input_folders, desc="convert jpg -> bin"):
        input_folder = input_path + paper
        # output_folder = output_path + paper
        # os.mkdir(output_folder)
        input_files = os.listdir(input_folder)
        for input_file in input_files:
            input_image = input_folder+"/"+input_file
            # output_image = output_folder + "/" + input_file
            output_image = output_path  + paper+"_"+ input_file
            img_cv = cv2.imread(input_image)
            img_cv = img_cv[150:, :]
            cv2.imwrite(output_image, img_cv)
