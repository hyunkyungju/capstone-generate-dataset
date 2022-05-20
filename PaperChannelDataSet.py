from torch.utils.data import Dataset
from PIL import Image
import jsonlines
import os
from tqdm import tqdm
import cv2
import numpy as np
import torch

class PaperChannelDataSet(Dataset):
    def __init__(self, overall_image_path, transform=None):
        print("initialize data sets")
        self.transform = transform
        rating_dict = {}
        self.paper_path_list = list()
        self.score_list = list()
        years = ["2021"]
        for year in years:
            year_image_path = overall_image_path+"iclr"+year+"/"
            with jsonlines.open(f"iclr{year}_metadata.jsonl") as read_file:
                for line in read_file.iter():
                    rating_dict[line['forum']] = line['rating']
            input_paths = os.listdir(year_image_path)
            for one_file_image_path in tqdm(input_paths, desc="make data set"):
                paper_path = year_image_path + one_file_image_path + "/"
                self.paper_path_list.append(paper_path)
                rating = rating_dict[one_file_image_path]
                self.score_list.append(rating)

    def __len__(self):
        return len(self.paper_path_list)

    def __getitem__(self, idx):
        lst = list()
        paper_path = self.paper_path_list[idx]
        label = self.score_list[idx]
        for i in range(9):
            binary_file = f"{paper_path}{i+1}.bin"
            with open(binary_file, 'rb') as f:
                data = f.read()
            encoded_img = np.fromstring(data, dtype=np.uint8)
            img = cv2.imdecode(encoded_img, cv2.IMREAD_COLOR)
            if self.transform is not None:
                img = self.transform(img)
                print("img shape:", img.shape)
            lst.append(img)
        tensor = torch.cat(lst, 0)
        return tensor, label