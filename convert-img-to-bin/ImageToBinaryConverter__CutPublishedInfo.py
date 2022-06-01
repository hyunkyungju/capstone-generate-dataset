import cv2, io
import os
import numpy as np
from tqdm import tqdm

def image_to_binary_cut(input_path, output_path):
    input_folders = os.listdir(input_path)
    for input_folder in tqdm(input_folders, desc="convert jpg -> bin"):
        output_folder = output_path + input_folder
        os.mkdir(output_folder)
        for i in range(1, 9):
            path = input_path+input_folder+"/"+str(i+1)+".jpg"
            img_cv = cv2.imread(path)
            if img_cv is None:
                img_cv = cv2.imread("../white.jpg")
            img_cv = img_cv[160:, :]
            resized_cv = cv2.resize(img_cv, dsize=(224, 224), interpolation=cv2.INTER_AREA)
            binary_cv = cv2.imencode('.PNG', resized_cv)[1].tobytes()
            binary_file = f'{output_folder}/{i + 1}.bin'
            with open(binary_file, "wb") as f:
                f.write(binary_cv)


def binary_to_image_cut():
    binary_file = "../../dataset/binary/iclr2021_cut/_77KiX2VIEg/2.bin"
    with open(binary_file, 'rb') as f:
        data = f.read()
    encoded_img = np.fromstring(data, dtype=np.uint8)
    img = cv2.imdecode(encoded_img, cv2.IMREAD_COLOR)
    print(img.shape)
    print(type(img))
    cv2.imshow('decoding', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
